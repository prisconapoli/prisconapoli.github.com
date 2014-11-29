---
layout: post
category : Development
tags: [c, c++, coding standards]
image : cpp_coding_standard/cover.png
tagline: Fools ignore complexity. Pragmatists suffer it. Some can avoid it. Geniuses remove it.
---
{% include JB/setup %}

**46 advices, tools and best practices from the book *C++ Coding Standards***

<!--more-->

1. **Think**. Do follow good guidelines conscientiously; but don't follow them blindly. No set of guidelines, however good, should try to be a substitute for thinking.

2. **Manage pressure**. As software developers, we routinely face enormous pressure to deliver tomorrow's software yesterday. Under schedule pressure, we do what we are trained to do and are used to doing. 

3. **Coding Style**.

	* Don't specify how much to indent, but do indent to show structure.
	* Don't enforce a specific line length, but do keep line lengths readable.
	* Don't overlegislate naming, but do use a consistent naming convention.
	* Write useful comments. Write code instead of comments where possible.
	* Don't just place braces randomly or in a way that obscures scope nesting.
	* Try to follow the style already in use in each file.


4. **Take warnings to heart**.

	* Use your computer's highest warning level.
	* Require clean and warning-free builds.
	* Understand all warnings.
	* Eliminate warnings by changing your code, not by reducing the warning level.

5. **One-action build system**. Push one button. Use a fully automatic *one-action* build system that builds the whole project without user intervention.

6. **Successful builds produce no noise**. The ideal build is silent and warning-free and produce only one log message: *Build succeeded*.

7. **Version Control System (VCS)**. The palest of ink is better than the best memory *(Chinese proverb)*.

8. **Don't break the build**. The code in the VCS must always build successfully.

9. **Re-view code**. More eyes will help make more quality. Show your code, and read others'. You'll all learn and benefit.

10. **What come first**. Correctness, simplicity, and clarity come first.

11. **Focus on one thing at a time**. Prefer to give each entity (variable, class, function, namespace, module, library) one well-defined responsibility.

12. **Keep Entity's responsibilities limited**. As an entity grows, its scope of responsibility naturally increases, but its responsibility should not diverge.

13. **One sentence is enough**. A good business idea, they say, can be explained in one sentence.

14. **better than**.

	* Correct is better than fast.
	* Simple is better than complex.
	* Clear is better than cute.
	* Safe is better than insecure.

15. **KISS**. Keep It Simple Software. What you can't comprehend, you can't change with confidence.

16. **Manage more data**. Whatever your code does today it may be asked to do tomorrow against much more data.

17. **Choose flexibile and dynamic data structures**. Use flexible, dynamically allocated data structures instead of fixed-size. Arrays *larger than the largest I'll ever need* are a terrible correctness and security fallacy.

18. **Prefer to use linear (or better) algorithms wherever possible**. Avoid polynomial algorithms where reasonable.

19. **Exponential algorithms**. Avoid them with all your might.

20. **The first rule of optimization**. Don't do it

21. **The second rule of optimization (for experts only)**: Don't do it yet.

22. **Optimization goals**. Measure twice, optimize once. Optimization
must be preceded by **measurement**; and measurement must be preceded by **optimization goals**. Until the need is proven, your focus should be on priority.

23. **Demand proof**. When someone asks you to optimize, do demand proof.

24. **Easy on yourself**. Easy on the code.

24. **Sharing causes contention**. Avoid shared data, especially global data. Shared data increases coupling, which reduces maintainability and often performance.

25. **Share nothing**. Prefer communication (e.g., message queues) over data sharing.

26. **Information hiding**. Don't tell. Don't expose. Use abstraction.

27. **One man's constant is another man's variable**. The C++ Standard says not one word about threads. Nevertheless, C++ is routinely and widely used to write solid multithreaded code.

28. **Compile-time polymorphism**. Consider replacing *run-time polymorphism* (virtual functions) with *compile-time polymorphism* (templates) when defining generic functions or type.

29. **Const is viral**. Add it in one place, and it wants to propagate throughout your code as you call other functions whose signatures aren't yet const-correct.

30. **Const-correctness is worthwhile**. It is proven, effective, and highly recommended.

31. **The first rule about macros**. Don't use them.

32. **The second rule about macros**. Don't use them unless you have to. 

33. **Are macros good?**. Almost every macro demonstrates a flaw in the programming language, in the program, or in the programmer.

34. **Are macros always bad?**. Macros remain the only solution for a few important tasks, such as *#include* guards, *#ifdef* and *#if* defined for conditional compilation, and implementing assert.

35. **No magician required**.Programming isn't magic, so don't incant it.

36. **State make you vulnerable**. Variables introduce state, and you should have to deal with as little state as possible, with lifetimes as short as possible.

37. **Sensible initialization**. Don't declare a variable before you can initialize it sensibly.

38. **Memory management requires disciplines**. Clean memory before you use it. Initialize variables upon definition.

39. **Wisdom means knowing when to refrain**. Write to minimize duplication and maximize efficiency. But premature optimization is dangerous.
 
40.  **Clarity. Above all**. The most important single aspect of software development is to be clear about what you are trying to build - Bjarne Stroustrup.

41. **Avoid inheritance taxes**. Prefer composition to inheritance unless you know that the latter truly benefits your design.

42. **Prefer weakest relationship instead of strongest**. If a relationship can be expressed in more than one way, use the weakest relationship that's practical.

43. **Composition wins inheritance**.

	* Greater flexibility without affecting calling code
	* Greater compile-time insulation, shorter compile times

44. **Don't pay for what you don't need**. Unless you need inheritance's power, don't endure its drawbacks.

45. **Behavior and state**. Prefer to add non member functions instead of member functions. Prefer composition instead of inheritance


##Further Information
[C++ Coding Standards: 101 Rules, Guidelines, And Best Practices](http://www.amazon.it/Coding-Standards-Rules-Guidelines-Practices/dp/0321113586), by Herb Sutter, Andrei Alexandrescu, Bjarne Stroustrup

