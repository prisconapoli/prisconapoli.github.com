---
layout: post
title : What the code says? 
category: lessons
tags: [rvalue, lvalue, rref, lref, std::move, references, template, c++, c++11]
tagline: "Supporting tagline"
---

{% include JB/setup %}

**On the power of the rvalues references and the different meanings of *&&* when this is used in template functions**


Here we are. In this post I’ll introduce you about the power of the **rvalue references (rrefs)** and what pitfalls may arise when these latter are used as arguments in **templates functions**.
Probably you have already heard about rref. People describe them as one of the most important new features in C++11. To tell the truth, **Move Semantic** and **Perfect Forwarding** are the real coolest new features. Rrefs are simply the mechanism on which they are built. Before enter in the core of our discussion, let's take a quick look at what **lvalues** and **rvalues** are.

The first thing to keep in mind is that lvalues and rvalues are both **expressions**. We can say that an expression is an lvalue if we can take the address of its memory location via the *& operator* (if you are interested in a rigorous definition take a look at this [ACCU article](http://accu.org/index.php/journals/227)). The most simple example of lvalue that you can think is the declaration of a variable **var** of type **T**:
