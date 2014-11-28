---
layout: post
category : Development
tags: [c, c++, coding standards]
image : cpp_coding_standard/cover.png
tagline: Do follow good guidelines conscientiously. But don't follow them blindly.
---
{% include JB/setup %}

**Advices, best practices and design gems from the book *C++ Coding Standards***

<!--more-->

**Think**. Do follow good guidelines conscientiously; but don't follow them blindly […] No set of guidelines, however good, should try to be a substitute for thinking.

As software developers, we routinely face enormous pressure to deliver tomorrow's software yesterday. Under schedule pressure, we do what we are trained to do and are used to doing. So 

<!--summary-->

Good rules:
Don't specify how much to indent, but do indent to show structure

Don't enforce a specific line length, but do keep line lengths readable

Don't overlegislate naming, but do use a consistent naming convention

Write useful comments: Write code instead of comments where
possible


Don't just place braces randomly or in a way that ob-
scures scope nesting, and try to follow the style already in use in each file.

Take warnings to heart: Use your computer's highest warning level. Require clean (warning-free) builds. Understand all warnings. Eliminate warnings by changing your code, not by reducing the warning level.

Use an automated build system. Push the (singular) button: Use a fully automatic ("one-action") build system that
builds the whole project without user intervention.

Successful builds should be silent and warning-free. The ideal build produces no noise and only one log message: "Build succeeded."

The palest of ink is better than the best memory (Chinese proverb): Use a version control system (VCS).

Don't break the build. The code in the VCS must always build successfully.

Re-view code: More eyes will help make more quality. Show your code, and read others'. You'll all learn and benefit.

Fools ignore complexity. Pragmatists suffer it. Some can avoid it. Geniuses remove it.

Correctness, simplicity, and clarity come first.

Focus on one thing at a time: Prefer to give each entity (variable, class, function,
namespace, module, library) one well-defined responsibility. As an entity grows, its
scope of responsibility naturally increases, but its responsibility should not diverge.

A good business idea, they say, can be explained in one sentence.

Correct is better than fast. Simple is better than complex. Clear is better than cute. Safe is better than insecure.

KISS (Keep It Simple Software): what you can't comprehend, you can't change with confidence.

One clear consequence is that whatever your code does today it may be asked to do tomorrow against more data—much more data.

Useflexible,dynamically-allocated data and instead of fixed-size arrays:Arrays"larger
than the largest I'll ever need" are a terrible correctness and security fallacy.

Prefer to use linear (or better) algorithms wherever possible. Avoid polyno-
mial algorithms where reasonable. Avoid exponential algorithms with all your
might

The first rule of optimization is: Don't do it. The second rule of op timization (for experts only) is: Don't do it yet. Measure twice, optimize once

So, optimization
must be preceded by measurement; and measurement must be preceded by optimization goals. Until the need is proven, your focus should be on priority.

When someone asks you to optimize, do demand proof.

Easy on yourself, easy on the code.

Sharing causes contention: Avoid shared data, especially global data. Shared data increases coupling, which reduces maintainability and often performance.

Strive for "shared-nothing;" prefer communication (e.g., message queues)
over data sharing.

Information hiding. Don't tell: Don't expose internal information from an entity that provides an abstraction.

The C++ Standard says not one word about threads. Nevertheless, C++ is routinely
and widely used to write solid multithreaded code.

One man's constant is another man's variable.

Compile-time polymorphism. Consider replacing run-time polymorphism (virtual functions) with compile-time polymorphism (templates) when defining generic functions or type

Const is "viral". Add it in one place, and it wants to propagate throughout your
code as you call other functions whose signatures aren't yet const-correct.

Const-correctness is worthwhile, proven, effective, and highly recommended.

The first rule about macros is: Don't use them unless you have to. Almost every macro demonstrates a flaw in the programming language, in the program, or in
the programmer

Macros remain the only solution for a few important tasks, such as #include guards, #ifdef and #if defined for conditional compilation, and implementing
assert.

