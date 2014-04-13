---
layout: post
category : lessons
tags: [virtual functions, c++, c,inheritance, polimorphism, object oriented design]
---
{% include JB/setup %}

**Classes, polymorphism and inheritance using the C Programming Language.**

<!--more-->

>Virtual functions in C++

The first version of C++ Language written by Bjarne Stroustrup is called *C with Classes* because it first transform C++ code to C code, then compile it with a regular C compiler. The ideas behind object-oriented programming such as **classes**, **polymorphism** and **inheritance**, however, *go beyond the limitations of the specific programming language* and can be always applied taking care to make the right things. In this post I'll show you how virtual functions, dynamic dispatch and inheritance can be implemented using the C Programming Language.

Virtual functions are one of the most important features in C++. They make possible for writing software using  *polimorphism*, a design tecnique which is one of the five pillars of the **Object Oriented Design**.

A virtual function allows derived classes to **reuse or replace the implementation** provided by a base class. Is care of the compiler be sure that the right implementation of the member function is called each time, whenever the object in question is actually of the derived class, even if the object is accessed by a base pointer rather than a derived pointer. This is called **dynamic dispatch**.

{% highlight cpp %}
#include <stdio.h>
class Shape
{
public:
    Shape();
    virtual ~Shape();
    virtual double calculateArea();
protected:
    double area;
};
Shape::Shape() : area (0.0)
{
    printf("Shape::Ctor\n");
}
Shape::~Shape()
{
    printf("Shape::Dctor\n");
}
double Shape::calculateArea()
{
    printf("Shape::area ");
    return area;
}
class Square : public Shape
{
public:
    Square(double);
    virtual ~Square();
    virtual double calculateArea();
private:
    double length;
};
Square::Square(double l) : Shape(), length(l)
{
    printf("Square::Ctor\n");
}
Square::~Square()
{
    printf("Square::Dctor\n");
}
double Square::calculateArea()
{
    printf("Square::area ");
    area = length*length;
    return area;
}
class Triangle : public Shape
{
public:
    Triangle(double, double);
    virtual ~Triangle();
    virtual double calculateArea();
private:
    double width;
    double height;
};
Triangle::Triangle(double w, double h) : Shape(), width(w), height(h)
{
    printf("Triangle::Ctor\n");
}
Triangle::~Triangle()
{
    printf("Triangle::Dctor\n");
}
double Triangle::calculateArea()
{
    printf("Triangle::area ");
    area = width * height / 2;
    return area;
}
int main()
{
    Shape* pBase;
    pBase = new Shape();
    printf("%f\n", pBase->calculateArea());
    delete pBase;
	
    printf("\n");
    pBase = new Square(5);
    printf("%f\n", pBase->calculateArea());
    delete pBase;
	
    printf("\n");
    pBase = new Triangle(3, 5);
    printf("%f\n", pBase->calculateArea());
    delete pBase;
}
{% endhighlight %}

Although virtual functions make software extremely powerful, is not always a good idea mark all the member functions as "virtual". 

The firs reason is related to **software design**: a non-virtual function in the base class cannot and should not be overridden in child classes. 

The second reason is related to **performance**: virtual functions are more costly to invoke than non-virtuals. 
Indeed, non-virtual member functions are resolved at compile time (statically) by the compiler which select the member function that will be called based on the **type of the pointer/reference to the object**. Virtual functions, in contrast, are resolved at run-time (dynamically). In this case, the member function is selected based on the **type of the object** and not the type of the pointer/reference to that object. 

This technique is called *dynamic binding*. Most C++ compilers use a variant of dynamic binding for efficiency reasons.
**For each class** that has at least one virtual function,  the compiler creates a **global unique table** called the *virtual-table* or *v-table*. This table is basically an array of pointers to each of the virtual functions in the class.

If an object has one or more virtual functions, the compiler puts a hidden pointer in the object called a *virtual-pointer* or *v-pointer*. This v-pointer points to the *virtual-table*.

For example consider the code above. The class **Shape** has one virtual function called **calculateArea()**. There would be exactly one v-table associated with the class **Shape**, no matter how many Shape objects are defined, and the *v-pointer* of those objects would point to the same Shape's *v-table*. During a dispatch of a virtual function, the **run-time system** *follows* the object’s v-pointer to the class’s v-table, then follows the appropriate slot in the v-table to the method code.

