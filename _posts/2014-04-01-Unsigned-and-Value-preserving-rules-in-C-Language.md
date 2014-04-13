---
layout: post
category : lessons
tags: [c, ansi c, programming, signed, unsigned]
---
{% include JB/setup %}

**On behavior of an unsigned type when it is promoted to a larger type.**

<!--more-->

Few days ago I was working on a C++ program for decoding a financial protocol. Like all the other times, before commit my code I run a series of test to be sure that everything was fine: no compile errors, no warnings, no  memory leaks, 100% passed for coverage and unit tests.
 
However, few minute after committed my code, I realized that the build was broke. The issue was a **gcc warning** in my code: *comparison between signed and unsigned integer expressions.*

I started work for fixing the build as soon as possible, so I asked myself two questions:

1. Why I was unable to detect the error on my sandbox before the commit?

2. Where I made a mistake comparing a signed and unsigned?

This post is about the second question. What happen when an unsigned type is promoted to a **larger** type? Should the signed be preserved or not?(e.g. promotion to a larger signed or unsigned type)? I'll show you that the answer is no unique, and depends on how much the larger type is *truly* larger.

Look at the code below that shows the issue in a simplified way. Image you have an object called *paylaod* that simply represent an array of bytes, and you want check if the payload has a proper size, suppose 1500. The funtions *start()* and *end()* return respectively the position of the first and last bytes in the paylod.
 
{% highlight cpp linenos %}
uint8_t start = payload.start();
uint8_t end = payload.end();
unsigned length = 1500;
//rest of you code
if (length > end - start) {
    printf("Exceed limit !\n");
    return -1;
}
{% endhighlight %}

The warning was raised at line 5.

Apparentely all seems fine: *start* and *end* are both uint8_t. *length* is unsigned. Compare unsigned with unsigned doesn't broke the rules of the languade, so what is realy happening when **gcc** raise the warning for comparison between signed and unsigned values?

To explain this, let me introduce you the *unsigned preserving* and *value preserving* rules.

The **unsigned preserving rule** says that the promoted type is always *unsigned*, while the **value preserving rule** says that the conversion **depends on the actual sizes** of the original and promoted types. If the promoted type can represent all the values of the original (e.g unsigned type as signed value), then the promoted type is *signed*. If the two types have the same size, then the promoted type is *unsigned*.

The first consequence of this latter rule is that the results will vary from machine to machine due the actual sizes of the types used in making the decision. 
On some machines, short int is smaller than int, but on some machines, they're the same size. On some machines, int is smaller than long int, but on some machines, they're the same size.

In ANSI C Standard, the **value preserving rule** is applyed ( it reduce the number of cases where these surprising results occur). 

So what happened to the code above? The difference between *end* and *size* was promoted to an **int** before the comparison; but *int* is *signed*, and comparing a signed value with an unsigned value (*length*) is not permitted by the C Language rules.

To avoid surprises it's best to avoid mixing signed and unsigned types in the same expression. To solve the problem in the code above, an explicit cast can be used to remove any ambiguous promotion type.

{% highlight cpp linenos %}
uint8_t start = payload.start();
uint8_t end = payload.end();
unsigned length = 1500;
//rest of you code
if (length > (unsigned)(end - start)) {
    printf("Exceed limit !\n");
    return -1;
}
{% endhighlight %}

See you for the next post.


PS. If someone of you is curious to know more about the first question (why I didn't find the warning on my sandbox), well... the reason was due a different level of optimization specified for the build and the local sandbox.

##Further Information

[C Programming Language, 2nd Edition](http://www.amazon.com/C-Programming-Language-2nd-Edition/dp/0131103628)

[C-FAQ](http://www.c-faq.com/expr/preservingrules.html)

