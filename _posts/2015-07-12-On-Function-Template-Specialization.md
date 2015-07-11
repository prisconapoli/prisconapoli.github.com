---
layout: post
category : Development
tags: [c++,  c, template, metaprogramming]
image : zen_programming/templates.jpg
tagline: A well-written program is its own Heaven; a poorly-written program is its own Hell - The Tao Of Programming

---
{% include JB/setup %}

**Don't Panic. It's just a full function template specialization**
<!--more-->

I'd like to start this new post with a little puzzle. What is the ouput of the program below?

{% highlight cpp %}
#include <iostream>
template <class T>
void func(T) {
    std::cout << "a";
}

template <class T>
void func(T*) {
    std::cout << "b";
}

template <>
void func<>(int *) {
    std::cout << "c";
}

int main()
{
    int* i;
    f(i);
}
{% endhighlight %}

If your answer is **"c"**, well you're rigth. Now, let me reorder a little bit the code.  Again, what is the ouput? 

{% highlight cpp %}
#include <iostream>
template <class T>
void func(T) {
    std::cout << "a";
}

template <>
void func<>(int *) {
    std::cout << "c";
}

template <class T>
void func(T*) {
    std::cout << "b";
}

int main()
{
    int* i;
    f(i);
}
{% endhighlight %}

If you answered **"c"** again, will, I regret to inform you that is wrong. The correct answer is **"b"**. What the hell! Why? Perhaps the compiler has a bug? Well, don't worry. The compiler is working fine. However, to figure out **why the correct answer is *"b"***, I need to give you a brief overview on templates in C++ and overloading rules.

###Templates
C++ is great. I love it. I love it more that any others programming language I know (actually I am in a strong relationship with other 4 programming languages, and I had more than 20 lovers in my life as software engineer). In my opinion, C++ is the programming language, among fews, that pushes me to think as a software architect and as an ultra skilled developer equally.
To write high quality C++ software, think at different level of abstractions in the same time is fundamental. From assembly to metaprogramming, from pipeline architecture to multithreading, from pointers to memory allocation strategies. Working with C++ is awesome and amusing.

One of the most impressive features you can find using C++ are the so called templates. In particular, there are *class templates* and *function templates*, depending if we use them with classes or functions. Class templates and function templates don't work in the same way. For classes, you can have both partial specialization and full specialization, while for functions only full specialization is permitted (partial specialization is forbidden).
The unspecialized templates are generally called **base templates**.

{% highlight cpp %}
// A class template C
template<class T, class U>
class C {};

// A partial specialization of C
template<class T>
class C<T,int>{};

// A full specialization of C
template<>
class C<bool,int>{};


// A function template func with two overloads
template<class T>  //(a)
void func(T);             

template<class T, class U>
void func(T, U);   //(b)

//A full specialization for (a)
template<>
void func<int>(int);

//A full specialization for (b)
template<>
void func<int, double>(int, double);

//A plain old function that overload with (a)
void func(int);

//A plain old function that overload with (b)
void func(int, double);

{% endhighlight %}

Now, let's give a quick look on the overloading rules to see which function get called in different situations. At high level, these rules are summarised below:

1- Plain old function, or simply non nontemplate functions, are first-class citizens. If both a nontemplate function and a function template match the parameter types,  the former will be selected. A plain old function has priority over all the other functions template.

2- If there are no plain old functions, then function base templates will be consulted. It will be selected the function base template that has the best match, ie is the most specialized, (note: in this context "specialized" has nothing to do with template specializations) according to parameter types

2.1- If there is only one **most specialized** function base template, that one will be used. Moreover, if that base template has been full specialized for the parameter types, the full specialization will be used, otherwise the base template instantiated with the correct types replaced.

2.2- If there are more than one **most specialized** function base template, the compiler cannot decide so a compilation error is  generated, with a message reporting that the call is ambiguous. At this point, is up the developer do something to disambiguate the call, ie qualifying the call.

2.3- If there is not a function base template that matches the parameter types, the call is considered wrong and an error is generated. Again,  is up the developer fix the code.

As last thing, it worth to note that order declaration matter for attributing a full specialization to a template. In this case, (c) is considered a specialization of (b). However, if (b) didn't exist, then (c) would be a valid specialization of (a). 

{% highlight cpp %}

template<class T>   // (a) a base template 
void func(T);

template<class T>   // (b) another base template, overloads with (a) 
void func(T*);       

template<>          // (c) a full specialization for (a) or (b)? Answer: (b)
void func<>(int*);
{% endhighlight %}


At this point, is a piece of cake to figure out why we have in the first puzzle the answer was **"c"** while in the second one was **"b"**. In both cases, only function base templates are considered for overloading resolution, ie (c) is taken out. And in both cases, (b) won because it is the **most specialized** template function. However, (c) order declaration is different. In the first puzzle, **(c)** is considered a specialization of **(b)**, while in the second one it is considered a specialization of **(a)**. So, this explain why the correct answer was **"c"** in the first puzzle and  **"b"** in the second one. Mystery solved ;-) 

##Further Information

[Why Not Specialize Function Templates?](http://www.gotw.ca/publications/mill17.htm), by Herb Sutter



