---
layout: post
category : Development
tags: [Programmers' theoretical minimum, SPARC, register window]
image : development/development.png
tagline: Store function's parameters in special registers instead of stack memory.
---
{% include JB/setup %}

**Programmers’ theoretical minimum: do you never hear "register window"?**

<!--more-->

Call a function is expensive because an amount of resources available need to be reserved to properly handling the call and the return values.

This mechanism is described through the concept of **activation record**. The caller requires spaces on the stack to pass the parameters to the called function, the return value and the program counter.

Due the fact that the stack is a limited and precious resource, the **SPARC** architecture has a set of registers solely dedicated to holding parameters in procedure activation. This is called **register window**.
 
##Further Information

[Expert C Programming: Deep C Secrets](http://www.amazon.co.uk/gp/search?index=books&linkCode=qs&keywords=9780131774292) by Peter van der Linden
