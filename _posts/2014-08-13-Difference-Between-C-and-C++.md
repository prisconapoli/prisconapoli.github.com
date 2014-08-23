---
layout: post
category : misc
tags: [Programmers' theoretical minimum, C, C++]
---
{% include JB/setup %}

**Small but fundamentals differences between C and C++**

<!--more-->

### Function main
In C++ there are two variants of the function *main*: **int main()** and **int main(int argc, char* *argv)**.

The ruturn type is an **int**, while in C is *void*. Moreover, it is not required to add an explicit *return 0* at the end of the function. If ommitted function *main* return 0 by default. 


###Comments
**C++** introduces an **end-of-line** comment wich starts with a double slash (//). Is it still possible continue to use the old **C** comments /\* \*/.


### Strict type checking
**C++** requires that for each function the prototype must be know before the function is called. Moreover, the call must match the prototype. The compiler can promote a basic type to another with bigger size (e.g. a *short* promoted to *int*). This mechanism is called **implicit cast** and is also present in **C**


###Sizeof char
In *C++* the size of a char is 1, while in *C* is 4. This happen because in *C* the **char** is promoted to an **int**.


##nullptr
**C++** introduces a new value to initialise pointers variables: **nullptr**. This is very useful to avoid confusion between **0** and **NULL**. NULL is simply a macro (#define NULL 0) and should be always avoided.


###Default arguments
In **C++** is possible use default values in a function. These values are supplied by the compiler when they are not specified by the programmer. This means that the arguments must be know at compile-time. As a consequence, these arguments need to be supplied in function declaration. 
Is not possible provide default arguments for all type in **C++** (e.g. you can use a defualt value for an argument passed by reference).


###void parameter list
In **C** a function declared as *void func()* is able to accept any kind of parameters. In **C++** the same function doesn't accept any parameters because it is equivalent to *void func(void)*.


###typedef
**typedef** is a keyword that comes from **C** and is still used in **C++**. However it is not required anymore when defining *struct*, *enum* or *union* because the type can be use also as type name.


##Further Information
[C++](http://en.wikipedia.org/wiki/C%2B%2B)

[C++ Annotations](http://cppannotations.sourceforge.net/) by Frank B. Brokken, Ver 9.9.0

