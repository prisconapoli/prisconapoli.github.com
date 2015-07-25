---
layout: post
category : Development
tags: [c++,  c, template, metaprogramming]
image : zen_programming/singleton.jpg
tagline: There are only patterns, patterns on top of patterns, patterns that affect other patterns. Patterns hidden by patterns. Patterns within patterns. -  Chuck Palahniuk

---
{% include JB/setup %}

**Code the Singleton correctly**
<!--more-->

**Singleton** is surely one of the most famous design pattern, hugely  mentioned in programming books, forums and blogs.  Its particularity lies in its simple and concise description: *make sure there is only one instance of a class, and provide a global access point to it*.
Despite at first look the Singleton pattern sounds pretty easy to implement, the bad news is that it hides many pitfalls. Singleton is indeed very special: so easy to describe, particularly hard to to implement correctly.
In this post, I'll go through the main implementations, the implications of each design, and the main pitfalls.
I'll use metaprogramming, an awesome and powerfull tecnique to design a template class that can be used to add Singleton functionality to every other class.

No matter what programming language you're using, a respectable implementation need to go across three main aspects

1. **Creating**

2. **Lifetime**

3. **Multi-Threading**


####Creation
Let’s start reflecting again on Singleton’s description: **ensure the presence of a single instance and provide a **unique global access point**. The last statement, in particular, has a subtle implication: the singleton owns itself, ie it manages its own life: creation and destruction.

C++ provide an adequate support to ensure the uniqueness of the access point. In particular, it is enough to make private the declarations of constructor, copy constructor and copy assignment operator. It worth to note that only declarations are enough, it is not necessary define the functions. In this way, the compiler will never define a default versions for us. The advantage of this approach, is that the compiler will raise an error message whenever the singleton is used improperly, ie an attempt to instantiate it or make a copy.

An initial attempt for implementing Singleton is the so called monolithic singleton. It assumes that all data and functions are static. However, although quite simple, the monolithic pattern can be applied in a limited number of cases, cause it has few disadvantages:

- no virtual functions
- no access points for creation or cleanup operations.

{% highlight cpp %}
//Solution 1: monolithic
template <class T>
class Singleton {
public:
    static T& Instance() { return instance_; }
private:
    static T instance_;
    Singleton();
    Singleton(const Singleton&);
    Singleton& operator=(const Singleton&);
};

template <class T>
T Singleton<T>::instance_;
{% endhighlight %}

A second solution makes use of a **pointer and dynamic allocation**. The singleton is created on-demand, when the static method **Instance** is called the first time. In this case, is necessary take in account for the memory release defining a static method function **Release**.


{% highlight cpp %}
//Solution 2: pointer + dinamyc allocation 
template <class T>
class Singleton {
public:
    static T& Instance() {        
        if (!pInstance_)
            pInstance_ = new T;
        return *pInstance_;
    }
    static void Release() {
        if (pInstance_)
            delete pInstance_;
        pInstance_ = NULL;
    }
private:
    static T* pInstance_;
    Singleton();
    Singleton(const Singleton&);
    Singleton& operator=(const Singleton&);
};

template <class T>
T* Singleton<T>::pInstance_ = NULL;
{% endhighlight %}


The third solution makes use of a **static variable** defined inside **Instance**. Also in this case, the singleton object is created on-demand, ie when **Instance** is called for the first time. Moreover, it does not allocate memory on the heap. This solution can be adopted when objects are relatively small, ie. up to 32 bytes. Memory allocation has always a cost and for small objects standard allocation function can be very inefficent. 

{% highlight cpp %}
//Solution 3: static variable
template <class T>
class Singleton {
public:
    static T& Instance() {        
        static T instance_;
        return instance_;
    }
private:
    Singleton();
    Singleton(const Singleton&);
    Singleton& operator=(const Singleton&);
};
{% endhighlight %}

All examples provide a static public method **Instance** that return a T&. Is not unusual to find some implementation in books or around the web,  where a pointer T* is returned. I don't like this kind of implementations cause they are a violation of information hiding. Exposing the private member T* is always dangerous. A client could call **delete** on this pointer and crash the program. For safety reason, the best solution is return a reference T&.

