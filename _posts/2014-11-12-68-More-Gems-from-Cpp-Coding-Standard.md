---
layout: post
category : Development
tags: [c, c++, coding standards]
image : cpp_coding_standard/cover.png
tagline: Misuse of inheritance destroys correctness.
---
{% include JB/setup %}

**68 more gems from the book *C++ Coding Standards***

<!--more-->

1. **Units of work**. Functions, including overloaded operators, are the fundamental units of work. This has a direct effect on how we reason about the correctness and safety of our code.

2. **Parameterize well**. Choosing well among values, references, and pointers for parameters is good habit that maximizes both safety and efficiency.

3. **const-qualify input parameters**. Always const-qualify all pointers or references to input-only parameters. Consider pass-by-value instead of reference if the function requires a copy of its argument.


4. **C-style varargs**. Don't use it. Never.


5. **Avoid surprises**. Overload operators only for good reason, and preserve natural semantics. In ambiguous or counterintuitive cases, prefer using named functions instead of fostering cryptic code.

6. **Doubt**. When in doubt, do as the ints do.

7. **Binary Arithmetic Operators**. When defining binary arithmetic operators, provide their assignment versions as well, and write to minimize duplication and maximize efficiency.

8. **Assignment operator**. Assignment version should be member function, while non-assignment function a normal function or friend.

9. **postfix/prefix**. Prefer to implement the postfix form in terms of the prefix form.

10. **prefix**. The prefix form is semantically equivalent, just as much typing, and often slightly more efficient by creating one less object. This is not premature optimization; it is avoiding premature pessimization.

11. **Logical operators**. The primary reason not to overload logical operators is that you cannot implement the full semantics of the built-in operators in these three cases, and programmers commonly expect those semantics. In particular, the built-in versions evaluate left-to-right, and also use short-circuit evaluation.

12. **Keep (evaluation) order**. Don't write code that depends on the
order of evaluation of function arguments.

13. **Right interface above all**. The most important thing to get right is the interface. Everything else can be fixed later. Get the interface wrong, and you may never be allowed to fix it.

14. **Inheritance**. It is the second-strongest relationship you can express in C++, second only to friend.

15. **Critical factor during the design phase**. How to manage dependencies among components.

16. **Minimal classes**. Prefer minimal classes to monolithic classes.

17. **1 Concept. 1 Class**. A minimal class embodies one concept at the right level of granularity.

18. **Monolithic always fails**. Monolithic classes usually result from an attempt to predict and deliver a *complete* solution to a problem.

19. **Weakest relationship**. If a relationship can be expressed in more than one way, use the weakest relationship that's practical. If you can express a class relationship using composition alone, you should prefer that.

20. **Standalone class is evil**. Using a standalone class as a base is a serious design error and should be avoided.

21. **To add behavior**. Prefer use non-member functions** instead of member functions.

22. **To add state**. Prefer composition instead of inheritance

23. **Love abstract art**. Abstract interfaces help you focus on getting an abstraction right without muddling it with implementation or state management details. 

24. **Root hierarchies in abstract classes**. Design hierarchies that implement abstract interfaces that model abstract concepts.

25. **Master the Dependency Inversion Principle.**

	* High-level modules should not depend upon low-level modules. Rather, both should depend upon abstractions.

	* Abstractions should not depend upon details. Rather, details should depend upon abstractions

26. **No state in abstract interfaces**. This simplifies the entire hierarchy design.

27. **Public inheritance is about substitutability**. Inherit to be reused, not to reuse.

28. **Misuse of inheritance destroys correctness**. Public inheritance is indeed about reuse, but not the way many programmers seem to think.

29. **Know what**. Public inheritance allows a pointer or reference to the base class to actually refer to an object of some derived class, without destroying code correctness and without needing to change existing code.

30. **Know why**. Don't inherit publicly to reuse code (that exists in the base class); inherit publicly in order to be reused (by existing code that already uses base objects polymorphically).


31. **Derived classes**. Although they usually add more state (i.e., data members), they model subsets, not supersets, of their base classes.


32. **Prefer full abstraction**. Consider making virtual functions nonpublic, and public functions nonvirtual. This is the *Nonvirtual Interface (NVI)*pattern.


33. **Avoid providing implicit conversions**. Prefer to rely on explicit conversions (explicit constructors and named conversion functions).

34. **explicit** By default, write explicit on single-argument constructors

35. **Public data is bad**.  A class models an abstraction and maintain invariants. Having public data means that part of your class's state can vary uncontrollably, unpredictably, and asynchronously with the rest of its state. 

36. **Private data preserve invariants**. It demonstrates that you have invariants and some intent to preserve them.

37. **Don't give away your internals**. Avoid returning handles to internal data managed by your class, so clients won't uncontrollably modify state that your object thinks it owns.

38. **Give safe handler**. But hiding data and then giving away handles to it is self-defeating.

39. **Master PIMPL**. making private members truly invisible using the Pimpl idiom to implement compiler firewalls and increase information hiding. 

40. **Name lookup and overload resolution**. Even though private member functions can never be called from outside the class and its friends, they do participate in name lookup and overload resolution and so can render calls invalid or ambiguous.

41. **Avoid membership fees**. Where possible, prefer making functions nonmember non-friends.