Programming isn't magic, so don't incant it.

Variables introduce state, and you should have to deal with as little state as possible, with lifetimes as short as possible.

They can't always be sensibly initialized: Never declare a variable before you can
initialize it sensibly.

Being disciplined about cleaning memory
before you use it; initialize variables upon definition.

//Create a zero filled array of size MAX_PATH
char path[MAX_PATH] = {'\0' };

Write to minimize duplication and maximize
efficiency. But premature optimization is dangerous.

Wisdom means knowing when to refrain.

The most important single aspect of software development is to be clear about what you are trying to build (Bjarne Stroustrup).

Avoid inheritance taxes. Prefer composition to inheritance unless you know that the latter truly benefits your design.

If a relationship can be expressed in
more than one way, use the weakest relationship that's practical.

Composition has important advantages over inheritance:
1- Greater flexibility without affecting calling code. 
2-Greater compile-time insulation, shorter compile times

But don't pay for what you don't need; unless you need inheritance's power, don't endure its drawbacks.

To add behavior, prefer to add non member functions instead of member functions.

To add state, prefer composition instead of inheritance. Avoid inheriting from concrete base
classes.


##Class design and interface

The most important thing to get right is the interface. Everything else can be fixed later. Get the interface wrong, and you may never be allowed to fix it.

Inheritance is the second-strongest relationship you can express in C++, second only to friend.

The most critical factor during the design phase, is how to manage dependencies among components.

Prefer minimal classes to monolithic classes.

A minimal class embodies one concept at the right level of granularity.

Monolithic classes usually result from an attempt to predict and deliver a "com
plete" solution to a problem; in practice, they virtually never succeed.

Avoid inheritance taxes: Inheritance is the second-tightest coupling relationship in C++, second only to friendship.

A sound rule of software engineering is to minimize coupling: If a relationship can be expressed in
more than one way, use the weakest relationship that's practical.

If you can express a class relationship using composition alone, you should prefer that.

Using a standalone class as a base is a
serious design error and should be avoided.

**To add behavior, prefer to add non-member functions** instead of member functions. **To add state, prefer
composition** instead of inheritance. Avoid inheriting from concrete base classes.

Love abstract art: Abstract interfaces help you focus on getting an abstraction right
without muddling it with implementation or state management details. 

Prefer to design hierarchies that implement abstract interfaces that model abstract concepts.

Avoiding state in abstract interfaces simplifies the entire hierarchy design.

Misuse of inheritance destroys correctness. Public inheritance is indeed about reuse, but not the way many programmers seem to think.

Know what: Public inheritance allows a pointer or reference to the base class to actually refer to an object of some derived class, without destroying code correctness and without needing to change existing code.
Know why: Don't inherit publicly to reuse code (that exists in the base class); inherit publicly in order to be reused (by existing code that already uses base objects polymorphically).

As already pointed out, the purpose of public inheritance is to implement substitutability. The purpose of public inheritance is not for the derived class to reuse base class code to implement itself in terms of the base class's code. Such an i implemented-in-terms-of relationship can be entirely proper, but should be modeled by composition—or, in special cases only, by nonpublic inheritance (see Item 34).

Although derived classes usually add more state (i.e., data members), they model subsets, not supersets, of their base classes. In correct inheritance, a derived class models a special case of a more general base concept.

Consider making virtual functions nonpublic, and
 public functions nonvirtual.

Prefer to make public functions nonvirtual, and prefer to make virtual functions private (or protected if derived classes need to be able to call the base versions). This is the Nonvirtual Interface (NVI) pattern.

A public virtual function inherently has two different and competing responsibilities, aimed at two different and competing audiences:
1. It specifies interface: Being public, it is directly part of the interface the class pre
sents to the rest of the world.

2. It specifies implementation detail: Being virtual, it provides a hook for derived
classes to replace the base implementation of that function (if any); it is a cus
tomization point.

##Further Information


