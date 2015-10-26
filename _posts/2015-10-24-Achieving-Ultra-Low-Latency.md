---
layout: post
category : Development
tags: [latency, high performance, financial trading]
image : latency/speed_latency.jpg
tagline: Computer scientists rely on speed to gain minuscule advantages in arbitraging price discrepancies in some particular security trading simultaneously on disparate markets - Low-latency strategies, Wikipedia

---
{% include JB/setup %}

**Learn what you need to build ultra low latency applications.**

<!--more-->
Is not a mystery that **Financial sector** is characterized by extreme competition among many firms and several execution venues. Every actor has different purposes and operates with different strategies. Hedge funds want to make trading at best price, while exchange venues try to attract market makers in their venues and put risk in their order book.

From an IT perspective, the financial sector is particularly interesting since the rate of technological change is incredibly high. To ensure advantages over competitors and increasing revenues, significant investments are continuously made on all technology stack.
To stay competitive, businessmen and IT leadership must learn new approaches, techniques, technologies and how to integrate them. Even customers, from their point of view, needs innovative tools for performance monitoring and troubleshooting.

The list below reports a short list of the most used technologies that have proved to be particularly valuable. They represents key-factors in any firm's technology that operates in the field of **high frequency trading**:

1. Low Latency Messaging
2. InfiniBand/ Gigabit Ethernet
3. Hardware Acceleration
4. Cache-Friendly Algorithms
5. Inter-Thread Communication
6. Shared-Nothing Architectures
7. Real-Time Analytics


The main factor on which firms continue to invest and sponsor research is that of *latency reduction*.
The **network latency* is, of course, the first thing that comes to mind when everyone talks about latency. 
However, another factor that is equally important in every high-performance financial application, is the *application latency*.

###Network latency
In a nutshell, is the inter-server latency. It largely depends on the technologies used to build the end-to-end path: network interfaces, cables, switches, routes, firewalls.

The most obvious solutions for latency reduction fall again in the route-optimizations category. It means replace copper cable with *optic fibers* (or even microwave towers), use network switches with very low latency (<2 microseconds), and route your data choosing the path which guarantees the shortest distance between the two endpoints and contains the least number of intermediate nodes. Moreover, technologies as Gibabit Ethernet or Infiniband are extremely successfull for improving *bandwith*, reducing *latency* and *jitter*.

Proximity and colocation are two further types of solutions adopted to reduce latency in financial applications. This solution could be particularly costly compared to an in-house data centers In a way, they represent the trend to move applications next to the data. In other words, firms put their servers in buildings next to an exchange's gateway, or inside the Exchange itself renting a space (called a *cage*). This explain another thread in the exchange's feature: they are becoming cloud providers.
It is a converse solution compare the way we used to think about application design, where programs run inside private data centes or in the cluod, and data is moved towards them.

Finally, it worth to mention some techniques used to reduce the time to process the network packets' header. The most known are the so-called *OS kernel bypass* and *TCP offload*. Before we see how they work, let's recall the great advantage of the protocol suite **TCP/IP** in terms of abstraction:  applications speak in terms of *sockets*, while networks speak in terms of *packets*. 

An application can ignore how to send packets, and the level that deals with packaging, routing and packets  delivery does not need to know data or what they will be used for.

The software libraries that implement the TCP/IP suite are traditionally implemented within the operating system (OS). Whether you use Linux, OSX or Windows, the OS is able to process network packet headers, remove all the extra payload must all'intradamento and data validation, and pass the payload application. However, this can have a non-negligible cost in applications that require very low processing times and suprattutto are very sensitive to latency. A call to a function of the operating system, the so-called system call, can have unpredictable results in terms of answers. In other words, if you are working on an ultra sensitive to latency, the operating system is an enemy. The **OS kernel bypass** is a tecnique used to bypass the kernel avoiding syscalls, and let an application to access data directly in the network interface buffer. In this way, there are not OS interruptions and the application can run very fast. The **TCP offload** consists in stripping off TCP/UDP header via hardware, generally inside the NIC itself. Also in this case, there is a significative improvement in performance for all the applications that process millions of packets per seconds.

###Application latency
It's about the latency that may arise between individual software components: processes, threads, functions and code blocks.

There are largely adopted principles or rule of thumbs in the traditional approach of application engineering: *abstractions*, *isolate software components from the machine*, *machines are cheap while developing time is expensive*, ecc.

In case of latency sensitive applications, the approach is totally different. The principle of software abstraction from the underlying machine is partly relaxed: here is necessary adopt a *machine-friendly* approach.
Deep knowledge about *CPU architectures*, *memory hierarchies*, *storage devices* technologies are becoming increasingly important to take advantage of the underlying hardware and ensure the maximum return in terms of performance.

There are many aspects able to affect application latency. Consider a software that has to process massive quantities of market data: this is typically burst traffic, so packets could arrive and then end up in a queue waiting to be processed. Message processing itself could slow down because of contention raised by several threads that compete to write a shared data, or lack of hardware resources like CPU time, storage and so forth. Moreover, the critical path could be interrupted by a syscall or an exception.

A pretty successfull approach adopted in the last years is the so-called *sharing nothing*. In a nutshell, applications are designed to **minimize the amount of data shared among threads** adopting multithreading techniques able to reduce the overall overhead for synchronization and the cost for thread creation/destruction.

Moreover, all data structures and algorithms are tuned in order to **maximise cache hit-rate**. Indeed, considering the speed of CPU and caches, is important to maximise the number of instruction/data accessess that have success and count how many failures happen. Every cache miss requires an extra access to memory or disk, and this causes delays and a kind if non-determinism that cannot be tolerated in some situations.

###Summary
At this point it should be pretty clear why financial firms hire the top specialists in programming languages, compilers and kernel optimizations, and hardware experts in CPU architectures, FPGA, file systems, and various technologies for data storage SSD, HHD, SAS, SATA.
The competition is extremely hard and require lots of expertise. If you're really interested in achieving *top performance*, this is the list to check:

- Adopt fast networking technologies: Gibabit Etherner or Infiniband
- Consider to use low latency network switch, proximity and colocation 
- Minimize network interface's processing time (e.g. FPA)
- OS kernel bypass/TCP offload
- Add batch processing to reduce costly operation
- Keep the working set in memory (hopefully inside the cache)
- Use specialised threads on the critical path, do the rest on other generic threads 
- Use dedicated core/cpu for critical threads
- Everything else on the other cores (not critical path)
- Minimize data sharing
- Do not share data among threads on the critical path and the others
- Use lock-free or wait free data structures
- Design to reduce contention
- Provide opportunities for concurrency
- Use advanced inter-thread communications pattern (e.g. Disruptor)
- Minimize syscalls (OS is an enemy)
