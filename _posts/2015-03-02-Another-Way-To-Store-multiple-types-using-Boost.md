---
layout: post
category : Development
tags: [c++, 'boost::variant', boost]
image : boost/boost_logo.png
tagline: One of the most highly regarded and expertly designed C++ library projects in the world - H.Sutter and A.Alexandrescu, C++ Coding Standards


---
{% include JB/setup %}

**boost::variant: unleash the power of C++ with Boost libraries.**

<!--more-->

This is the second part of [Storing Multiple Types Using Boost ]({% post_url 2015-03-01-Storing-multiple-types-using-Boost %}). In the previous post I introduced **boost::any** class and how to use it to store a single value of any type.

We have seen that it is very flexible and simple to use, and why in some circumstances it cannot be used for performance reasons. Indeed, it requires to work dynamic memory allocation and  **runtime type information (RTTI)** enabled.

The Boost.Variant library is the rigth alternative to use in these situations. This class can store any of the types specified at compile time; it also manages in-place construction/destruction and doesn't even require the C++11 standard.

To use this class, just add *#include <boost/variant.hpp>* to your program. See the example below:

{% highlight cpp %}
#include <boost/variant.hpp>
#include <iostream>
#include <vector>
#include <string>
int main() {
     typedef boost::variant<int, const char*, std::string> some_values;
     some_values.push_back(10);
     const char* c_str = "a string ";
     some_values.push_back(c_str);
     some_values.push_back(std::string("Hello, "));
     std::string& s =
         boost::get<std::string>(values.back());
     s += "World!\n";
     std::cout << s;
     return 0;
}
{% endhighlight %}

To get a value from a boost::variant<T> variable, just use boost::get<N>() with one of the following approaches:

{% highlight cpp %}
boost::variant<int, std::string> val(std::string("value"));

//If actual value in variable is not a std::string, it throws a boost::bad_get exception
std::string s1 = boost::get<std::string>(val);

//If actual value in variable is not a std::string, the return value is NULL pointer
std::string* s2 = boost::get<std::string>(&val);
{% endhighlight %}

**boost::variant** class holds an array of characters and stores values in that array.
Array size is determined at compile time using *sizeof()* and functions to get alignment.
It is extremely fast because it does not allocate memory in a heap and does not require **RTTI** enabled. 

##Further Information

[Boost.Variant](http://www.boost.org/doc/libs/1_56_0/doc/html/variant.html)

[Advantages of using the C++ Boost Libraries](http://stackoverflow.com/questions/125580/what-are-the-advantages-of-using-the-c-boost-libraries)

[Boost C++ Application Development Cookbook](https://www.packtpub.com/application-development/boost-c-application-development-cookbook), by Antony Polukhin


