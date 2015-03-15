---
layout: post
category : Development
tags: [c++, 'boost::any', boost]
image : boost/boost_logo.png
tagline: One of the most highly regarded and expertly designed C++ library projects in the world - H.Sutter and A.Alexandrescu, C++ Coding Standards


---
{% include JB/setup %}

**boost::any: unleash the power of C++ with Boost libraries.**

<!--more-->

The **boost::any** class is a generic container for a single value.
It is based on the concept of *discriminated types*, which means it can contain values of different types but do not attempt any conversion between them (e.g. 10 is held strictly as an int and is not implicitly convertible either to "10" or to 10.0).

The **indifference to interpretation** and the **awareness of different types** make boost:any a **safe generic containers of single values**, with no scope for surprises from ambiguous conversions.

To use this class, just add *#include <boost/any.hpp>* to your program. See the example below:

{% highlight cpp %}
#include <boost/any.hpp>
#include <iostream>
#include <vector>
#include <string>
int main() {
     std::vector<boost::any> some_values;
     some_values.push_back(10);
     const char* c_str = "a string ";
     some_values.push_back(c_str);
     some_values.push_back(std::string("Hello, "));
     std::string& s =
        boost::any_cast<std::string&>(some_values.back());
     s += "World!\n";
     std::cout << s;
     return 0;
}
{% endhighlight %}

To get a value from a boost::any variable, just use **boost::any_cast<**T**>**() with one of the following approaches:

{% highlight cpp %}
boost::any val(std::string("value"));

//If actual value in variable is not a std::string, it throws a boost::bad_any_cast exception
std::string s1 = boost::any_cast<std::string>(val);

//If actual value in variable is not a std::string, the return value is NULL pointer
std::string* s2 = boost::any_cast<std::string>(&val);
{% endhighlight %}

**Boost.Any** is based on **type erasure** technique. On assignment of some variable of type T, **Boost.Any** constructs a type (e.g. **holder<**T**>**) to store a value of the specified type **T**, and is derived from some internal base-type placeholder.

The placeholder has virtual functions for getting *std::type_info* of a stored type and for cloning a stored type. When **any_cast<**T**>()** is used, *boost::any* checks that *std::type_info* of a stored value is equal to *typeid(T)* (the overloaded placeholder's function is used for getting *std::type_info*).

Unfortunately, *boost::any* requires dynamic memory allocation in copy constructor and copy assignment operators and cannot be used with **runtime type information (RTTI)** disabled.
If you are keen on performance, see the [boost::variant ]({% post_url 2015-03-02-Another-Way-To-Store-multiple-types-using-Boost %}) which has not these limitations.

##Further Information

[Boost.Any](http://www.boost.org/doc/libs/1_56_0/doc/html/any.html)

[Advantages of using the C++ Boost Libraries](http://stackoverflow.com/questions/125580/what-are-the-advantages-of-using-the-c-boost-libraries)

[Boost C++ Application Development Cookbook](https://www.packtpub.com/application-development/boost-c-application-development-cookbook), by Antony Polukhin


