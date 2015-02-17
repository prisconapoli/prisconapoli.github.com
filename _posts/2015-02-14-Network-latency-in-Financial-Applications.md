---
layout: post
category : Financial-Trading
tags: [latency, networking,  TCP/IP, High Frequency Trading]
image : latency/latency.png
tagline: Nowadays, networks which carry financial data are monitored with the same diligence of changing market prices, correlations, and trends

---
{% include JB/setup %}

**Network latency: from physical fundamentals to engineering analysis**

<!--more-->

The emergence of **algorithmic trading industry** within the past few years is a telltale sign of the growing importance and demand for a fast delivery of financial data.

Market demand for **ultra low latency networking** is growing rapidly, pushed by Financial buying power to improve networks and applications. As example, consider what happened in early 2011. **Huawei** and **Hibernia Atlantic** began laying a fiber-optic link cable across the Atlantic Ocean to connect London to New York, with the sole goal of saving traders 5 milliseconds of latency by taking a shorter route between the cities, as compared with all other existing transatlantic links.
The cable was landed to be used by financial companies only, with a cost of over **$400M** to complete, which translates to **$80M** per millisecond saved.

Banks and financial institutions with algorithmic trading platforms are aware that a *small delay in trades could have a big impacts over profits*. Variability in network performance could drown out the sophistication of the trading algorithms. A small edge of a few milliseconds can translate to miillions in loss or profit. Nowadays, networks which carry financial data are monitored with the same diligence of changing market prices, correlations, and trends.


### Network Latency
The overall performance of a generic distributed application depends on hosts' processing time and time required to exchange data over the network. If we wxclude the hosts’ software processing at the source and destination end-points, the remaining **delay introduced by the network** is what is called **network latency**.

Latency can be measured either **one-way** (the time from the source sending a packet to the destination receiving it), or **round-trip** (which is the sum of the one-way latency from source to destination plus the one-way latency from the destination back to the source).

In algoritmic trading world, latency requirements are much stricter than for traditional web applications, such as VoIP, video conference or network gaming. As example, to enable good conversation quality, one-way latency in VoIP calls or video conference should not exceed 150 milliseconds. Interactive games typically require latencies between 100 and 1000 milliseconds depending on the game genre. However, while traditional applications can tolerate more than 100 milliseconds of one-way packet latency, high frequency trading, derivative pricing, and latency arbitrage are sensitive to milliseconds, microseconds, or less. **Low latency is a critical advantage for algorithmic trading platforms**. Excessive delays in executing trades are a disadvantage against competitors. Random jitter lowers the algorithmic predictability and reduces the potential profit. A trader which experiences 5 extra milliseconds in network latency, could be literally taken out of the market. As a consequence, has become more and more frequent to hear people in Financial Events which use expressions like "latency reduction" ans "latency monitoring".

It worth nothing that in computer networks, many users consider the **bandwidth** as the primary measure for network performance. Bandwith represents the **overall capacity of a connection** as the amount of data that can pass via it over a time period. It is measured in bits-per-second (bps), and is tipically an absolute value measured in isolation which depends only on the equipment.

Unlike bandwidth, latency and jitter are the indicator to consider in order to evaluate network performance. Unfortunately, they are very hard to characterize because they depend on the specific context of network topology and traffic conditions. 

Below is reported a simplistic description of the steps required to send a packet over a packet-switched network:

1. At sender side, an application that needs to send data to another application which run in another host, write this data using a socket API provided by the operating system.

2. The operating system packetizes the data and puts it in a memory buffer.

3. The network interface card encodes the bits in the memory buffer and transmits modulated signals over a cable to the next hop.

4. Network elements like switches, gateways, and routers forward the packet from hop to hop toward the receiving host.

5. At the receiving side, the signals reach the network interface card, where they are decoded, converted in bits and placed in a memory buffer.

6. The operating system de-packetizes the received data and puts it in a memory buffer.

7. The application gets access the received data via the socket API provided by the operating system.


###Physical fundamentals
In the previous paragraph we have introduced the concept of **network latency** saying that *it refers the delay between sending and receiving a message over a packet-switched network*. It is worth remembering that the overall application latency is comprised of the time to process messages at both the sending and receiving hosts (host latency) and the delays which occur inside the network (network latency).

In algoritmic trading, high speed and low latency requirements are driven by empirical results, as measured with respect to the bottom-line performance of financial businesses. The two critical components that dictate the performance of all network traffic are latency and bandwidth. To understand how to deliver data faster, we need to understand the many factors and fundamental limitations that are at play.


#### Speed of Light Barrier
As Einstein outlined in his **Theory of Special Relativity**, the **speed of light** is the *maximum speed at which all energy, matter, and information can travel*. According to the current understanding of Physics, the speed of light is considered a **fundamental constraint**. In a vacuum it is exactly **299,792,458 meters per second** (~300,000 kilometers per second, or 186,411 miles per second). 

