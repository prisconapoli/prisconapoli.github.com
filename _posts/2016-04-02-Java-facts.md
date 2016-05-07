---
layout: post
category : Development
tags: [JAVA, JVM, effective java, object oriented]
image : java/java.jpeg
tagline: Learning the art of programming, like most other disciplines, consists of first learning the rules and then learning when to break them - Effective Java
---
{% include JB/setup %}

**Java (more or less) advanced**

<!--more-->

# Not full Object-Oriented
The Java programming language is object-oriented with single inheritance. Despite it is the  most famous object oriented programming language, inside a method is possible to use only an imperative statement-oriented coding style. 

# Refactoring
Bear in mind the fundamental goals of refactoring are the **improvement of system structure** and the **avoidance of code duplication**. Better to repeat again: **system structure** and **code duplication**. 


# Rules before yourself
Programmer or Software Archithect, no matter what's your job. Respect few fundamental rules:
 + clarity and simplicity come first
 + Don't make surprises, e.g. preserve the expected behavior
 + Small but no smaller
 + Design to reuse
 + Don't copy
 + Minimize dependencies
 + Detect errors as soon as possible, ideally at compile time

## Static factory methods Vs constructor
A static factory method is a static method thet returns an instace of a class.

A constructor is the way used by a class to allow a client to get an instance of itself.

So far so easy. But in some situations static factory methods are useful to clarify the programmer's intentions.

Static factory methods:
 - they've a name that be used to clarify the returned object
 - create instance-controlled classes. Is not required to return a new object each time (singleton, non instantiable, equal instances, e.g. use == instead of a.equals(b))
 - return object of any subtype
 - return non public object which implements public interface
 - reduce verbosity of creating parameterized type instances
 
Disadvantage:
 - use only static factory methods makes impossible to inherit from the class
 - not distinguishable e.g. *valueOf*, *of*, *getInstance*, *newInstance* 

## Scale object construction when faced with many parameters
 - telescoping constructor pattern, a constructor with only required parameters, another with a single optional parameter, a third with two optional parameter and so on, culminating in a constructor with all the optional parameters
 - JavaBeans patterns, call a parameterless constructor to create the object and then call setter methods to set each required parameters and each optional parameter of interest. Problem: 1. It can be in an inconsistent state through its construction. 2. Can't create immutable object
 - Builder pattern: call a constructor with the required parameters, and gets a builder object (so use a public static class). Then the client calls *setter-like* methods on the builder object to set each optional parameter of interest. Finally, the client calls a parameterless build method to generate the object (which is a private class) , which is immutable.

## Best way to implement a singleton
A singleton is a class that is instantiated exactly one. They are used to model single resources in the system.
- private constructor and public static final member. Vulnerable to AccessibleObject.setAccessible method.
- private constructor, private static final member, public static method.
Both the approaches above are vulnerable if the serialization is not well implemented. All fields need to be declared transient and provide an 'object readResolve()' method.
- make an enum type with one element. Serialization for free. Guaranteed one instance. Thread save. It works because enum fields are compile time constants, but they are instances of their enum type.  And, they're constructed when the enum type is referenced for the first time.

## Non instantiability
Making a class abstract does not work well to prevent that a class is instantiated through a subtype. In this situations, the rigth approach is making the constructor private.

## Avoid creating unnecessary objects

## Avoid unintentional object retantion.
Eliminate all references to obsolete objects. Everytime an object is unintentionally retained, it is excluded by garbage collector with all the other objects it refers to. Null out reference when it become obsolete. But bear in mind that nulling out object references should be the exception rather than the norm. The best way to eliminate an obsolete reference is to let the variable that contained the reference fall out of scope.
*Rule of thumb*: whenever a class manages its own memory, be alert for memory leaks. Easy way is nullable any variable that references to an obsolete object.
Another common source of memory leaks is caches. A third common source of memory leaks is listeners and other callbacks. Use heap profiler.

## Avoid finalizers
The golden rule with finalizers is *don't use them* because they have an unpredictable behaviour and there is a severe performance penanlty for using them. There is no guarantee a finalizer is executed promptly, and there is no guarantee that finalize is ever called on any object.
Never rely on finalizer and never put critical code in a finalizer.
In particular, should be used only for cleanup of non-Java resources.
Another oddity is the missing of *finalizer chaining* which is not performed automatically.

## Overriding equals
In a nutshell, the important concept is the difference between **logical equality** and **object identity**. Don't override the equals method if:
 - each instance is unique
 - there is no concept of logical equality
 - an appropriate equals is already implemented in a superclass
 - private class/package, and you know equals will never be invoked.

When override? whenever a class has a notion of **logical equality that differs from mere object identity**. This is generally true for value classes: classes which represent a value. For these classes, you need *satisfy the programmer expectation*.