Implement virtual functions is no costless in terms of space and time efficiency:

- space: is necessary store an extra pointer (v-pointer) for every object who have virtual members functions, plus an extra pointer for each virtual method in the v-table;

- time: call a virtual function requires two extra fetches compared to a normal function call: one to get the value of the v-pointer, a second one to get the address of the method in the v-table. None of this runtime overhead happens with non-virtual functions, since the compiler resolves them at compile-time based on the type of the pointer.

The output of the sample is:

{% highlight cpp %}
Shape::Ctor
Shape::area 0.000000
Shape::Dctor

Shape::Ctor
Square::Ctor
Square::area 25.000000
Square::Dctor
Shape::Dctor

Shape::Ctor
Triangle::Ctor
Triangle::area 7.500000
Triangle::Dctor
Shape::Dctor
{% endhighlight %}

The sample above shows some important things:

- inheritance: both the classes **Triangle** and **Square** inherit from class **Shape**, which means that both includes the data members of the base classes

- constructor/destructor chaining: when an object of class Square is created, that Shape's constructor is invoked as first, then followed by the Square's contructor. Destructors get invoked in the opposite order of the constructors

- virtual functions: the *rigth* implementaton of **calculateArea()** that will be called depend on the type of the instance *shape* points to. For example, on an instance of Square, we see that calling area invokes Shape's version, while calling triangle invokes Triangle's version


>Implement the same program in C

As first thing, let's see how is possible mimic *inheritance* between a base class and its derived classes using the *C Language*. As said previously, C++ compilers implement virtual functions by using a virtual function table, called **v-table**. If a class declares or inherits at least one virtual function, the compiler adds a hidden member **v-pointer** that points to a **v-table**. Each class have its own virtual table that store all the function pointers in an array:

{% highlight cpp %}
typedef void** VTable;
typedef VTable* VPointer;

VTable ShapeVTable = NULL;
VTable SquareVTable = NULL;
VTable TriangleVTable = NULL;
{% endhighlight %}

For transforming the classes in C-like structures, two step are required:

- replace each class with a **struct**
- follow a specific order in the derived class for member declaration

In particular, the first member in the derived class (*Square* or *Triangle*) need to be of the same type of the base class (*Shape*):

{% highlight cpp %}
//Class Shape
typedef struct
{
    VPointer vPointer;
    double area;
} Shape;
//Class Square
typedef struct
{
    Shape shape;
    double length;
} Square;
//Class Triangle
typedef struct
{
    Shape shape;
    double width;
    double height;
} Triangle;
{% endhighlight %}

In this way the memory is laid out from base-most to child-most and lead us to a first great advantage: the address of a derived class (e.g. *triangle* ) and that of base class (e.g. *shape*) are the same. This is exactly what happen in C++ where the compiler doesn't need to manipulate the address at all when assigning from child pointer to base pointer.

{% highlight cpp %}
Tringle* triangle = new Triangle();
Shape* shape = triangle;
{% endhighlight %} 

In the sample above, moreover, is important emphasize the use of the variable *vPointer*, which contains a pointer to the virtual table. 

The second important thing to consider is how build the *constructor/destructor chainings*. Indeed, when deal with inheritance the compiler make sure that the base class's constructor is called *before* than the derived class's constuctor. For destructors is the same, except that they are invoked in the opposite order of the constructors. 
In C++ is necessary declare a destructor as virtual: in this way the destruction of a generic object start from children to parents. 
Unfortunately, there is no way to mimic the same behavior in C, so the alternative is explicitly invoke the parent constructor inside a child constructor before initializing any member:

{% highlight cpp %}
void Shape_Ctor(Shape* this)
{
    printf("Shape::Ctor\n");
    this->vPointer = &ShapeVTable;
    this->area = 0.0;
}
void Square_Ctor(Square* this)
{
    Shape_Ctor((Shape*)this);
    printf("Square::Ctor\n");
    ((Shape*)this)->vPointer = &SquareVTable;
    this->length = 0;
}

void Delete_Shape(Shape* this)
{
    if (this)
    {
        ((destructor)(*(this->vPointer))[VFUNC_DESTRUCTOR])(this);
        free(this);
    }
}
{% endhighlight %}

Note that in *Square_Ctor()* the vPointer points to **SquareVTable** which contains the pointers to the Square class's member function. 

