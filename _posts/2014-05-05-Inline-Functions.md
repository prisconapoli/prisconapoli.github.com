---
layout: post
category : misc
tags: [Programmers' theoretical minimum, Inline functions, c++]
---
{% include JB/setup %}

**Programmers’ theoretical minimum: rule of thumbs for defining inline functions in C++**

<!--more-->

In C++ there is a special keyword called **inline** that allow you to declare a function that is expanded inline rather than called through the usual function call mechanism.

The main reason for making a virtual function inline is to generate more efficient object code. However, overuse of inlining can actually make programs slower. Not all functions are always inlined, even if they are declared as such. A tipical example are recursive functions which are not normally inlined. 

Below is reported a **rule of tumbs** for defining inline functions:

* they are small (e.g. 10 lines of code or less)
* they don't contains loops or switch statements
* they are not recursive


##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)
[Google C++ Style Guide](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml), Revision 3.274