With inheritance, is very easy implement badly the equals method, and violates both simmetry and transitivity properties.

##Dont't forget hashCode()
hashCode has to be overriden everytime equals has been overridden. **Equal objects must have the same hash code**.

##And toString(), of course!
It is recommended that all subclasses override this method. So, do it!
Provide a good *toString()** implementation makes a class much more pleasant to use.

This method is automatically invoked when an object is passed to *println*, *printf*, *concatenation operator*, or *assert* ecc. java.lang.Object provides a rudimental version of toString(). 

So please do a little effort, and design this method with the goal to **return all of the interesting information contained in the object**.

Is considered a good practice document the format used and provide static methods to easily translate back and forth between the object and its string representation. Whetever* or not you specify the format, provide programmatic access to all of the information contained in the value returned by toString.

##Clone it, but judiciously
The Cloneable interface is pretty weird, cause it has any methods. It modifies the behaviour of a protected method on a superclass, e.g **Object**'s protected *clone* method implementation.

The general contract for the *clone* method is weak. It creates and return copy of this object, but the precise meaning of "copy" may depend on the class of the object. The general intent is:
*x.clone() != x* will be true
*x.clone().getClass() == x.getClass()* will be true
*x.clone().equals(x)* will be true.

In practice, a class that implements *Cloneable* is expected to provide a properly functioning public *clone* method.

>Never make the client do anything the library can do for the client.

The *clone* architecture is incompatible with normal use of final fields referring to mutable objects, except in cases where the mutable objects may be safely shared between an object and its clone.

##Comparable and compareTo()
*compareTo()* is the sole method in the Comparable interface. It is not declared in **Object** class. It is used to define *natural ordering*. It is similar to *equals* method, except it permits order comparisons in addition to simple equality comparison.

A class that violates the *compareTo()* contract can break other classes that depend on the comparison, e.g. *TreeSet and *TreeMap. Other interfaces like *Collection*, *Set* or *Map* use the *equals* method, and this can lead to inconsistent results, e.g. entry duplication.
Also, *compareTo* requires an update everytime a new field is added to a class.

##Hide module's details
Decouples the modules that comprise a system is a primary goal for a good design.

Information hiding is not just a theoretical things or a fancy style in object-oriented programming. There is a massive practical impact with information hiding. It enables parallel development and testing, effective performance tuning, software reuse!

If you think that information hiding is hard to describe or implement, just follow this rule of thumb: your design goal is **make each class or member as inaccessible as possible**.

That means, use the lowest possible access level consistent with the solution you are developing.
Instance fields should never be public. Classes with mutable fields are not thread-safe. By making the field public you give up the flexibility to switch to a new internal data representation in which the field does not exist.

##Prefer accessors over public fields for public classes
If a class is accessible outside its package, provide accessor methods, to preserve the flexibility to change the class's internal representation. 
*Never never never* expose mutable fields in public classes! It is, however, sometimes desiderable for package-private or private nested classes to expose fields, whether mutable or immutable.
If a class exposes its data fields, all hope of changing its internal representation is lost, as client code can be distributes far and wide.
If you can help to expose fields directly, is less harmful if the fields are immutable.

##Immutable class is better (and resist the urge to write a setter for every getter)
An immutable class is simply a class whose instances cannot be modified. All of the information contained in each instance is provided when it is created and is fixed for lifetime of the object.

**Classes should be immutable unless there is a very good reason to make them mutable.** And if a class cannot be made immutable, limit its mutability as much as possible.

**Reduce the number of states in which an object can exist.** It makes it easier to reason about the objects and reduces the likelihood of errors.

**Make every field final unless there is a compelling reason to make it non final.**

*String* and *BigDecimal* are examples of immutable classes.
Immutable classes are less prone to error and more secure. To make a class immutable, follow these rules:
- Don't provide any mutators
- Ensure the class can't be extended, e.g. make it final or use static factories instead of constructors
- Make all fields final and private
- Ensure exclusive access to any mutable component


Why we like immutable object so much? For manys simple and extremely useful reasons.
1. One state. Yes, an immutable object can be in exactly one state, the state in which it was created. If you make sure that all constructors establish class invariants, then it is guaranteed that these invariants will remain true for all time, with no further effort on your part or on the part of the programmer who uses the class.
Rule of thumb: **no methods may modify the object and all fields must be final**. However, these rule is a bit stronger than necessary and can be relaxed to improve performance. In truth, no method may produce *externally visible* change in the object's state.

2. Thread safety. Immutable objects are inherently thread-safe; they require no synchronization because they cannot be corrupted by multiple threads.
They can be shared freely. Immutable classes should take advantage of this by encouraging clients to reuse existing instances wherever possible. A consequence of the fact that immutable objects can be shared freely is that you never have to make defensive copies.  In fact, any copy is required at all, because all copies would be forever equivalent to the original.

