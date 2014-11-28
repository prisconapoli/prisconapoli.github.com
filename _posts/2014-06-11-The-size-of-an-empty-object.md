---
layout: post
category : Development
tags: [Programmers' theoretical minimum, C++, class, empty object]
image : development/development.png
tagline: Empty objects don't exist.
---
{% include JB/setup %}

**Programmers’ theoretical minimum: the size of an empty object**

<!--more-->

{% highlight cpp %}
class Empty { };
int main()
{
    Empty e;
    std::cout << "The size of e is " << sizeof(e);
}
{% endhighlight %}

Running this little program on my Macbook, I receive this output:

{% highlight cpp %}
Running…
The size of e is 1
Debugger stopped.
Program exited with status value:0.
{% endhighlight %}

In C++, **empty objects don't exist**. Indeed, C++ allocate for the objects **at minimum** 1 bytes.

This is due to the fact that each object needs have a different address in memory.
 
##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)


