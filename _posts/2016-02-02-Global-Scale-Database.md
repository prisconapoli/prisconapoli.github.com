---
layout: post
category : Development
tags: [spanner, distributed, database, google, scalability, external consistency]
image : mind_maps/spanner/cover.jpg
tagline: I’m an old guy. Megabytes were big things. But when I came to Google, I had to add another three zeros to all my numbers - John Wilkes, Google.
---
{% include JB/setup %}

**Spanner: Google's global distributed database**

<!--more-->

[Google's Spanner](http://research.google.com/archive/spanner.html) is a distributed storage system project that for the first time has solved the issue of externally consistent transactions at global scale. It provides global distribution and replication of data to provide both high availability and to minimize latency of data reads and writes.

Google's engineers have made an amazing job. They have created a virtual global *wall clock*, called *TrueTime*, which is used by the system to ensure the global transactions order.
*TrueTime* exposes the uncertainty in the clock by representing time as an interval.

To get more insights and architecture details, I strongly recommend to read [Google's paper]((http://research.google.com/archive/spanner.html)) and watch this Youtube video [Spanner: Google's Globally-Distributed Database](https://www.youtube.com/watch?v=NthK17nbpYs) by Wilson Hsieh

<div style="text-align:center" markdown="1">

<b>Mind map: Spanner DB</b>([download]({{ site.url }}/assets/images/mind_maps/spanner/spanner_big.png))
<br>    
![]({{ site.url }}/assets/images/mind_maps/spanner/spanner_small.jpg "Spanner DB")

</div>