3. No copy, no clone. For immutable classe we don't need implement *clone()* method or a *copy contructor*. Immutable objects are great **building blocks** for other objects, whether mutable or immutable.

The only real disadvantage of immutable classes is that they require a **separate object for each distinct value**. Creating this object can be costly.

##The functional approach
In the functional approach, every methods return the result of applying a function to their operand without modifying thme. Contrast this to the more common procedural or imperative approach in which methods apply a procedure to their operand, causing *its state to change*.
The functional approach may appear unnatural if you’re not familiar with it, but it enables immutability, which has many advantages. Immutable objects are simple, fast and secure.

##Constructors
The purpose of a constructor is not limited to the creation of an instance of a specific class and the initialization of its fields. It's main purpose is to establish all object's **invariants**.

Don’t provide a public initialization method separate from the constructor or static factory unless there is a compelling reason to do so. Similarly, don’t provide a kind of *reinitialize()* method that enables an object to be reused as if it had been constructed with a different initial state. Such methods generally provide little if any performance benefit at the expense of increased complexity.

##Favor composition over inheritance
Inheritance is a powerful way to achieve code reuse, but it is not always the best tool for the job.  Used inappropriately, it leads to fragile software.  It's safe use inheritance within a package, because classes and subclasses are under control of the same programmer. **But inheriting from ordinary concrete classes across package boundaries is dangerous**.
To avoid problem, a subclass must evolve in tandem with its superclass, unless the superclass's authors have designed and documented it specifically for the purpose of being exented.

**Unlike method invocation, inheritance violates encapsulation.**
**Data encapsulation** is a mechanism of bundling the data, and the functions that use thir data.
**Data abstraction** is a mechanism of exposing only the interfaces and hiding the implementation details.

Use inheritance where composition is appropriate is dangerous. First, implementation details are exposed needlessly. The resulting API ties you to the original implementation, forever limiting the performance of your class. More seriously, by exposing the internals you let the client access them directly. At the very least, this can lead to confusing semantics.
And at very very least, if the API has any flows, you could propagate these flaws inside your class.

##Inheritance places limitations on the class
The following sentence is very important, so read it carefully and most important, keep it in you mind if you want design good code and not rubbish.

**Designing a class for inheritance places substantial limitations on the class.**

Firstly, a class designed to be extended, should document precisely its self-use of overridable methods, e.g. **non final** and either **public** or **protected**.

Bear in mind a good API documentation should describe **what** a given method does and not *how* it does. Describe overridable methods is an unfortunate consequences of the fact that inheritance violates encapsulation. To document a class so that it can be safely subclassed, you must describe implementation details that should otherwise be left unspecified.

Constructors must not invoke overridable methods, directly or indirectly. If you violate this rule, program failure will result. Ensure that the class never invokes any of its overridable methods and to document this fact.

If the class designed for inheritance implements Cloneable or Serializable, remember that *clone()* and *readObject()* behave a lot like constructors, so a similar restriction applies: nor *clone()* nor *readObject()* may invoke an overridable method, directly or indirectly.

Each time a change is made in such a class, there is a chance that client classes that extend the class will break. The best solution to this problem is to prohibit subclassing in classes that are not designed and documented to be safely subclassed. The easier of the two is to declare the class final. The alternative is to make all the constructors private or package-private and to add public static factories in place of the constructors

##For API designers.... No sorry, I meant for all
-Don't violate principle of least astonishment
-Don't violate the abstraction hierarchy
-Don't use similar names for widely different behaviours

An example is the **autoboxing**. Autoboxing blurs but does not erase the distiction between primitives and boxed primitives.

Only four of the six comparison operators work on boxes primitives:
1. <, >, <= and >= work
2. == and != do not work


##Abstract classes and Interfaces
The real practical use of an abstract class is that it can be used as type definition. The restrictions related to single inheritance are a pretty big limitation. Abstract classes enable the construction of rigid hierarchical frameworks.

Interfaces are on the opposite side. Their ideal use is for defining a so called*mixing*, a type that a class can implement in addition to its primary type to declare that it provides some optional behaviour. For their nature, interfaces enable safe and powerful functionality enhancements via the wrapper class idiom. However, they are not permitted to contain method implementations.

Provide an abstract skeletal implementation is a smart way to combine the virtues of interfaces and abstract classes. The interface defines the type, and the skeletal implementation takes all of the work out of implementing it.

Skeletal implementations are called AbstractInterface, where *Interface* is the name of the interface they implement, e.g. AbstractCollection, AbstractSet, AbstractList, and AbstractMap.

Abstract classes are far easier to evolve than an interface. Is possible add new methods with default implementatioj without breaking the hierarchy. Public interfaces, therefore, must be designed carefully. Once an interface is released and widely implemented, it is almost impossible to change.
If you don't do it right the first time, they will irritate you and your users.







