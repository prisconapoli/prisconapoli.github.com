---
layout: post
category : misc
tags: [Programmers' theoretical minimum, Application Binary Interface, linux]
---
{% include JB/setup %}

**Programmers’ theoretical minimum: Application Binary Interface**

<!--more-->

Dynamic linking is the modern approach to link libraries at runtime. It has two main advantages:

* smaller executable size
* decouple programs from the particular library versions they use 

The concept of **Application Binary Interface**, or simply ABI, is very similar to the concept of **Application Program Interface(API). It simly means that the operating system provides an interface to programs to access services. Programs can call the services promised by this interface and not worry about how they are provided or how the underlying implementated. Moreover,  this interface is guaranteed to be stable over time and successive release of the operating system.

This approach is called **Application Binary Interface** because this is an interface between application programs and the services provided by **library binary executables**.

##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)

[Stackoverflow: What is Application Binary Interface (ABI)?](http://stackoverflow.com/questions/2171177/what-is-application-binary-interface-abi)


