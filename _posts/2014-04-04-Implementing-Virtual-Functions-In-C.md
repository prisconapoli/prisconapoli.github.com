---
layout: post
category : lessons
tags: [virtual functions, c++, c,inheritance, polimorphism, object oriented design]
---
{% include JB/setup %}

**The first version of C++ Language written by Bjarne Stroustrup is called *C with Classes* because it first transform C++ code to C code, then compile it with a regular C compiler. The ideas behind object-oriented programming such as classes, polymorphism and inheritance, go beyond the limitations of the specific programming language and can be always applied, taking care to make the right things. In this post I'll show you how virtual functions, dynamic dispatch and inheritance can be implemented using the C Programming Language.**

<!--more-->

>Virtual functions in C++

Virtual functions are one of the most important features in C++. They make possible for writing software using  *polimorphism*, a design tecnique which is one of the five pillars of the **Object Oriented Design**.

A virtual function allows derived classes to **reuse or replace the implementation** provided by a base class. Is care of the compiler be sure that the right implementation of the member function is called each time, whenever the object in question is actually of the derived class, even if the object is accessed by a base pointer rather than a derived pointer.  This is called **dynamic dispatch**.

{% highlight cpp %}
#include <stdio.h>
class Shape
{
public:
    Shape();
    virtual ~Shape();
    virtual float area();
    float width;
    float height;
};
Shape::Shape()
{
    printf("Shape::Ctor\n");
    width = 0.0;
    height = 0.0;
}
Shape::~Shape()
{
    printf("Shape::Dctor\n");
}
float Shape::area()
{
    printf("Shape::area ");
    return 0.0;
}
class Square : public Shape
{
public:
    Square(float w, float h);
    virtual ~Square();
    virtual float area();
};
Square::Square(float w, float h) : Shape()
{
    printf("Square::Ctor\n");
    width = w;
	height = h;
}
Square::~Square()
{
    printf("Square::Dctor\n");
}
float Square::area()
{
    printf("Square::area ");
	return width * height;
}
class Triangle : public Shape
{
public:
    Triangle(float w, float h);
    virtual ~Triangle();
	virtual float area();	
};
Triangle::Triangle(float w, float h) : Shape()
{
    printf("Triangle::Ctor\n");
	width = w;
	height = h;
}
Triangle::~Triangle()
{
    printf("Triangle::Dctor\n");
}
float Triangle::area()
{
    printf("Triangle::area ");
	return width * height / 2;
}
int main()
{
    Shape* shape, square, triangle;
    shape = new Shape();
    printf("%f\n", shape->area());
    delete shape;
	
    printf("\n");
    square = new Square(3, 5);
	printf("%f\n", square->area());
    delete square;
	
    printf("\n");
    triangle = new Triangle(3, 5);
    printf("%f\n", triangle->area());
    delete triangle;
}
{% endhighlight %}

Although virtual functions make software extremely powerful, is not always a good idea mark all the member functions as "virtual". 

The firs reason is related to **software design**: a non-virtual function in the base class cannot and should not be overridden in child classes. 

The second reason is related to **performance**: virtual functions are more costly to invoke than non-virtuals. 
Indeed, non-virtual member functions are resolved at compile time (statically) by the compiler which selected the member function that will be called based on the **type of the pointer/reference to the object**. Virtual functions, in contrast, are resolved at run-time (dynamically). The member function is selected based on the **type of the object** and not the type of the pointer/reference to that object. 

This technique is called *dynamic binding*. Most C++ compilers, however, use a variant for efficiency reasons.
**For each class** that has at least one virtual function, the compiler creates a global unique table called the *virtual-table* or *v-table*. This table is basically an array of pointers to each of the virtual functions in the class.

If an object has one or more virtual functions, the compiler puts a hidden pointer in the object called a *virtual-pointer* or *v-pointer*. This v-pointer points to the *virtual-table*.

For example consider the code above. The class **Shape** has one virtual function called **area()**. There would be exactly one v-table associated with the class **Shape**, no matter how many Shape objects are defined, and the *v-pointer* of those objects would point to the same Shape's *v-table*. During a dispatch of a virtual function, the **run-time system** *follows* the object’s v-pointer to the class’s v-table, then follows the appropriate slot in the v-table to the method code.

Implement virtual functions is no costless in terms of space and time efficiency:

- space: is necessary store an extra pointer (v-pointer) for every object who have virtual members functions, plus an extra pointer for each virtual method in the v-table;

- time: call a virtual function requires two extra fetches compared to a normal function call: one to get the value of the v-pointer, a second one to get the address of the method in the v-table. None of this runtime overhead happens with non-virtual functions, since the compiler resolves them at compile-time based on the type of the pointer.

The sample above demonstrates few important things:

- inheritance: both the classes **Triangle** and **Square** inherit from class **Shape**, which means that both includes the data members of the base classes

- constructor/destructor chaining: when an object of class Square is created, that Shape's constructor is invoked as first, then followed by the Square 'scontructor. Destructors get invoked in the opposite order of the constructors

- virtual functions: the *rigth* implementaton of **area()** that will be called depend on the type of the instance *shape* points to. For example, on an instance of Square, we see that calling area invokes Shape's version, while calling triangle invokes Triangle's version


{% highlight cpp %}
Shape::Ctor
Shape::area 0.000000
Shape::Dctor

Shape::Ctor
Square::Ctor
Square::area 15.000000
Square::Dctor
Shape::Dctor

Shape::Ctor
Triangle::Ctor
Triangle::area 7.500000
Triangle::Dctor
Shape::Dctor
{% endhighlight %}


##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)

[C++ FAQ Inheritance — virtual functions](http://www.parashift.com/c++-faq/virtual-functions.html)

[Object-oriented design](http://en.wikipedia.org/wiki/Object-oriented_design)