What about returning a *constant reference*? Well, in this situation, the only way is to define another function, ie *CInstance*, to return a const T&:

{% highlight cpp %}
//Solution 2: pointer + dinamyc allocation 
template <class T>
class Singleton {
public:
    ...
    static const T& CInstance() {        
        return const_cast<const T&>(Instance());
    }
    ...
};

//Solution 3: static variable
template <class T>
class Singleton {
public:
    ...
    static const T& CInstance() {        
        return const_cast<const T&>(Instance());
    }
    ....
};
{% endhighlight %}



### Lifetime
The **Instance** function is quite interesting; it defines the *creation moment*, but leaves a question open: the *destruction moment*.

What is the best moment for a singleton to be destroyed? This is not a trivial problem, indeed we can say that this choice is the most important for a correct implementation of this pattern. The decision should be taken carefully because the singleton may acquire resources that would be lost if not properly handled.

Let’s take a look at second and third implementations, which are indeed the most used in practice. The true difference lies in the destruction of the object, as in the first case we have to call delete, while in the second case the memory is freed automatically thanks to compiler. For this last case, in particular, the static object T is initialized when the control flow reaches its definition inside **Instance()**, and the object T is guaranteed to be destroyed.
How this can happen? Well, we know that compilers make a lot of stuffs  as expanding macros, loop unrolling, instruction reordering ecc. With static objects, a compiler generates extra code in such a way that the object can be destroyed when the program exits. This 'kind of magic' consists in putting a call to a Standard C library function [atexit](http://man7.org/linux/man-pages/man3/atexit.3.html), that allows to register a function that will be called automatically when the program exits.

{% highlight cpp %}
//Solution 3: static variable
template <class T>
class Singleton {
public:
    // Functions/variable with __ as prefix are generated by the compiler
    extern void __build(void * buffer);
    extern void __destroy();
    ...
    static const T& Instance() {
        if (!__init)
        {
            __build(__buffer);
            atextit(__destroy);
            __init = true;
        }
        return *reinterpret_cast<T*>(__buffer);
    }
private:
    Singleton();
    Singleton(const Singleton&);
    Singleton& operator=(const Singleton&);
    static bool __init;
    static char __buffer[sizeof(T)];    
};
template <class T>
bool Singleton<T>::__init = false;

template <class T>
char Singleton<T>::__buffer[sizeof(T)];

{% endhighlight %}

**atexit** works using a private stack kept by the **C Runtime library**. When it is called, **atexit** performs a push on this stack, while at exit time it makes a pop and calls the corresponding function, according to a LIFO policy.
For static objects,  destructors are called when function **main()** exits or when the Standard C library function **exit()** is explicitly called. In most implementations, **main()** just calls **exit()** when it terminates. Static object destructors are not called if program terminates using the Standard C library function **abort()**.


Singletons are largely used for logging, configuration and to manage unique physical resource. In some situation, they need to be used carefully to avoid memory leaks, crashes, and to spend many nights debugging the code.

Use a static member implies a simplification of the implementation, and leaves to the compiler the tasks of constructing the instance and release the corresponding memory. It seems a very good compromise, However, this solution has a subtle issue. Consider the example below:

{% highlight cpp lineno %}
#include <iostream>
#include <sstream>
#include <atomic>
#include <thread>  

template <class T>
class Singleton {
    // One of the implementation above
...
};
class Log {
public:
    Log();
    ~Log();
    void log(const std::string& line);
    std::string getLog();
private:
    std::stringstream ss;
};
class Printer{
public:    
    Printer();
    ~Printer(); 
    bool print(const std::string& doc);
private:
    void addJob(const std::string& doc);
    std::atomic_flag lock;
};
Log::Log() : ss() {
    std::cout << "Log ctor" << std::endl;
} 
Log::~Log() { 
    std::cout << "Log dctor" << std::endl;
}
std::string Log::getLog() {
    return ss.str();
}
void Log::log(const std::string& line) {
    ss << line<< std::endl;
}
Printer::Printer() : lock(ATOMIC_FLAG_INIT) {
    std::cout << "Printer ctor" << std::endl;
}
Printer::~Printer() { 
    if (!lock.test_and_set()) //Fails to lock, so a print is in progress
        Singleton<Log>::Instance().log("Print interrupted. The printer is shutting down\n");
    std::cout << "Printer dtor" << std::endl;
}
void addJob(const std::string& doc) {
    // some actions, ie use driver to perform the check amount of colors, the paper, run the print
    lock.clear();
}
bool Printer::print(const std::string& doc) {
    if (lock.test_and_set())
    {
        std::cout << "Printing:" << std::endl;
        Singleton<Log>::Instance().log("Printing\n");
        //Start a new thread to print the document
        //when the thread completes, it will call lock.clear()
        std::thread start(addJob, doc);
        return true;
    }
    return false;
}
int main()
{
    if (!Singleton<Printer>::Instance().print("Test"))
        Singleton<Log>::Instance().log("something wrong");   
}
{% endhighlight %}

This program just uses two singletons to manage a Printer and a Log. Every action is logged thanks to a public member *log*.
Below the output:
{% highlight bash lineno %}
2L:singleton prisconapoli$ ./singleton
Printer ctor
Printing:Test
Log ctor
Log dctor
Printer dtor <--Oops: Log is no more present
{% endhighlight %}

There is a subtle issue into **Printer::~Printer()**. If the print is still in progress, the function try to use Singleton<Log> to log a message. However, the instance of **Log** has been deleted!


This is the so-called **dead reference problem**. There could be different lifetime among singletons or singletons and traditional objects. If a singleton is used after it has been destroyed, we may encounter memory leaks, crashes etc, etc.


It follows that a correct implementation of the singleton must be able to determine if it is destroyed or not. And if necessary, raise an exception when something goes wrong. If Solution 2 is used, is enough to add a boolean flag **destroyed** that can be checked every time *Instance* is called and is set to true when **Release** is called. We can use this flag to raise an exception.

{% highlight cpp %}
//Solution 2: pointer + dinamyc allocation + dead referencer
template <class T>
class Singleton {
public:
    static T& Instance() {
        if (destroyed_)
            throw std::runtime_error("Dead Reference Detected");       
        if (!pInstance_)
            pInstance_ = new T;
        return *pInstance_;
    }
    static void Release() {
        if (pInstance_)
            delete pInstance_;
        pInstance_ = NULL;
        destroyed_ = true;
    }
private:
    static T* pInstance_;
    static bool destroyed; 
    Singleton()
    Singleton(const Singleton&);
    Singleton& operator=(const Singleton&);
};

template <class T>
T* Singleton<T>::pInstance_ = NULL;
template <class T>
bool Singleton<T>::destroyed = false;
{% endhighlight %}

However, not always is desiderable to raise an exception. Indeed, no matter if the Singleton has been destroyed, we need it so we want to recreate it. This approach is the so called **Phoenix Singleton Pattern**. In a nutshell, the singleton is recreated after it has been regularly destroyed.

{% highlight cpp %}
//Solution 2: pointer + dinamyc allocation + phoenix singleton
template <class T>
class Singleton {
public:
    static T& Instance() { 
        if (!pInstance_ || destroyed_)
        {
            pInstance_ = new T;
            destroyed_ = false;
        }
        return *pInstance_;
    }
    static void Release() {
        if (pInstance_)
            delete pInstance_;
        pInstance_ = NULL;
        destroyed_ = true;
    }
private:
    static T* pInstance_;
    static bool destroyed_;
    Singleton();
    Singleton(const Singleton&);
    Singleton& operator=(const Singleton&);
};

template <class T>
T* Singleton<T>::pInstance_ = NULL;
template <class T>
bool Singleton<T>::destroyed = false;
{% endhighlight %}


If a static object is used, ie Solution 3, the new object can be reconstructed in the same shell of the previous one using the **new placement operator**. Obviously, in this situation it will be necessary manually insert a call to *atexit* to register

{% highlight cpp %}
//Solution 3: static variable + phoenix pattern
template <class T>
class Singleton {
public:

    static void create() {        
        static T instance_;
        pinstance_ = &instance_;
    }

    static T& Instance() {        
        if (!pInstance_) {
            if (destroyed_)
                OnDeadReference();
            else
                Create();
        }
        return *pInstance_;
    }
    ~Singleton() {
        pInstance_ = NULL;
        destroyed = true;  
    }

    static void Release() {
        pInstance_->~Singleton();
    }

    static void OnDeadReference() {
        Create();
        // now pInstance_ points to the shell of the destroyed object
        new(pInstance_) Singleton();
        atexit(Release);
        destroyed_ = false;
    }
private:
    Singleton();
    Singleton(const Singleton&);
    Singleton& operator=(const Singleton&);
    static T* pInstance_;
    static bool destroyed;   
};

template <class T>
T* Singleton<T>::pInstance_ = NULL;
template <class T>
bool Singleton<T>::destroyed = false;
{% endhighlight %}

The **Phoenix Singleton** solves some of the problems but has the disadvantage of altering the lifetime of a singleton. In particular, if the singleton handle a state, the situation may be complicated because is necessary preserve the state. This longevity problem is not limited to singletons but is much more general.


#Thread safe
A successful singleton implementation must be thread safe. The most common approaches are the use of a **mutex lock** and the **double-checked locking** pattern. Class Lock can handle mutex. The mutex is locked in Lock's ctor and unlocked in Lock's dtor. While mutex_ is locked, other threads cannot lock the same mutex and are forced to wait. 

{% highlight cpp %}
//Lock + Mutex
static T& Instance() {
    Lock guard(mutex_);       
    if (!pInstance_)
        pInstance_ = new T;
    return *pInstance_;
}
...
static Mutex mutex_;
{% endhighlight %}

The solution above works but lacks of efficiency because every call to *Instance* locks the object. However, the race condition can appear only when the object need to be constructed. It worth to note that locking operations are quite expensive and should be limited as much as possible. In this situation, the double-checked locking pattern helps. Its mechanism is very simple: check the condition, enter the synchronization code, and check the condition again to be sure that the object has not been initialized by some other thread.

{% highlight cpp %}
//Double-checked locking
static T& Instance() {      
    if (!pInstance_) {
        Lock guard(mutex_);
        if (!pInstance_) 
            pInstance_ = new T;
       }
    return *pInstance_;
}
...
static Mutex mutex_;
volatile static T* pInstance_; //pInstance_ is volatile
{% endhighlight %}

Double-checked locking pattern is very efficient but has some weaks too. In particular, in symmetric multiprocessor environment, it could not works correctly. This is due the presence of writing optimization, ie variable are write in memory in burst rather than one by one. As a consequence, different processors can see an old value for pInstance_, because it has not been written in memory.
To solve this issue, is enough mark pInstance_ as *volatile*, so not kind of optimization is used.

####Summary
In this post we've seen that Singleton is a highly controversial pattern. Some people refer to it as a kind of *glorified global variable*. Despite exist several ways to implement singletons, each of them has advantages and disadvantages. In C++ it's quite easy ensure only one instance and a single global access point (in Java is not so easy because static objects exist per class-loader and not for JVM). More complicated is to handle life cycle and the destruction moment, because these aspects are specific for each application.
From a software engineering perspective, the important thing to keep always in mind during designing, is that using singleton introduce global state into a program. Anyone can access it at anytime and everywhere (scope is ignored).
Have a global state can be problematic in many situations. A program could be more difficult to test, because global state hides internal dependencies, making hard refactoring, adding new features and code maintenance.

##Further Information

[Singleton Pattern](https://en.wikipedia.org/wiki/Singleton_pattern), Wikipedia.org

[Modern C++ Design: Generic Programming and Design Patterns Applied](http://www.amazon.com/Modern-Design-Generic-Programming-Patterns/dp/0201704315), by Andrei Alexandrescu

[atexit](http://man7.org/linux/man-pages/man3/atexit.3.html), Linux Programmer's Manual