As explained before, each class has a **global unique** virtual table that is simply an array of pointers to members function. In our example, these three virtual tables are called respectively *ShapeVTable*, *SquareVTable* and *TriangleVTable*. For populating these tables in an easy I declarated an enum; it is useful to index the functions inside the vtables. Subsequently, each table is filled with the proper pointers to the functions (note the cast to void*):

{% highlight cpp %}
enum
{
    VFUNC_DESTRUCTOR,
    VFUNC_CALCULATE_AREA,
    NUM_VFUNCS
};
ShapeVTable = (VTable)malloc(sizeof(void*) * NUM_VFUNCS);
ShapeVTable[VFUNC_DESTRUCTOR] = (void*)&Shape_Dctor;
ShapeVTable[VFUNC_CALCULATE_AREA] = (void*)&Shape_calculateArea;

SquareVTable = (VTable)malloc(sizeof(void*) * NUM_VFUNCS);
SquareVTable[VFUNC_DESTRUCTOR] = (void*)&Square_Dctor;
SquareVTable[VFUNC_CALCULATE_AREA] = (void*)&Square_calculateArea;

TriangleVTable = (VTable)malloc(sizeof(void*) * NUM_VFUNCS);
TriangleVTable[VFUNC_DESTRUCTOR] = (void*)&Triangle_Dctor;
TriangleVTable[VFUNC_CALCULATE_AREA] = (void*)&Triangle_calculateArea;
}
{% endhighlight %}

The last step is the implementation of the **operator new**. It is responsible for allocating the memory for the object and build it invoking the constructor chain (which in turn sets up the vtable if necessary):

{% highlight cpp %}
Square* NewSquare(double l)
{
    Square* s = (Square*)malloc(sizeof(Square));
    Square_Ctor(s);
    s->length = l;
    return s;
}
{% endhighlight %}

At this point, there are all the elements for invoking a virtual functions polymorphically via a base class pointer. To invoke *calculateArea()*, the code first look up the address of the function in the instance's vtable following *vPointer*. This evaluates to a void*, a pointer to the function setted in InitVTables. This pointer is cast to a *calculateArea* function pointer type so that is possible invoke it using the **call operator ()**. 

{% highlight cpp %}
Shape* shape;
shape = (Shape*)NewSquare(5);
printf("%f\n",((calculateArea)(*(shape->vPointer))[VFUNC_CALCULATE_AREA])(shape)); 
{% endhighlight %}


>Summary

In this post I explained how is possible reuse the concepts of virtual functions, dynamic dispatch and inheritance using the C Programming Language. Starting from a C++ program, we have built the same program in C following the same rules adopted by a C++ compiler. More important, now should be more clear the mechanism behind virtual functions and the cost to pay in term of performance every time a function is declared as vitual. Non-virtual member functions are resolved statically at compile time, while virtual functions are resolved dynamically at run-time. Select the proper member function requires two extra fetches compared to a normal function call: one to get the value of the v-pointer and another to get the address of the method in the v-table. 

At the end of the page is reported the full program (main.c). If you liked this post please **leaves a comment** or **share it**.

##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)

