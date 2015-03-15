---
layout: post
category : Development
tags: [c++, 'boost::optional', boost]
image : boost/boost_logo.png
tagline: One of the most highly regarded and expertly designed C++ library projects in the world - H.Sutter and A.Alexandrescu, C++ Coding Standards


---
{% include JB/setup %}

**boost::optional: unleash the power of C++ with Boost libraries.**

<!--more-->

**Boost.Optional** class is very close the [boost::variant ]({% post_url 2015-03-02-Another-Way-To-Store-multiple-types-using-Boost %}) class but for only one type.
*boost::optional* holds an array of char, where the object of type **T** can be an **in-place** constuctor.
It has also a boolean flag to remember the state of the object (if is constructed or not). 

To use this class, just add *#include <boost/optional.hpp>* to your program. See the example below:

{% highlight cpp %}
#include <boost/optional.hpp>
#include <iostream>
#include <stdlib.h>

class lock{
    //Note: constructor is private
    explicit lock (const char * name) {
        std::cout << name << " is locked \n";
    }
    public:
    ~lock () {
        //release lock
    }

    void use() {
        std::cout << "Success!\n";
    }

    static boost::optional<lock> acquire() {
        if (rand()%2) {
            return boost::none;
        }
        return lock("MyLock");
    }
};

int main() {
    srandom(5);
    for (unsigned i = 0; i < 10; i++) {
        boost::optional<lock> t =
            lock::acquire();
        if (t) {
            t->use();
            return 0;
        } else {
            std::cout << "... trying again  \n";
        }
    }
    std::cout << "Failure \n";
    return -1;
}
{% endhighlight %}

**Boost.Optional** class does not use dinamic allocation, and it does not require a default constructor
for the underlying type. 

##Further Information

[Boost.Optional](http://www.boost.org/doc/libs/1_56_0/doc/html/optional.html)

[Advantages of using the C++ Boost Libraries](http://stackoverflow.com/questions/125580/what-are-the-advantages-of-using-the-c-boost-libraries)

[Boost C++ Application Development Cookbook](https://www.packtpub.com/application-development/boost-c-application-development-cookbook), by Antony Polukhin