**Einstein's observation places a hard limit on the propagation time of signals and, obviously, any network packet**. The speed of light tells how faster we can move a bit of data from one location to another. In other words, physics laws proved that is impossible to reduce network latency beyond a certain threshold. Neither the buying power of Banks nor equipment Vendors’ claims can alter this limit.

Nowadays, communication speed is pretty far from the speed of light. Because of the **physical construction** of the media, signals in fiber or copper cables can travel at roughly **~70%** of the speed of light, which is 210,000 kilometers per second. 

When a light signal travels through a transparent material it slows down due to the interaction with the electrons bound to the atoms in the material. The so called **refractive index** describes the slow down factor relative to vacuum (e.g. for glass it is between 1.3 to 1.5).

Similarly, when an electrical signal travels in a copper cable, it slows down due to the effects of **inductance**, **capacitance**, and **resistance** of the cable.

For long distance signal transmission, fiber cables are more efficient and economical than copper cables. It takes **~3.3 microseconds** in a vacuum for a signal to propagate 1 kilometer at the speed of light (1 kilometer divided by 300,000 kilometers per second). In a fiber optic cable it slows down to 70%, so the propagation delay for 1 kilometer is **~4.76 microseconds** (1 kilometer divided by 210,000 kilometers per second).


#### A little more about latency

Define latency *as the time a packet takes to travel from source to destination* is a simple and useful, but hides some useful details. Latency is indeed comprised by four components:

Propagation delay: amount of time required for a message to travel from the sender to receiver, which is a function of distance over speed with which the signal propagates.

Transmission delay: amount of time required to push all the packet’s bits into the link, which is a function of the packet’s length and data rate of the link.

Processing delay: qmount of time required to process the packet header, check for bit-level errors, and determine the packet’s destination.

Queuing delay: amount of time the incoming packet is waiting in the queue until it can be processed.

It worth mentioning the famous **infamous last-mile problem**. Frequently, is in the last few miles, not the crossing of oceans or continents, where significant latency is introduced.


###TCP Protocol
TCP protocol provides the **abstraction of a reliable network running over an unreliable channel**. It has been designed to be *adaptive* when network conditions change, to make an *efficient* use of the underlying network resources and to be *fair* with all nodes.  Despite TCP standard has continued to evolve during the last 30 year, the core principles and their implications remain unchanged:

• TCP packets are sequenced and delivered in order.

• TCP three-way handshake introduces a full roundtrip of latency.

• TCP slow-start is applied to every new connection.

• TCP flow and congestion control regulate throughput of all connections.

• TCP throughput is regulated by current congestion window size.


####Three-Way Handshake
The first main trait of TCP Protocol is that **all connections begin with a three-way handshake**. Before two processes can exchange any data, they must agree on starting packet sequence numbers, as well as a number of other connection specific variables, from both sides. For security reasons, sequence numbers are picked randomly from both sides, while connections variables depend on the TCP version implemented.

1. **SYN**: sender (or client) picks a random sequence number **xXX and sends a **SYN packet**, which could include additional TCP flags and options.

2. **SYN/ACK** receiver (or server)  increments **x** by one, picks a random sequence number **y**, appends its own set of flags and options, and send a response.

3. **ACK**: sender increments both **x** and **y** by one and completes the handshake by sending the last ACK packet in the handshake.

Once the three-way handshake is complete, applications' data can begin to flow. The client can send a data packet immediately after the ACK packet, and the server must wait for the ACK before it can dispatch any data. 

This startup process applies to every TCP connection and carries an important implication for performance of all network applications using TCP: **each new connection will have a full roundtrip of latency before any data can be transferred**.The delay imposed by the three-way handshake makes new TCP connections expensive to create, and is one of the big reasons why connection reuse is a critical optimization for any application running over TCP.

> The TCP handshake phase has been identified as a significant source of total web browsing latency, in large part due to the prevalence of very short TCP flows required to retrieve dozens to hundreds of assets from various hosts.
**TCP Fast Open* (TFO)** is a mechanism that aims to reduce the **latency penalty** imposed on new TCP connections. Based on traffic analysis and network emulation done at **Google Labs**, researchers have shown that TFO, which allows data transfer within the SYN packet, could decrease HTTP transaction network latency by 15%, wholepage load times by over 10% on average, and in some cases by up to 40% in high latency scenarios.


###Sensing the network's changes
TCP Protocol governs the rate with which applicatiions data can be sent in both directions through flow and congestion control.

####Flow Control
One of the big issue in digital communication is **how prevent the sender from overwhelming the receiver with data it may not be able to process**. This is not an unusual situation considering the finite amount of resource available. It could happen the receiver is busy, under heavy load, or may only be willing to allocate a fixed amount of buffer space.

