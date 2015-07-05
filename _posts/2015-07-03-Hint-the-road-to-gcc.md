---
layout: post
category : Development
tags: [c++, 'boost::optional', boost]
image : branch_prediction/hint.jpg
tagline: Premature optimization is the root of all evil - Tony Hoare (popularized by Donald Knuth)

---
{% include JB/setup %}

**How to provide the compiler with branch prediction information.**
<!--more-->

If you're a Linux kernel developer or you're working on a Linux based system, probably you've been through code with calls to **likely** and **unlikely** functions:

{% highlight cpp %}
if (unlikely(cond))
{
    /* Do something */
}
{% endhighlight %}

and

{% highlight cpp %}
if (likely(cond))
{
    /* Do something */
}
{% endhighlight %}

These two functions are nothing but that MACRO both defined in terms of a **__builtin_expect()** function, which takes two integral values as arguments, respectively the value to be tested and the expected result:

{% highlight cpp %}
#define likely(x)      __builtin_expect(!!(x), 1)
#define unlikely(x)    __builtin_expect(!!(x), 0)
{% endhighlight %}

Is quite rare to use these functions, but if you're curious to know what they are for, they are for improving performance. As first thing, let's see what the **gcc** documentation says about: 

**— Built-in Function: long __builtin_expect (long exp, long c)**
You may use __builtin_expect to provide the compiler with branch prediction information. In general, you should prefer to use actual profile feedback for this (-fprofile-arcs), as programmers are notoriously bad at predicting how their programs actually perform. However, there are applications in which this data is hard to collect.

The return value is the value of exp, which should be an integral expression. The semantics of the built-in are that it is expected that exp == c. For example:

    if (__builtin_expect (x, 0))

        foo ();

indicates that we do not expect to call foo, since we expect x to be zero. Since you are limited to integral expressions for exp, you should use constructions such as

    if (__builtin_expect (ptr != NULL, 1))

        foo (*ptr);

when testing pointer or floating-point values.


In a nutshell, *__builtin_expect()* is nothing but that an hint used by compiler to correctly optimize the branch and exploit the usage of the processor pipeline. Use *likely(x)* means that **x is expected to be true**, while *unlikely(x)* that **x is expected to be false**. The code is arranged so that the likeliest branch is executed without performing any jmp instruction, so none collateral effecta as flush the pipeline are present. This kind of speedup can have a significant impact for critical code sections. It's also pretty easy to guess where the names *likely* and *unlikely* come from: both are referring to *likelihood* in Statistics.

However, as wrote into gcc documentation, the use of both these functions is not easy at all because it can lead to counterintuitive results. As software developer, everyone should prefer to use **profiling feedback** for optimization. I wrote a short program **test_bexp** (a short name for *test branch_expected()*) just to test the performance and verify what is the better. The program just check if the first generated number corresponds to max number 100.


{% highlight cpp %}
#include <iostream>
#include <stdlib.h>
#include <time.h>

#define likely(x) __builtin_expect(!!(x),1)
#define unlikely(x) __builtin_expect(!!(x), 0)
using namespace std;
int main()
{
    static const int Max = 100;
    srand(time(NULL));
    bool found = false;
    for (int i = 0; i < 1e6; i++)
    {
        int n = (rand()% Max) + 1;
        bool cond = n == Max & i == 100;
    #ifdef LIKELY
        if (likely(cond))
    #elif defined UNLIKELY
        if (unlikely(cond))
    #else
        if (n == cond)
    #endif
            found = true;
    }
    std::cout << "Found: "<< found << endl;
}
{% endhighlight %}

We can compile four different versions of the program for results comparison (below values averaged over 20 iterations):

{% highlight bash %}
g++ -g -O3 -DUNLIKELY -o unlikely test_bexp.cpp

g++ -g -O3 -DLIKELY -o likely test_bexp.cpp

g++ -g -O3 -fprofile-generate -o normal test_bexp.cpp

g++ -g -O3 -fprofile-use -o optimised test_bexp.cpp

root@2L:~/likely# time ./likely
Found: 0

real    0m0.014s
user    0m0.012s
sys 0m0.000s

root@2L:~/likely# time ./normal
Found: 0

