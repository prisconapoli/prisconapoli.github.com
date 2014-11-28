---
layout: post
category : Development
tags: [Programmers' theoretical minimum, gcc, dynamic library, static library]
---
{% include JB/setup %}

**Programmers’ theoretical minimum: how create static or dynamic library**

<!--more-->

Create a static or dynamic library isn't hard indeed.

It's enough to compile your code without a main routine and process the resulting objects (.o) files with the correct utility *ar* for **static libraries** or *ld* for **dynamic libraries**:

#####square.h
{% highlight cpp %}
double square(double);
{% endhighlight %}

#####square.c
{% highlight cpp %}
double square(double num) {
  return num*num;
}
{% endhighlight %}

As first step is necessary to product the objects files passing *-c* to **gcc** compiler:

{% highlight cpp %}
gcc -c square.c -o square.o
{% endhighlight %}

####Creating the static library
Static libraries are known as **archives** and they are created and updated using the **ar** (archive) utility.

Convention dictates that static library's name starts with **lib** and has an **.a** extension.

{% highlight cpp%}
ar rcs libsquare.a square.o
{% endhighlight %}

####Creating the shared library using ld
A dynamically linked library is created by the link editor **ld**. The conventional file extension for a dynamic library is **.so** meaning *shared object*, because every program linked against this library shares the same one copy, in contrast to static linking, in which everyone is (wastefully) given their own copy of the contents of the library.
 
{% highlight cpp%}
ld -o square.so square.o
{% endhighlight %}

####Creating the shared library using gcc
A dynamic library can also be created using **gcc**  and passing the *-shared* option, like below:
{% highlight cpp %}
gcc -shared -o square.so square.o
{% endhighlight %}


##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)

[Creating a shared and static library with the gnu compiler [gcc]](http://www.adp-gmbh.ch/cpp/gcc/create_lib.html)


