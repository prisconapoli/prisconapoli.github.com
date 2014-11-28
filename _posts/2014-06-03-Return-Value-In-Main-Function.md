---
layout: post
category : Development
tags: [Programmers' theoretical minimum, C++, main]
---
{% include JB/setup %}

**Programmers’ theoretical minimum: return value in Main function**

<!--more-->

This is a little test about the most used function in C++ programs: **main function**. 

Consider the code below:

{% highlight cpp %}
#include <iostream>
int main()
{
    std::cout << "Can I be compiled?";
}

{% endhighlight %}

The question is: **can this code be compile?**.
Before answer the question, is a good thing resume shortly the characteristics of *main*. This function is *very special*. It is called when our program starts, and its return value is checked when the program exit. The return value is extremely important because it indicate **how** the program is termintated. Conventionally, zero return value represents exit with no errors, while abnormal termination is signalled by a non-zero return value.

It should be note that a **void** return value in *main function** is **explicitly prohibited** by the **C++ ISO Standard** and should never be used. Indeed, the only valid C++ main signatures are:

{% highlight cpp %}
int main()
int main(int argc, char* argv[])
int main(int argc, char** argv)
{% endhighlight %}

Moreover, the C++ ISO Standard states:
*flowing off the end of a function is equivalent to a return with no value; this results in undefined behavior in a value-returning function*

At this point, tt seems reasonable say that the code above cannot compile. So let's try...

{% highlight bash %}
bb2l@host:~/EPC-Lec2$ g++ example1.cpp -o example1
bb2l@host:~/EPC-Lec2$ 
{% endhighlight %}

The code has compiled correctly. No errors have been found. 

Someone could objects that we haven't used any option to show warnings, so let's try again using **Wall**

{% highlight bash %}
bb2l@host:~/EPC-Lec2$ g++ -Wall esample.1 -o example1
bb2l@host:~/EPC-Lec2$ 
{% endhighlight %}

Also in this case, we can see that no errors are present.

**Why?** Isn't *main* like any other C++ function? 

Well, as said before, **main** is a **really**  a *very special function*. One of its particularity is that **it can be left without a return value**. In this case  zero is returned by default. 

 
##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)


