---
layout: post
category : lessons
tagline: "Supporting tagline"
tags : [intro, beginner, jekyll, tutorial]
---
{% include JB/setup %}

This Jekyll introduction will outline specifically  what Jekyll is and why you would want to use it.
Directly following the intro we'll learn exactly _how_ Jekyll does what it does.

## Overview

**On the power of the rvalues references and the different meanings of *&&* when this is used in template functions**


Here we are. In this post I’ll introduce you about the power of the **rvalue references (rrefs)** and what pitfalls may arise when these latter are used as arguments in **templates functions**.
Probably you have already heard about rref. People describe them as one of the most important new features in C++11. To tell the truth, **Move Semantic** and **Perfect Forwarding** are the real coolest new features. Rrefs are simply the mechanism on which they are built. Before enter in the core of our discussion, let's take a quick look at what **lvalues** and **rvalues** are.

The first thing to keep in mind is that lvalues and rvalues are both **expressions**. We can say that an expression is an lvalue if we can take the address of its memory location via the *& operator* (if you are interested in a rigorous definition take a look at this . The most simple example of lvalue that you can think is the declaration of a variable **var** of type **T**:
