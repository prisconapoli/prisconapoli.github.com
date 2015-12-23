---
layout: post
category : Development
tags: [C++, C++11, concurrency, multithreading]
image : concurrency/polar_bear.jpg
tagline: We have to fight chaos, and the most effective way of doing that is to prevent its emergence - Edsgar Dijkstra.

---
{% include JB/setup %}

**Design to maximise opportunities for concurrency**
<!--more-->

This post is intended for giving a brief review on the different approaches in the design of data structures for concurrent programming.

I saw many times a bit of confusion in people involved in the development of concurrent programs. It's hard to be fully aware on the complexity of this topic, the variety of possible tools available and the possible approach to develop customised solutions. Understand the power of concurrent programming is a key to maximize  performance on modern software systems.

Let's begin explaining a fundamental concept in concurrent programming: *thread safety*. A data structure is said to be *thread safe* when the following properties are all achieved:

- concurrent access is supported
- there is always a self consistent view
- no data lost
- no data corruption
- no race conditions
- no invariants violation

**Guarantee the thread safety is only a part of the entire design process. Equally important is the need to ensure a genuine concurrent access for all threads**.

In particular, the *access serialization* on the data strucure is commonly achieved through the adoption of **mutex**. By their true nature, the word *mutex* stands for *mutual exclusion*. That is, a mutex is used to protect the access to a data structure or a specific part of the code. When the mutex is *locked*, only one thread can advance, i.e. use the data structure for a specific purpose, while everyone else that need use the same data structure is forced to wait. More threads are waiting, less faster is the system. For these reasons, it is essential that a good design will take care of this behaviour and try to **limit as much as possible the region of data to protect**.

Serialize the minimum amount of operations is the first thing to look at in order to improve overall performance. Any operation that does not require exclusive access should be done without locking a mutex, so as to allow other threads to progress without waiting. Lock granularity impacts the potential of true concurrent. Every time you design a data structure for a concurrent program, remember that a good design must be addressed to **identify the best opportunities for concurrent access**.

##Lock-Based
The easiest and largely adopted way is design *lock-based* data structures. This name comes from *lock*, a high-level data structure used to implement the mechanism of **mutual exclusion**. The design steps for a lock-based data structure can be summarized in the following sentence: *ensure that the correct mutex is locked when a data structure shared among several threads is accessed, and ensure it is locked for the shortest time possible*.

The use of mutex is not sufficient to guarantee a *safe access*. Much attention should be taken when designing interfaces. An interface should represent comprehensive operations and not operational steps. Also, it shouldn't return any hook to shared data, nor directly nor indirectly. Even the definition of simple operations such as constructors, destructors, and copy assignment operator can hide pitfalls in the context of multi-threaded programming.

In addition, everytime the use of many locks is required, we can experience the unpleasant effect of **dead-lock**. Also exception handling require much more care compared to a single thread program. An unexpected behaviour can lead to the violation of invariants and leave the data structure in an inconsistent state.

In general, we can say that a data structure which uses a mechanism such a **mutex**, **condition variables** or **future**, is classified as a blocking data structure. In this context, the word blocking means that only one thread can make progress while others are stuck waiting for the release of the mutex.
Another aspect to keep in consideration because can have a huge impact on performance, is that this approach may involve the use of blocking calls, e.g. system calls A system call can have **unpredictable effects** in terms of response time. Not surprisingly, in every high-performance system, the operating system is seen as an *hostile environment*, because the mechanism for allocating resources are not predictable. When a thread is awakened and passes from the wait-queue to the ready-queue, it can be stopped waiting because the operating system has in the meantime decided to run another process.


##Non blocking
As the name suggests, the data structure is designed so as not to require the use of any blocking call. From a practical standpoint, the easiest way is to use *spin-lock*. This technique, however, has the disadvantage of wasting CPU cycles and, as a consequence, lead to another common problem in concurrent programming: **starvation**.

##Lock-free
Let's begin clarifying that saying a data structure is lock-free is not equivalent to *a data structure that does not use lock*. In my opinion, a better expression that best describes the essence of this tecnique is *mutual-exclusion free*. In fact, a data structure is said to be lock-free *if, at any time, several threads (at least two) can make progress in their execution*. Obviously, these threads can do both the same or different operations. As example, consider the shared mutex in Boost library. A thread can use a **read** mutex to declare its willingness to access the data structure in reading mode. Obviously, every time a write operation is necessary, there is no other way than to have exclusive access or use the transactional model, e.g. try to write the data and verify that in the meantime there have been changes. The use of lock-free data structures guarantees an increase of the overall degree of concurrency obtainable within a system and improves the robustness in case of exceptions. Also, lock-free data structures have the advantage of being dead-lock free, although live-lock is always possible. The design of a lock-free data structure requires great care and experience. From a practical point of view,  gerenally the CAS operation are largely used. It should be noted that a CAS operation may have a significant cost on certain type of architectures (e.g. old ARM), while is almost free on others (e.g. x64). In other words, is not always true that use a lock-free data structure corresponds to an improvement in terms of the overall performance. On modern CPUs, system performance may be subject to a further deterioration due to CPU architecture. Because the adoption of multi-level caching, a bad designed data structure can lead to phenomena such as cache ping-pong, which is triggered by false sharing. For those interested in this topic, I'd suggest to read my previous article on C++ memory models, within is possible find a quick overview of a modern CPU architecture and a description of false sharing.

##Wait-free
*Wait-free* data structures are the most interesting and at the same time the most complicated to design. They ensure that all threads complete their task in a finite number of steps. In other words, they behaviour is completely deterministic.
These structures are a very powerful tool in concurrent programming: *is the entire system and not just few threads that has the ability to proceed forward*.
However, from a design standpoint, develop a wait-free data structure is a very complex task. A new wait-free data structure as queue, stack or hash-map is certainly a remarkable work worthy of publication. Wait-free structures do not suffer nor dead-lock nor live-lock. However, in some case there could be an overall performance decrease because of cache ping-pong.

##Further Information

[C++ Concurrency in Action: Practical Multithreading](http://www.amazon.com/C-Concurrency-Action-Practical-Multithreading/dp/1933988770), by Anthony Williams

[Foundations of the C++ Concurrency Memory Model](http://rsim.cs.illinois.edu/Pubs/08PLDI.pdf), by H.Boehm, S.Adve

[Memory model for multithreaded C++](http://www.hboehm.info/c++mm/mmissues.pdf), by Hans-J. Boehm
