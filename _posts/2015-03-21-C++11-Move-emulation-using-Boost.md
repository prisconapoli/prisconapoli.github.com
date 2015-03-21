---
layout: post
category : Development
tags: [c++, 'Move', boost, rvalue]
image : boost/boost_logo.png
tagline: One of the most highly regarded and expertly designed C++ library projects in the world - H.Sutter and A.Alexandrescu, C++ Coding Standards


---
{% include JB/setup %}

**Learn how to emulate C++11 move semantics in C++03 compilers using Boost.Move.**

<!--more-->

**Move Semantic** has been introduced in C++11 to solve a very annoying issue: avoid the *unnecessary copy* of temporary objects. To understand better what I am saying, take a quick look at these few lines below:

{% highlight cpp %}
typedef std::vector<T> Foo;
Foo getFoo();
Foo vec;
vec = getFoo(),    
{% endhighlight %}

This chunk of code looks pretty easy. There is the declaration of a new type **Foo** that is simply a shortname for a vector of  generic type **T**, a factory method named *getFoo()* that return a **Foo** object, and a local variable **vec**.

Now, let me ask you a question: *how many **Foo** objects have been created?*

The answer is **3**. Below the explaination:

1. an object is created inside the getFoo() function

2. a temporary object is created to store the object returned by *getFoo()*

3. the third object is simple the local variable **vec** 

If the cost payed to create and destroy a temporary objects **Foo** is expensive, we could have a noticeable impact on the performance. Generally, if a function returns a very expensive object, it could be nice to assign the return value directly to a our local variable, without the use of unnecessary and expensive temporary objects. 
The issue here is that we have no countrol over temporary object. Temporary variables don't appear in the source code and we cannot see them because they are inserted automatically by the compiler in some circustamces (e.g. when functions return objects).

If you are using a compiler which supports C++11, the use of **Move Semantics** is the natural way to solve this kind of issues. This feature is fundamentally based on a simple idea: is allowed to modify temporary objects **stealing** resources from them. In other words, move is a potentially **destructive copy**. Technically speaking, the mechanism is implemented thanks to *rvalue reverences* (rref),  which are used to identify a *moveable* object. You can get more details about this tecnique reading [What the code say]({% post_url 2014-02-08-what-the-code-says %}).

In C++03 there are not nor **rref** nor **move semantics**. Fortunally, with **Boost.Move** library is still possible to write some portable code that emulates move semantics.

To use this feature, just add *#include <boost/move/move.hpp>* to your program. Then, follow 4 steps:

1. Put the following macro in the private section: BOOST_COPYABLE_AND_MOVABLE(classname)

2. Leave copy constructor as is.

3. Write a copy assignment taking the parameter as BOOST_COPY_ASSIGN_REF(classname)

4. Write a move constructor and a move assignment taking the parameter as BOOST_RV_REF(classname)

{% highlight cpp %}
#include <boost/swap.hpp>
#include <boost/move/move.hpp>
#include <string>
#include <iostream>

namespace other {
    //A very simple class which has a fast/cheap default ctor
    class fastclass{};
};

struct myclass {
        bool is_female;
        std::string name;
        other::fastclass fc;

        void swap(myclass& rhs) {
                std::swap(is_female, rhs.is_female);
                std::swap(name, rhs.name);
                boost::swap(fc, rhs.fc);

        }

        myclass() {
            // call ctors if required
        }

        ~myclass(){
            // call dtors if required
        }

        //copy constructior
        myclass(const myclass& mc)
                : is_female(mc.is_female)
                , name(mc.name)
                , fc(mc.fc) {
        }

        //move constructor
        myclass(BOOST_RV_REF(myclass) mc) {
            swap(mc);
        }

        // copy assignment
        myclass& operator=(BOOST_COPY_ASSIGN_REF(myclass) mc) {
            if (this != &mc) {
                myclass tmp(mc);
                swap(tmp);
            }
            return *this;
        }

        //move assignment
        myclass& operator=(BOOST_RV_REF(myclass) mc) {
            if (this != &mc) {
                swap(mc);
                myclass tmp(mc);
                tmp.swap(mc);
            }
            return *this;
        }

        private:
            BOOST_COPYABLE_AND_MOVABLE(myclass);
};

int main()
{
    myclass alice;
    alice.is_female = true;
    alice.name = "Alice";
    std::cout << alice.name << " is " << (alice.is_female ? "female": "male");
    std::cout << std::endl;

    myclass laura(boost::move(alice));
    laura.name = "Laura";
    std::cout << laura.name << " is " << (laura.is_female ? "female": "male");
    std::cout << std::endl;
}

{% endhighlight %}

Program output:

{% highlight bash %}
2L:boost-move prisconapoli$ ./move
Alice is female
Laura is female
{% endhighlight %}

The [Boost.Move](http://www.boost.org/doc/libs/1_57_0/doc/html/move.html) library is implemented in a very efficient way. All functions never copy passed values, nor call any dynamic memory allocations or virtual functions.
Moreover, if a C++11 compiler is used, all the macros for **rvalues emulation** are expanded to C++11-specific features, while on C++03 compilers **rvalues** are emulated using specific datatypes.


##Further Information

[Boost.Move](http://www.boost.org/doc/libs/1_57_0/doc/html/move.html)

[A Brief Introduction to Rvalue References](http://www.artima.com/cppsource/rvalue.html)

[C++ Rvalue References Explained](http://thbecker.net/articles/rvalue_references/section_01.html)

[Want Speed? Pass by Value](http://cpp-next.com/archive/2009/08/want-speed-pass-by-value/)

[Advantages of using the C++ Boost Libraries](http://stackoverflow.com/questions/125580/what-are-the-advantages-of-using-the-c-boost-libraries)

[Boost C++ Application Development Cookbook](https://www.packtpub.com/application-development/boost-c-application-development-cookbook), by Antony Polukhin