To address this issue, TCP protocol requires that both sides **communicate the size** of the **available buffer space to hold the incoming data**. This parameter, called *receive window* (or *rwnd*), is sent in each ACK packet. 

If, for any reason, one of the sides is not able to keep up, then it can advertise a smaller window to the sender. A **zero receive window** is treated as a signal that **no more data should be sent** until the existing data in the buffer has been cleared by the application layer.

This workflow continues throughout the lifetime of every TCP connection: each ACK packet carries the latest rwnd value for each side, allowing both sides to dynamically adjust the data flow rate to the capacity and processing speed of the sender and receiver.


####Slow-Start
In the mid to late 1980, more and more computers start to be connected all around the world, and **network congestion collapse** starts to became a big issue. 

Despite **flow control** works pretty good to prevent the sender from overwhelming the receiver, it **does not prevent either side from overwhelming the underlying network**. Neither the sender nor the receiver know the available bandwidth at the beginning of a TCP connection, and hence they need a mechanism to estimate it and also adapt their speeds to the continuously changing conditions within the network.

**Slow-start** has been designed around the basic idea that *the only way to estimate the capacity between two nodes is to measure it by exchanging data*.
This is accomplished using a *congestion window*, or **cwnd**.
During the start of a TCP connection, both sides initialize their **cwnd**, which can vary along the connection's existence. To prevent network congestion, the maximum amount of data in flight (not ACKed) between the the hosts is the minimum of rwnd and cwnd variables.

It is worth mentioning that **cwnd** is not advertised or exchanged between the sender and receiver like **rwnd**, but is a private variable maintained by the hosts. The congestion window size is initially set to a conservative value, depending on the TCP version implemented by the Operting System. Originally, the **cwnd** starting value was set to 1 network segment. **RFC 2581** updated this value to a maximum of 4 segments, and most recently the value was increased once more to 10 segments by **RFC 6928**. Both sender and receiver determine the optimal values for their congestion window size starting slow and growing the window size as the packets are acknowledged. That's where the slow-start name comes from. The server can send up to **N** network segments to the client, at which point it must stop and wait for an acknowledgment. This phase of the TCP connection is commonly known as the “exponential growth” algorithm, as the client and the server are trying to quickly converge on the available bandwidth on the network path between them.

An obvious consequence of this fact is that **is not possibile use the full channel capacity immediately**, because of every TCP connection must go through the slow-start phase.

>One of the simplest ways to improve performance for all users and all applications running over TCP is to increasing the initial congestion window size on the server to the new RFC 6928 value of 10 segments.

TCP includes also a **slow-start restart (SSR)** mechanism, which resets the congestion window size after a connection has been idle for a defined period of time. The rationale is simple: the network conditions may have changed while the connection has been idle, and to avoid congestion, the window is reset to a *safe* value.


####Congestion Avoidance
TCP has been specifically designed to use packet loss as a **feedback mechanism** to help regulate its performance and get the best from the underlying communication channel.
A dropped packet allows the receiver and sender to **adjust the sending rates** and avoid overwhelming the network.

Slow-start initializes the connection with a conservative window and, for every roundtrip, doubles the amount of data in flight until it exceeds the receiver’s flow-control window, a system-configured congestion threshold window, or until a packet is lost, at which point the congestion avoidance algorithm takes over. In TCP, **Congestion avoidance** works with the implicit assumption that **a packet loss is indicative of network congestion**. Somewhere packets have encountered a congested link or a router, which was forced to drop the packet, and hence TCP need to adjust **cwnd** to avoid inducing more packet loss to avoid overwhelming the network.

