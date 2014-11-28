---
layout: post
category : Development
tags: [Programmers' theoretical minimum, structs, c, c++]
---
{% include JB/setup %}

**Programmers’ theoretical minimum: struct**

<!--more-->

In C and C++ there is a special keyword called **struct** that allow you to declare a bunch of data items grouped togheter.

Define a struct is pretty easy. It's enough add the **struct** keyword before a block (delimited by curly braces), optionally followeb by a name (e.g. my_struct). Is also possible add variable names after the struct definition. This means we are declaring such variables of this struct type, for example:

{% highlight cpp %}

struct my_struct{
item_1
item_2
. . . 
item_n
} variable_1, variable_1;

{% endhighlight %}

The items in a struct can be vary: data declarations, individual data items, arrays, other structs, pointers, and so on. 

**Structs** are very similar to **classes** in C++. The main difference is that in a **struct** all members (data   an functions) are **public** by default, while for a class all members are **private** by default [1](http://stackoverflow.com/questions/92859/what-are-the-differences-between-struct-and-class-in-c).

One interesting thing that you can do with a struct, is transform a generic type to be used as a first-class type. For instance, look at the code below:

{% highlight cpp linenos %}
/* array inside a struct */ 
struct my_array { int a[10]; };
{% endhighlight %}

You can now copy the entire array with an assignment statement, pass it to a function by value, and make it the return type of a function. Obviously it's not very efficient to put an array inside a struct, but this depends by yours designing skills of good software.


##Further Information

[Expert C Programming: Deep C Secrets](http://www.amazon.co.uk/gp/search?index=books&linkCode=qs&keywords=9780131774292) by Peter van der Linden


