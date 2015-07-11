---
layout: post
category : Development
tags: [c++,  c, struct hack,  zero length array]
image : zen_programming/ninja.jpg
tagline: A well-written program is its own Heaven; a poorly-written program is its own Hell - The Tao Of Programming

---
{% include JB/setup %}

**Design space-efficient variable length structs.**
<!--more-->

Put yourself as a C/C++ developer which is writing a software for a National Library or similar. At some point, you will deal with the modeling of book into software architecture.
A simple entity as a book is insidious, because it can have lots of related information, ie title, author, ISBN code, recensions from other users, ecc. But for the purpose of this discussion, let’s reduce the information required at minimum: just the ISBN code, the number of pages and a text description which will contain everything else.

Let's consider the code below: 

{% highlight cpp %}
typedef struct Book {
    char ISBN[13];
    char description[MAX_SIZE];
    int pages;
} Book;

// somewhere in your program
Book anotherBook = (Book *) malloc (sizeof(Book));
{% endhighlight %}

Which value you will choose for description? Perhaps 512 characters would be enough for the most part of cases, but we want to be sure that also bigger descriptions (e.g. 1024, 2048 ecc) can be stored safely. Moreover, we don't want to waste space when a description is smaller than **MAX_SIZE**.
A trivial solution is replace the fixed array which a pointer to char. In this way seem we solved our big issue: don't waste memory space. However, with this changes we've implicitly slowed down our code. Can you guess why?

{% highlight cpp %}
typedef struct Book {
    char ISBN[13];
    char* description;
    int pages;
} book;
{% endhighlight %}

Consider how the new *Book* struct will be used:

{% highlight cpp %}
// somewhere in your program
Book anotherBook = (Book *) malloc (sizeof(Book));
anotherBook->description = (char *) malloc(sizeof(char) * 512);
{% endhighlight %}

We have introduced the requirement for an **extra malloc**. Moreover, there is no guarantee that description will be allocated in **contiguous memory locations** to **book**.


But there is more. **malloc** is a generic function and is optimized for big chunk of data. In case of small object, ie 10, 50 or 100 bytes, the overhead paid to maintain the collection of free memory blocks is not negligible.
Moreover, we pay also the extra cost of pointer dereferencing to access the description. In some situations, dereferencing a pointer could have a catastrophic impact on performance, cause it can invalidate a cache line, require to transfer data from RAM and CPU caches and, in the worst case, read data form the swap area in the disk.
Does exist a way to handle efficiently a variable description without these extra costs? Of course the answer is yes, and is called flexible array member, or in a more geek way, struct hack. The former terminology has been adopted after this technique has been standardised in [C99](https://en.wikipedia.org/wiki/C99), while the latter comes from the early [GCC(C90)](https://en.wikipedia.org/wiki/GNU_Compiler_Collection). Look below how **Book** can be redefined:

{% highlight cpp %}
typedef struct Book {
    char ISBN[13];
    int pages;
    char description[];
} book;
{% endhighlight %}

First, no length has been provided for the description field. Second, description field has been moved at the end of the struct.
How this small code refactor can be helpful? Well, as first thing it worth to note that the sizeof(Book) is 13 (if no padding, ie __attribute__((packed)) is provided ) or 20 bytes.
Most important, is that now description has 0 length.
With this trick, you can allocate extra space with just one malloc, with the guarantee that description will be contiguous to the other fields, in order to maximize caching effect and reduce page swapping. Cool!

{% highlight cpp %}
// somewhere in your program
Book anotherBook = (Book *) malloc (sizeof(Book) + sizeof(sizeof(char) * 512));
//Now you can access description as you have a pointer, ie. anotherBook->description
{% endhighlight %}

With this short post I tried to show again how small is the demarcation line from efficient code from inefficient. My advice is to force always yourself to think deeper on the impact of every line code.

##Further Information

[GNU Compiler Collection](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)

[GCC Arrays of Length Zero](https://gcc.gnu.org/onlinedocs/gcc/Zero-Length.html)

[C99](https://en.wikipedia.org/wiki/C99)