Congestion avoidance addresses the issue of **how to grow congestion window size to minimize further loss in case the congestion window has been reset**. Indeed, at a certain point, another packet loss event could occur, and the process will repeat once over. Originally, TCP used the [Additive Increase/Multiplicative Decrease](http://en.wikipedia.org/wiki/Congestion_window) (AIMD) algorithm: when a packet loss occurs, halve the congestion window size, and then slowly increase the window by a fixed amount per roundtrip.
AIMD was too conservative in some circumstances, and hence a new algorithm called [Proportional Rate Reduction](research.google.com/pubs/pub37486.html)(specified by RFC 6937) has been developed by Google to improve the speed of recovery when a packet is lost. 

####Head-of-line blocking
In TCP connections, all packets are **sequenced and delivered in order**. A packet carries an **unique sequence number**, and the data must be passed  in-order to the application layer on the receiver side. If one packet is lost, then all subsequent packets must be held in the receiver’s TCP buffer until it is retransmitted and arrives at the receiver.
The application layer has **no visibility** about TCP retransmissions or queued packet buffers, because the **reassembly job is done entirely within the TCP layer**.
However, an application cannot process data until the full sequence has been received. This effect is known as **TCP head-of-line blocking**.

Head-of-line blocking has pro and con. It allows applications to avoid having to deal with **packet reordering** and **reassembly**, which *makes application design much simpler*. However, this is done at the cost of introducing **unpredictable latency variation** in the packet arrival times. This is commonly referred **jitter**, and can negatively impact the performance of the application.

####Spikes and Microbursts
At any time, only one packet can be transmitted from each physical output port of a switch.
If two or more packets arrive from separate input ports to the same output port at about the same time, a **resource contention might happen**.
Generally, when the output port is busy transmitting a packet, other packets are queued waiting their turn. This is another way in which head-of-line blocking phenomenon may occur 
along the route from source to destination. This effects **leads to inherent latency variations and jitter**, even at low traffic load.It could also happen for short periods of time that the instantaneous bandwidth reaches maximum utilization (~100%). These events, referred as **spikes** and **microbursts**, are a big issue to handle with because their effects is pushing an equipment to its operational limits, causing packets drops.


##UDP Protocol
We have seen that TCP ability to sense current network conditions and adapt its behavior is achieved via in-order delivery, retransmission of lost packets, flow and congestion controls, congestion avoidance. All combined, these features make TCP one of the most used transport protocol for distributed applications like email (SMTP), file transfer (FTP) and hypertext documents exchange (HTTP).

However, there are many kind applications that can deal with out-of-order delivery or packet loss, or that are very latency or jitter sensitive. These kind of applications like VoIP or video streaming, are better served with the [User Datagram Protocol](http://en.wikipedia.org/wiki/User_Datagram_Protocol) (UDP).
UDP was designed by **David P. Reed** and added to the core network protocol suite in 1980. 
A simple **connectionless transmission model** is used, with a minimum of protocol mechanism. Everithing is build around the concept of [datagram](en.wikipedia.org/wiki/Datagram), a **self-contained**, **independent entity of data** carrying *sufficient information to be routed from the source to the destination nodes without reliance on earlier exchanges between the nodes and the transporting network*. 

Looking at **UDP features**, is evident the great diversity from TCP protocol.

* No guarantee of message delivery

* No acknowledgments, retransmissions, or timeouts

* No guarantee of order of delivery

* No packet sequence numbers, no reordering, no head-of-line blocking

* No connection state tracking

* No connection establishment or teardown state machines

* No congestion control

* No built-in client or network feedback mechanisms

Indeed, TCP is a **byte-stream oriented protocol**, where application messages are spread across multiple packets without any explicit message boundaries within the packets themselves. To achieve this, every TCP connection hold a **connection state** allocated on both endpoints, and **each packet is delivered in order and retransmitted when lost**.

An UDP datagram, on the other hand, has boundaries because is carried in a single IP packet. An application read yields the full message because **datagrams cannot be fragmented**.

The appeal of UDP is not in what it introduces, but rather in all the features it omits. For this reason, UDP is colloquially referred to as a **null protocol**, because it has no handshake and datagrams are delivered via unreliable service, with no delivery guarantees and no failure notifications.

Due its simplicity, UDP is generally used for bootstrapping new transport protocols. 
Generally, an application which uses UDP has a more complex design, because of extra requirements: 

* must tolerate a wide range of Internet path conditions

* control rate of transmission

* perform congestion control over all traffic

* back off retransmission counters following loss

* not send datagrams that exceed path MTU

* handle datagram loss, duplication, and reordering


##Summary
In this post I introduced the basic features of both UDP and TCP protocols.
Understand how these protocols work is the first step to understand how a network is performing and what actions we can do to improve it.
Nowaday, there is a huge demand for ultra low latency networking in algorithmic trading world. Indeed, excessive delays in trades execution are a disadvantage against competitors. Latency and random jitter lowers the algorithmic predictability and reduces the profit potential. Latency and jitter are not easy to monitor because they vary with actual network topology and traffic conditions.


##Further Information
[socket](https://docs.python.org/2/library/socket.html), Low-level networking interface

[TCP](http://en.wikipedia.org/wiki/Transmission_Control_Protocol), Transmission Control Protocol

[UDP](en.wikipedia.org/wiki/User_Datagram_Protocol), User Datagram Protocol

[Latency](http://en.wikipedia.org/wiki/Latency_(engineering)), Wikipedia, the free encyclopedia

[High Performance Browser Networking](shop.oreilly.com/product/0636920028048.do), by Ilya Grigorik

[Pragmatic Network Latency Engineering Fundamental Facts and Analysis](http://www.cpacket.com/download/Introduction%20to%20Network%20Latency%20Engineering.pdf), by Rony Kay