real    0m0.013s
user    0m0.012s
sys 0m0.000s

root@2L:~/likely# time ./unlikely
Found: 0

real    0m0.012s
user    0m0.008s
sys 0m0.000s

root@2L:~/likely# time ./optimised
Found: 0

real    0m0.011s
user    0m0.008s
sys 0m0.000s
{% endhighlight %}


How you can see from results, the optimised version beat all the other ones. It worth to note that the profiling feedback is used to made several kind of optimizations, i.e. loops, not only for branch predictions.

It is interesting the comparison of the assembly code generated, especially for the *likely* and *unlikely* versions (there are few comments to help in identifying the important parts):
{% highlight bash %}
objdump -S normal > normal.dump.txt 
objdump -S likely > likely.dump.txt 
objdump -S unlikely > unlikely.dump.txt 
objdump -S optimised> optimised.dump.txt
{% endhighlight %}

**likely.dump.txt*

{% highlight cpp %}
[...]
bool cond = n == Max & i == 100;
    #ifdef LIKELY
        if (likely(cond))
  4008a6:   83 f9 63                cmp    $0x63,%ecx
  4008a9:   75 0b                   jne    4008b6 <main+0x56> <-- Note: if cond is false, jump at 0x4008b6 and continue with the for statement
    #elif defined UNLIKELY
        if (unlikely(cond))
    #else
        if (n == cond)
    #endif
            found = true;
  4008ab:   83 fb 64                cmp    $0x64,%ebx
  4008ae:   b8 01 00 00 00          mov    $0x1,%eax
  4008b3:   0f 44 e8                cmove  %eax,%ebp
int main()
{
    static const int Max = 100;
    srand(time(NULL));
    bool found = false;
    for (int i = 0; i < 1e6; i++)
  4008b6:   83 c3 01                add    $0x1,%ebx
  4008b9:   f2 0f 10 0d 27 02 00    movsd  0x227(%rip),%xmm1        # 400ae8 <_IO_stdin_used+0x10>
  4008c0:   00 
[...]
{% endhighlight %}

**unlikely.dump.txt**
{% highlight cpp %}
[...]
bool cond = n == Max & i == 100;
    #ifdef LIKELY
        if (likely(cond))
    #elif defined UNLIKELY
        if (unlikely(cond))
  4008a5:   83 f9 63                cmp    $0x63,%ecx
  4008a8:   74 3f                   je     4008e9 <main+0x89> <-- Note: if cond is true, jump at 0x4008e9 to set found = true
int main()
{
    static const int Max = 100;
    srand(time(NULL));
    bool found = false;
    for (int i = 0; i < 1e6; i++)
  4008aa:   83 c3 01                add    $0x1,%ebx
  4008ad:   f2 0f 10 0d 33 02 00    movsd  0x233(%rip),%xmm1        # 400ae8 <_IO_stdin_used+0x10>
  4008b4:   00 

[...]

 4008e8:    c3                      retq   
    #elif defined UNLIKELY
        if (unlikely(cond))
    #else
        if (n == cond)
    #endif
            found = true;
  4008e9:   83 fb 64                cmp    $0x64,%ebx
  4008ec:   b8 01 00 00 00          mov    $0x1,%eax
  4008f1:   44 0f 44 e0             cmove  %eax,%r12d
  4008f5:   eb b3                   jmp    4008aa <main+0x4a>
  4008f7:   66 0f 1f 84 00 00 00    nopw   0x0(%rax,%rax,1)
  4008fe:   00 00 

{% endhighlight %}

I would encourage all of you in using profiling optimizations that can significantly improve performance. For a software, the knowledge of both memory and execution patterns are extremely useful for code optimization and for exploiting the hardware at the maximum level. However, not always these patterns are available, i.e. for the kernel you cannot predict the user actions. In these situations, the use of **__builtin_expect** function can be considered for a branch optimization, but keep in mind that the final result can be counterintuitive, so use it really carefully.

##Further Information

[Other Built-in Functions Provided by GCC - Gnu](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html)

[http://kernelnewbies.org/FAQ/LikelyUnlikely](http://kernelnewbies.org/FAQ/LikelyUnlikely)


