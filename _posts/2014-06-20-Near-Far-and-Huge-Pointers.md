---
layout: post
category : misc
tags: [Programmers' theoretical minimum, near, far, large, pointers]
---
{% include JB/setup %}

**Programmers’ theoretical minimum: do you never hear the auto keyword?**

<!--more-->

If someone of you need to debug a program written in C more than 15 years ago, could face with some special pointers declarations:

{% highlight cpp %}
int __near *pNear;
int __far *pFar;
int __huge *pHuge;
{% endhighlight %}

The use of these keywords are relevant only on 16 bit Intel Architectures and stopped being significant about two decades ago with the introduction of virtual memory. 

In '80s, the most PCs had based on x86 CPUs and MS-DOS. Due to compatibility reason, the x86 Memory Model was designed around the concept of **segment**. This means that the address space was not uniform but was divided into 64KByte range known as **segment**. 

There was also an hard memory limit of 640 Kbytes for all the applications that ran under MS-DOS. In fact, the limit was 1 MB (20 bit used for address space), but some segments had reserved by the OS. So, the memory available for programmers was a bit more than 60% of the total.

Below a brief summary about the differences among **__near**, **__far**, and **__huge**:

- **__near**: a 16-bit pointer that can access any data in a range of 64K segment

- **__far**: a 32-bit pointer that contains a segment and an offset. However the object point to cannot be larger than 64K (in other words, it must be contained in one segment).

- **__huge**: a 32-bit pointer, with no one of the limitations mentioned above. This means that is possible access any data in the program's address space.

Choosing the right pointers to use was fundamental to increase application's performances. **Near pointers** were much faster than **far pointers** because no extra operations (combine the segment and the offset) is required to retrieve the data.

##Further Information

[The Intel Memory Model](http://en.wikipedia.org/wiki/Intel_Memory_Model)

[Expert C Programming: Deep C Secrets](http://www.amazon.co.uk/gp/search?index=books&linkCode=qs&keywords=9780131774292) by Peter van der Linden

[Stackoverflow.com: What is near, far and huge pointers?](http://stackoverflow.com/questions/3575592/what-is-near-far-and-huge-pointers)


