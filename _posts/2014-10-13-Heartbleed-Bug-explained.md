---
layout: post
category : Security
tags: [Heartbleed, OpenSSL, TLS]
image : heartbleed-explained/heartbleed.png
tagline: My primary goal of hacking was the intellectual curiosity, the seduction of adventure - Kevin Mitnick
---
{% include JB/setup %}

**It's easy to understand the Heartbleed bug**

<!--more-->

One of the most important bugs discovered this year is the **Heartbleed bug**. The bug affects the OpenSSL cryptography library, which is a widely used implementation of the Transport Layer Security (TLS) protocol.

In jargon, this kind of vulnerability is classified as a **buffer over-read**, which means that a software allows more data to be read than should be allowed. 

Surfing in the Web I found a nice picture which explains in a very understandable way what are the effects of this bug.  
<!--summary-->

<div style="text-align:center" markdown="1">
![How the Heartbleed works]({{ site.url }}/assets/images/heartbleed-explained/heartbleed-explained.jpg)
</div>

#####How the Heartbleed bug works, credits http://xkcd.com/1354

##Further Information

[Heartbleed](http://en.wikipedia.org/wiki/Heartbleede), Wikipedia.org

[OpenSSL](http://en.wikipedia.org/wiki/OpenSSL), Wikipedia.org

[TLS](http://en.wikipedia.org/wiki/Transport_Layer_Security), Wikipedia.org