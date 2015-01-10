---
layout: post
category : Development
tags: [NASA, c, critycal code]
image : nasa/nasa.png
tagline: The rules act like the seat-belt in your car.
---
{% include JB/setup %}

**Thoughts on the beauty of the code and code rules**

<!--more-->

#### Code guidelines
People involved in software projects agree on the use of coding guidelines. There are a lots of coding guidelines outside, proposed by several developer communities, sectors and IT companies.

I read several of these guidelines along my life. Curiously, there is little consensus on what a good coding standard is.
Despite guidelines provide useful insights and tips for software design and programming, they could contain well over a hundred rules, also with questionable justification. Sometimes, they focus too much over naming and indentation style, and less over best practices or tools to adopt.

Every changes made in the code should be done to make it **better**, **efficient** and **effective**. Every developer should do his best to follow coding style rules, but avoiding to be a style's fanatic. 

In my opinion, the aim of a set of good rules can be summarized in a single sentence: **make code beautiful**.
I am aware that use the word *beautiful* is pretty ambitious and could lead to an ambiguous interpretation in software world, so I'll be more clear.
I consider a software *beautiful* when it has three characteristics:

1. It expresses clearly developer's intention: names are well chosen, code lines are well indented,  and relationships and cooperations among components (functions, classes, libraries ecc. ecc.) are easy to identify and explain.

2.  It does its job well. Or in another way, it performs efficiently and effectively. Computational and storage resources are precious and absolutely cannot be wasted. The impact of an inefficient program is on overall system (software never runs alone). A memory leak in a program is an issue for all the other software that run in the system.

3. It does not make surprises. You could also say that it is 'idiot-proof'. A software should be robust enough to protect itself and the system from crashes.  Is a big mistake to underestimate this point, especially when code runs in critical contexts. A crash could have devastating consequences for business or people's life. Image what happen if a trading systems crashes during the market day, or the ABS system in a school bus stops to do its job.

Deep knowledge in software design, software paradigms, programming languages, tuning tools, performance measurement, debug and optimization are fundamental to write beautiful code. It's a goal hard to reach. Time, practice and dedication are needed. But keep in your mind that also imagination, problem solving and abstraction skills are foundamentals too.

The concept of beauty of code is sure something that cannot be explained easily. Maybe it cannot be explained at all, like some other Zen concepts. However, I think quote below could helps someone of you to reflect about *the beauty of code*:

> a well-written program is its own heaven; a poorly-written program is its own hell.


#### The Power of Ten – Rules for Developing Safety Critical Code

NASA is involved in development of critical software. **Gerard J. Holzmann**, a guy who works at **Jet Propulsion Laboratories**, proposed ten rules for developing **Safety Critical Code**.

I read these rules and like them. To quote Holzmann, *to be effective, a set of rules has to be small, and must be clear enough that it can easily be understood and remembered*.

It is great these rules are available for software community.


1. Restrict all code to very simple control flow constructs – do not use goto statements, setjmp or longjmp constructs, and direct or indirect recursion.

2. All loops must have a fixed upper-bound. It must be trivially possible for a checking tool to prove statically that a preset upper-bound on the number of iterations of a loop cannot be exceeded. If the loop-bound cannot be proven statically, the rule is considered violated.
 
3. Do not use dynamic memory allocation after initialization.

4. No function should be longer than what can be printed on a single sheet of paper in a standard reference format with one line per statement and one line per declaration. Typically, this means no more than about 60 lines of code per function.

5. The assertion density of the code should average to a minimum of two assertions per function. Assertions are used to check for anomalous conditions that should never happen in real-life executions. Assertions must always be side-effect free and should be defined as Boolean tests. When an assertion fails, an explicit recovery action must be taken, e.g., by returning an error condition to the caller of the function that executes the failing assertion. Any assertion for which a static checking tool can prove that it can never fail or never hold violates this rule. (I.e., it is not possible to satisfy the rule by adding unhelpful “assert(true)” statements.)


6. Data objects must be declared at the smallest possible level of scope.

7. The return value of non-void functions must be checked by each calling function, and the validity of parameters must be checked inside each function.

8. The use of the preprocessor must be limited to the inclusion of header files and simple macro definitions. Token pasting, variable argument lists (ellipses), and recursive macro calls are not allowed. All macros must expand into complete syntactic units. The use of conditional compilation directives is often also dubious, but cannot always be avoided. This means that there should rarely be justification for more than one or two conditional compilation directives even in large software development efforts, beyond the standard boilerplate that avoids multiple inclusion of the same header file. Each such use should be flagged by a tool-based checker and justified in the code.

9. The use of pointers should be restricted. Specifically, no more than one level of dereferencing is allowed. Pointer dereference operations may not be hidden in macro definitions or inside typedef declarations. Function pointers are not permitted.

10. All code must be compiled, from the first day of development, with all compiler warnings enabled at the compiler’s most pedantic setting. All code must compile with these setting without any warnings. All code must be checked daily with at least one, but preferably more than one, state-of-the-art static source code analyzer and should pass the analyses with zero warnings.


##Further Information
[The Power of Ten – Rules for Developing Safety Critical Code](http://www.google.ie/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CCAQFjAA&url=http%3A%2F%2Fspinroot.com%2Fgerard%2Fpdf%2FP10.pdf&ei=ZVyxVPC3A6WM7Aarz4E4&usg=AFQjCNEsPl28ABrG_WtO3EdejXH5YM5Lmw&sig2=E8uHJqbXdbj0cPqNq8zlFw&bvm=bv.83339334,d.ZGU), by Gerard J. Holzmann
NASA/JPL Laboratory for Reliable Software Pasadena, CA 91109

[Jet Propulsion Laboratory - NASA](http://www.google.ie/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0CCUQFjAA&url=http%3A%2F%2Fwww.jpl.nasa.gov%2F&ei=ulyxVIyOJNLZ7Qbu7YDADA&usg=AFQjCNE7SZUa6zxJC2oOB2klBkN9I6CPdQ&sig2=w0o3rsAfqzYVbdqxQwr2JA&bvm=bv.83339334,d.ZGU)