42. **Don't hide good news**. If a class defines any overload of operator new, it should provide overloads of all three of plain, in-place, and non-throwing operator new.

43. **Respect declaration order**. Write member initializers in the same order in which the members are declared. The reason for this language design decision is to ensure there is a unique order to destroy members; otherwise, the destructor would have to destroy objects in different orders, depending on the constructor that built the object.

44. **Initialization over assignment**. Using initialization instead of assignment to set member variables prevents needless run-time work and takes the same amount of typing.

45. **Ctor or Dtor shouldn't use virtual functions**. A call from a constructor or destructor to a pure virtual function that isn't defined at all has undefined behavior. Other techniques such as post-constructors should be used.

46. **Base class is equavalent to an abstraction**. Recall that for each member function participating in that abstraction, you need to decide:

	* Whether it should behave virtually or not.

	* Whether it should be publicly available to all callers using a pointer to Base or else be a hidden internal implementation detail.

47. **Always write a destructor for a base class**. Because the implicitly gener- ated one is public and nonvirtual.

48. **Destructors, deallocation, and swap never fail**. These are key functions that must not fail because they are necessary for the two key operations in transactional programming: to back out work if problems are encountered during processing, and to commit work if no problems occur.

49. **Exceptions in destructor**. Consider the following advice and requirements found in the C++ Standard:

	* If a destructor called during stack unwinding exits with an exception, terminate is called. So destructors should generally catch exceptions and not let them propagate out of the destructor.

	* No destructor operation defined in the C++ Standard Library [including the destructor of any type that is used to instantiate a standard library template] will throw an exception.

50. **Destructors don't throw**. Destructors that call functions that might throw exceptions need to protect themselves against leaking those exceptions.

51. **Copy constructor, copy assignemnt and destructor**.

	* If you write/disable either the copy constructor or the copy assignment operator, you probably need to do the same for the other.

	* If you explicitly write the copying functions, you probably need to write the destructor.

	* If you explicitly write the destructor, you probably need to explicitly write or disable copying.

52. **Copy consciously**. Ensure that your class provides sensible copying, or none at all. The choices are:

	* Explicitly disable both
	
	* Explicitly write both

	* Use the compiler-generated versions and add a comment to explain that the default behaviour is correct.


53. **STL Containers**. Disabling copying and copy assignment means that you cannot put a generic T objects into standard containers.

54. **Be proactive**. Copy operations can be insidious because the compiler has the tendency to generously generate them, and the compiler-generated versions are often unsafe by default for non-value-like types. 

55. **Clone memebr function**. In base classes, consider disabling the copy constructor and copy assignment operator, and instead supplying a virtual Clone member function if clients need to make polymorphic (complete, deep) copies.

56. **Copy constructor cannot be virtual**. In C++ the copy constructor is not virtual and cannot be made virtual.


57. **Assignment operator=**. Don't return const T&. Although this has the benefit of preventing odd code like (a = b) = c, it has the drawback that you wouldn't be able to put T objects into standard library containers. STL  containers require that assignment return a plain T&.

58. **Self-assignment**. Avoid writing a copy assignment operator that relies on a check for self-assignment in order to work properly; often, that reveals a lack of error safety.

59. **Use swap to implement copy assignment**. If you write the copy assignment operator using the swap idiom it will automatically be both strongly error-safe and safe for self-assignment; if self-assignment is frequent due to reference aliasing or other reasons, it's okay to still check for self-assignment anyway as an optimization check to avoid needless work.

60. **No-fail swap**. Consider using swap to implement copy assignment in terms of copy construction. For primitive types and for standard containers, std::swap will do. Other classes might implement swapping as a member function under various names.

61. **The Interface Principle**. For a class X, all functions (including nonmember functions) that both *mention* X and are *supplied with* X in the same namespace are logically part of X, because they form part of X's interface

62. **Namespaces**. Use them to manage names and reduce name collisions.

63. **Separate namespaces**. Keep types and functions in separate namespaces unless they're specifically intended to work together.

64. **Argument-dependent lookup**. ADL (also known as Koenig lookup) ensures that nonmember functions that take X objects and that are supplied with X's definition can participate as first-class members of X's interface, just like X's direct member functions naturally do.

65. **Namespace and #include directive**. Never write a using declaration or a using directive before an #include directive. You can and should use namespace using declarations and directives liberally in your implementation files after #include directives and feel good about it.

66. **The edge of a module**. Don't allow a type to appear in a module's external interface unless you can ensure that all clients understand the type correctly. Use the highest level of abstraction that clients can understand.

67. **Types in external interface**.The more widely distributed your library, and the less control you have over the build environment of all of its clients, the fewer the types that the library can reliably use in its external interface.

68. **lower-level abstraction is more portable**. If some clients understand only low-level types, and you must therefore use those, consider also supplying alternate operations that use higher-level types. Even when you choose to use a lower-level abstraction in a module's external interface, always use the highest level of abstraction internally and translate to the lower-level abstraction at the module's boundary. 

##Further Information
[C++ Coding Standards: 101 Rules, Guidelines, And Best Practices](http://www.amazon.it/Coding-Standards-Rules-Guidelines-Practices/dp/0321113586), by Herb Sutter, Andrei Alexandrescu, Bjarne Stroustrup

