---
layout: post
category : lessons
tags: [rvalue, lvalue, rref, lref, std::move, references, template, 'c++', 'c++11']
---
{% include JB/setup %}

**On the power of the rvalues references and the different meanings of *&&* when this is used in template functions**

<!--more-->

Here we are. In this post I’ll introduce you about the power of the **rvalue references (rrefs)** and what pitfalls may arise when these latter are used as arguments in **templates functions**.
Probably you have already heard about rref. People describe them as one of the most important new features in C++11. To tell the truth, **Move Semantic** and **Perfect Forwarding** are the real coolest new features. Rrefs are simply the mechanism on which they are built. Before enter in the core of our discussion, let's take a quick look at what **lvalues** and **rvalues** are.

The first thing to keep in mind is that lvalues and rvalues are both **expressions**. We can say that an expression is an lvalue if we can take the address of its memory location via the *& operator* (if you are interested in a rigorous definition take a look at this [ACCU article](http://accu.org/index.php/journals/227)). The most simple example of lvalue that you can think is the declaration of a variable **var** of type **T**:

    T var;

For this reason lvalues are typically called **named objects** because they have, effectively, a *name*. Another example of lvalues are the traditional *references* variables, also called *"lvalues references"*. A reference is nothing but that an alias for another object. It can be defined placing an **&** after the type **T** and before the name of the variable:

{% highlight cpp %}
T& lrvar = var;
{% endhighlight %}

Above we have defined a *reference variable to var*, called **rvar**. You should remember that references need to be **always** initialised, otherwise your program doesn't compile. If you want know more about how references work, look at this interesting discussion on [stackoverflow](http://stackoverflow.com/questions/2765999/what-is-a-reference-variable-in-c). 

Anytime we cannot take of the address of an expression, we are facing with an rvalue. A typical example are the unnamed temporary objects returned by the functions or the literals. Simple! Let’s see some examples to explain better the differences:

{% highlight cpp %}

int h = 3;              //h is lvalue   
int b = 5;              //b is lvalue
int area = a * b;       //area is lvalue 

int *parea              //parea has a name so it is an lvalue
*parea = area;

h * b = 15;             //error, h*b is rvalue

std::string address = "221B Baker Street"; //"221B Baker Street" is an rvalue

int SayThirtyThree();
SayThirtyThree = 33;    //error, SayThirtyThree() is a rvalue       

int& theAnswer2LifeTheUniverseAndEverything();
theAnswer2LifeTheUniverseAndEverything() = 42;   //ok is a lvalue 

{% endhighlight %}

Now we are ready for talk about the *mythical* **rvalue references** ( I'll call it simply *rref* ). 

Rref have been introduced in C++11 to solve a very annoying issue: avoid the *unnecessary copy* of temporary objects. To understand better what I am saying, look at the code below:

{% highlight cpp %}
typedef std::vector<T> Foo;
Foo getFoo();
Foo vec;
vec = getFoo(),    
{% endhighlight %}

This seems an innocous piece of code. There is the declaration of a new type **Foo** that is simply a shortname for a vector of **T** objects, a factory method named *getFoo()* that return a **Foo** object, and a local variable **vec**. 
Let me ask you a question: *How many Foo objects have been created?*

The answer is **3**. Below the explaination:

1. a **Foo** object is created inside the createVec() function
2. a temporary object of type **Foo** is created to store the object returned by *getFoo()*
3. the third object is simple the local variable **vec** 

How you can see, this simple program is a bit inefficient due to the use of **temporary variable **. Temporary variables don't appear in your source code any you cannot see them. They are inserted automatically by the compiler in some circustamces. One of these is when functions return objects. Here, anytime *getFoo()* is called, a temporary is created (and later destroyed) to store the return value.

The cost payed for create and destroy temporary objects can have a noticeable impact on the performance of your program. And with this little example I showed you how simple instructions can hide pitfalls that lead us in lose of time or space efficiency.
It could be better if we can assign the function return value directly to **vec**, without the use of unnecessary and expensive temporary objects. How we can obtain this?

This is the kind of things that **Move Semantic** make possible to do effectively (another interesting tecnique is the [Return Value Optimization](http://en.wikipedia.org/wiki/Return_value_optimization)). This *kind of magic* is possible thanks to the rrfes, which can identify all the objects that are moveable (the rvalues described before are all example of moveable objects). But before see how the move semantic can be implemented, let me to explain briefly how define an rref. 

An rvalue reference can be defined in a similar way as an lvalue reference. Suppose **var** is a variable of generic type **T**, we can define an *rvalue reference to var* placing an **&&** after the type **T**:

{% highlight cpp %}
T&& rrvar = var;
{% endhighlight %}

An rref behaves much like the ordinary reference X&, with few exceptions. The most important is that using an rref you can bind an rvalue (a temporary object), while you cannot do the same with a lref. Below you can see how an rref for the **Foo** object is declared:

{% highlight cpp %}
T& lrfoo = getFoo();         //error, getFoo() return a temporary
T&& rrfoo = getFoo();        //ok
{% endhighlight %}

Now, let's see how move semantic can help us to avoid the creation of temporary. With Move Semantic two new special member functions called **move constructor** and **move assignment operator** are introduced in addition to the four *standard* **special member functions**:

* Default constructor
* Destructor
* Copy constructor
* Copy assignment operator
* **Move contructor** 
* **Move assignment operator**

These functions are called *special* because they need to be always defined for a class. If the user forget to define all of them or forget someone, the compiler define the remaining implicitly for you. Write a **move constructor** or a **move assignment operator** is quite easy and can be summarized in three easy steps:

1. Define the function following the standard conventions (es. use the same name of the class for contructors, return a reference to the object itself for the assignment operator, ecc.), but make sure that it takes as param an *rvalue reference* to the class
2. *Assign* all the data members from the source object to the object that is being constructed
3. Leave the source object's data members in a *valid state* (typically this means assign them a default value)

Let's look an example soon. Suppose that **Foo** is a class that handle a pointer to a generic resource *m_resource* of type **T**. For the purpose of our discussion, think that a resource as something that require a considerable effort to construct, clone, or destruct.

{% highlight cpp %}
template<typename T>
class Foo {
public:
    Foo();    //default constructor
    ~Foo();    //destructor
    Foo(const Foo& rhs);    //copy contructor
    Foo& operator=(const Foo& rhs);    //copy assignment operator
    Foo(Foo&& rhs) : m_resource(rhs.m_resource)    //move contructor, param is Foo&& rhs
    {   
        rhs.m_resource = nullptr;  
    }
    Foo& operator=(Foo&& rhs)    //move assignment operator, param is Foo&& rhs
    {   
        if (this != &rhs)
        {   
            delete[] m_resource;
            m_resource = rhs.m_resource; 
            rhs.m_resource = nullptr;
        }
        return *this;
    }
private: 
    T* m_resource;
};
{% endhighlight %}

You can see how the implementation of the new special member functions follow the simple steps introduced to implement the Move Semantic (note: the remaining four special member functions are declared but not defined). Both the functions have as parameter a non-const rref to permit the exchange of content beetween the source and the destination object (remember that  a *const* rref is syntactically correct, but make no sense). Moving objects become extremely useful when objects have separate data on the heap on when deep copy is performed. One important thing to remember is that *value movement* are **safe** only when rvalues are involved. They became **unsafe** if an lvalue is used as source because the object coutinues to exists and may be referred again in some other part of your program. 
> *Value movement* are safe only when rvalues are involved 

Now we are ready to move to a new example. Suppose we have a template function that take as parameter an rref. The question that we'll try to respond is: *what is the deduced type of T in funcTempl()?*

{% highlight cpp %}
class Foo {};    //an empty class can be used in this example
Foo createFoo() {
    return Foo();
};
template <typename T>
void funcTempl(T&&) {
};
int main() {
    Foo f1; 
    funcTempl(f1);
    funcTempl(createFoo());
    return 0;
}
{% endhighlight %}

It seems reasonable to assume that the presence of “&&” is enough to confirm that it is an rvalue reference. But in this case, some strange things happen… and to see what *really* happen with the template istantiations, try to run *g++* whit the *fdump-tree-original* option to see  the **Abstract Syntax Tree** built by the compiler:

{% highlight cpp %}
g++ -fdump-tree-original foo.cpp -o foo 
{% endhighlight %}

Compiler create a file with a name *foo.cpp.003t.original* that contains something like the content below:

{% highlight cpp linenos%}
;; Function Foo createFoo() (null)
;; enabled by -tree-original
<<cleanup_point return <retval> = TARGET_EXPR <D.1615, {}>>>;

;; Function int main() (null)
;; enabled by -tree-original
{
  struct Foo f1;
    struct Foo f1;
  <<cleanup_point <<< Unknown tree: expr_stmt
  funcTempl<Foo&> ((struct Foo &) &f1) >>>>>;
  <<cleanup_point <<< Unknown tree: expr_stmt
  funcTempl<Foo> ((struct Foo &) &TARGET_EXPR <D.1650, createFoo ()>) >>>>>;
  return <retval> = 0;
}
return <retval> = 0;

;; Function void funcTempl(T&&) [with T = Foo&] (null)
;; enabled by -tree-original

;; Function void funcTempl(T&&) [with T = Foo] (null)
;; enabled by -tree-original
{% endhighlight %}

Don't be afraid about the strange syntax and try to concentrate yourself on the line 18 an 21. These are related to the template instantiation:

{% highlight cpp%}
    18 ;; Function void funcTempl(T&&) [with T = Foo&] (null)   

    21 ;; Function void funcTempl(T&&) [with T = Foo] (null)
{% endhighlight %}

If you try to replace T inside parentesis with the type deducted (T inside square brackets), you have:

{% highlight cpp%}
    18 ;; void funcTempl(Foo& &&) 
    
    21 ;; void funcTempl(Foo&&)
{% endhighlight %}

At this point, for the first function a *kind of magic* called *reference collapsing* is made (no such things as "reference to reference" are admitted by the syntax of C++), and at finally we have:

{% highlight cpp%}
    18 ;; void funcTempl(Foo&) 
    
    21 ;; void funcTempl(Foo&&)
{% endhighlight %}

Now is quite obvious what is happened. T’s deduced type isn't an rref fixed by the template but depends from what is passed to *funcTempl()* as param:

* if an lvalue is passed (f1) => T is an lvalue reference (T&)
* if an rvalue is passed (return value of createFoo()) => T is a non-reference (T)

The essence of the issue is that **&&** in a type declaration sometimes means rvalue reference, but sometimes it means either rvalue reference or lvalue reference. As such, some occurrences of **&&** in source code may actually have the meaning of *&*, i.e., have the syntactic appearance of an rvalue reference (&&), but the meaning of an lvalue reference (&). This *very special* kind of rrefs are called [Universal References (URefs)](http://www.artima.com/shop/overview_of_the_new_cpp) by *Scott Meyers*, a guru in C++ community. Scott summarizes how to identify an uref in few words:

>If a variable or parameter is declared to have type T&& for some deduced type T, that variable or parameter is a universal reference

Urefs must be initialized like all references, and is the kind of the initializer (lvalue or rvalue) that determines whether it represents an lref or an rref:

* If the initialize expression is an lvalue, the uref becomes an lvalue reference
* If the initialize expression is an rvalue, the uref  becomes an rvalue reference.

After this brief digression on the Universal Reference, let's move back to our example. How is possible that if we call the template function *funcTempl(T&&)* passing *f1* as argument, the istantiation is a function that get an *lref (T&)* as parameter and not an *rref (T&&)*?

     template<typename T>
     void funcTempl(Foo&)     ⇒    void funcTempl(Foo&)

This *mistery* can be easily revealed thanks to the **Reference Collapsing** and its rules introduced by C++11:

* **T& &    ⇒  T&**
* **T&& &   ⇒  T&**
* **T& &&   ⇒  T&**
* **T&& &&   ⇒  T&&**

How you can see, all the combinations involving an lref (T&) collapse into an lref. An rref (T&&) is obtained only when two rrefs are involved.

> Check always the reality of the situation!

Now, let's go back to our example and find a way to pass *f1* to *funcTempl()* in a proper way. In other words, we need something to turn lvalues into rvalues. How we can reach our goal?

Luckily, C++11 introduce a new function in **std library** that comes to our rescue. This function is called  [std::move](http://it.cppreference.com/w/cpp/utility/move), and its goal is to turn its argument into an rvalue. Nothing else is done.
 
Let's try to change our code for use *std::move*:
{% highlight cpp %}
#include <utility>
class Foo {};
Foo createFoo() {
    return Foo();
};
template <typename T>
void funcTempl(T&&) {
};
int main() {
    Foo f1; 
    funcTempl(std::move(f1));
    funcTempl(createFoo());
    return 0;
}
{% endhighlight %}

If we run **g++** with the *fdump-tree-original* option, we see (line 25) that T's deduced type is is a non-reference as expected. Great!

{% highlight cpp linenos %}
;; Function Foo createFoo() (null)
;; enabled by -tree-original
<<cleanup_point return <retval> = TARGET_EXPR <D.4351, {}>>>;

;; Function constexpr typename std::remove_reference< <template-parameter-1-1> >::type&& std::move(_Tp&&) 
   [with _Tp = Foo&; typename std::remove_reference< <template-parameter-1-1> >::type = Foo] (null)
;; enabled by -tree-original
<<< Unknown tree: must_not_throw_expr
  return <retval> = (struct type &) (struct type *) NON_LVALUE_EXPR <(struct type &) __t>
   >>>;

;; Function int main() (null)
;; enabled by -tree-original
{
  struct Foo f1;
    struct Foo f1;
  <<cleanup_point <<< Unknown tree: expr_stmt
  funcTempl<Foo> ((struct Foo &) (struct type *) std::move<Foo&> ((struct Foo &) &f1)) >>>>>;
  <<cleanup_point <<< Unknown tree: expr_stmt
  funcTempl<Foo> ((struct Foo &) &TARGET_EXPR <D.4393, createFoo ()>) >>>>>;
  return <retval> = 0;
}
return <retval> = 0;

;; Function void funcTempl(T&&) [with T = Foo] (null)
;; enabled by -tree-original

{% endhighlight %}

In this post I discussed briefly about the concepts of lvalues references and rvalue references, the useful of Move Semantics for increasing the performance of your programs and what pitfalls may arise when rvalue references  are used with templates functions. My suggestion is to further read more articles on these arguments (below some good links). 

Finally, If you liked this post, please leaves a comment or share it.

##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)

[A Brief Introduction to Rvalue References](http://www.artima.com/cppsource/rvalue.html)

[C++ Rvalue References Explained](http://thbecker.net/articles/rvalue_references/section_01.html)

[Want Speed? Pass by Value](http://cpp-next.com/archive/2009/08/want-speed-pass-by-value/)

[Universal References in C++11](http://isocpp.org/blog/2012/11/universal-references-in-c11-scott-meyers)