[C++ FAQ Inheritance — virtual functions](http://www.parashift.com/c++-faq/virtual-functions.html)

[Object-oriented design](http://en.wikipedia.org/wiki/Object-oriented_design)

[http://vgcoding.blogspot.ca](http://vgcoding.blogspot.ca/2014/03/virtual-functions-in-c.html)


####main.c

{% highlight cpp %}
#include <stdio.h>
#include <stdlib.h>
enum
{
    VFUNC_DESTRUCTOR,
    VFUNC_CALCULATE_AREA,

    NUM_VFUNCS
};
typedef void (*destructor)(void*);
typedef double (*calculateArea)();
typedef void** VTable;
typedef VTable* VPointer;

VTable ShapeVTable = NULL;
VTable SquareVTable = NULL;
VTable TriangleVTable = NULL;

//Class Shape
typedef struct
{
    VPointer vPointer;
    double area;
} Shape;
void Shape_Ctor(Shape* this)
{
    printf("Shape::Ctor\n");
    this->vPointer = &ShapeVTable;
    this->area = 0.0;
}
Shape* NewShape()
{
    Shape* s = (Shape*)malloc(sizeof(Shape));
    Shape_Ctor(s);
    return s;
}
void Shape_Dctor(Shape* this)
{
    printf("Shape::Dctor\n");
}
double Shape_calculateArea(Shape* this)
{
    printf("Shape::area ");
    return this->area;
}
void Delete_Shape(Shape* this)
{
    if (this)
    {
        ((destructor)(*(this->vPointer))[VFUNC_DESTRUCTOR])(this);
        free(this);
    }
}

//Class Square
typedef struct
{
    Shape shape;
    double length;
} Square;
void Square_Ctor(Square* this)
{
    Shape_Ctor((Shape*)this);
    printf("Square::Ctor\n");
    ((Shape*)this)->vPointer = &SquareVTable;
    this->length = 0.0;
}
Square* NewSquare(double l)
{
    Square* s = (Square*)malloc(sizeof(Square));
    Square_Ctor(s);
    s->length = l;
    return s;
}
void Square_Dctor(Square* this)
{
    printf("Square::Dctor\n");
    Shape_Dctor((Shape*)this);    
}
double Square_calculateArea(Square* this)
{
    printf("Square::area ");
    ((Shape*)this)->area = this->length*this->length;
    return ((Shape*)this)->area;
}

//Class Triangle
typedef struct
{
    Shape shape;
    double width;
    double height;
} Triangle;
void Triangle_Ctor(Triangle* this)
{
    Shape_Ctor((Shape*)this);
    printf("Triangle::Ctor\n");
    ((Shape*)this)->vPointer = &TriangleVTable;
    this->width = 0;
    this->height = 0;
}
Triangle* NewTriangle(double w, double h)
{
    Triangle* t = (Triangle*)malloc(sizeof(Triangle));
    Triangle_Ctor(t);
    t->width = w;
    t->height = h;
    return t;
}
void Triangle_Dctor(Triangle* this)
{
    printf("Triangle::Dctor\n");
    Shape_Dctor((Shape*)this);    
}
double Triangle_calculateArea(Triangle* this)
{
    printf("Triangle::area ");
    ((Shape*)this)->area = this->width * this->height / 2;
    return ((Shape*)this)->area;
}

//Initialize Virtual Tables
void initVTables()
{
    ShapeVTable = (VTable)malloc(sizeof(void*) * NUM_VFUNCS);
    SquareVTable = (VTable)malloc(sizeof(void*) * NUM_VFUNCS);
    TriangleVTable = (VTable)malloc(sizeof(void*) * NUM_VFUNCS);
    // Populate Shape vtable entries
    ShapeVTable[VFUNC_DESTRUCTOR] = (void*)&Shape_Dctor;
    ShapeVTable[VFUNC_CALCULATE_AREA] = (void*)&Shape_calculateArea;
    // Populate SQUARE vtable entries
    SquareVTable[VFUNC_DESTRUCTOR] = (void*)&Square_Dctor;
    SquareVTable[VFUNC_CALCULATE_AREA] = (void*)&Square_calculateArea;
    // Populate Triangle vtable entries
    TriangleVTable[VFUNC_DESTRUCTOR] = (void*)&Triangle_Dctor;
    TriangleVTable[VFUNC_CALCULATE_AREA] = (void*)&Triangle_calculateArea;
}

void deleteVTables()
{
    free(ShapeVTable);
    free(SquareVTable);
    free(TriangleVTable);
    ShapeVTable = NULL;
    SquareVTable = NULL;
    TriangleVTable = NULL;
}

int main (int argc, const char * argv[]) {
    Shape* shape;
    initVTables();
    shape = NewShape();
    printf("%f\n",((calculateArea)(*(shape->vPointer))[VFUNC_CALCULATE_AREA])(shape)); 
    Delete_Shape(shape);                         
	
    printf("\n");
    shape = (Shape*)NewSquare(5);
    printf("%f\n",((calculateArea)(*(shape->vPointer))[VFUNC_CALCULATE_AREA])(shape));    
    Delete_Shape(shape);                        
	
    printf("\n");
    shape = (Shape*)NewTriangle(3,5);
    printf("%f\n",((calculateArea)(*(shape->vPointer))[VFUNC_CALCULATE_AREA])(shape));
    Delete_Shape(shape);
	
    deleteVTables();
    return 0;
}
{% endhighlight %}

