---
layout: post
title : What the code says? 
category: lesson
tags: [rvalue, lvalue, rref, lref, std::move, references, template, c++, c++11]
---

{% include JB/setup %}

**On the power of the rvalues references and the different meanings of *&&* when this is used in template functions**

Here we are. In this post I’ll introduce you about the power of the **rvalue references (rrefs)** and what pitfalls may arise when these latter are used as arguments in **templates functions**.
Probably you have already heard about rref. People describe them as one of the most important new features in C++11. To tell the truth, **Move Semantic** and **Perfect Forwarding** are the real coolest new features. Rrefs are simply the mechanism on which they are built. Before enter in the core of our discussion, let's take a quick look at what **lvalues** and **rvalues** are.