---
layout: page
title: prisconapoli
tagline: ...the time has come to talk of many things
---
{% include JB/setup %}

{% if site.posts.first.style %}
  <link rel="stylesheet" href="/css/art-direction/{{ site.posts.first.style }}">
{% elsif page.style %}
  <link rel="stylesheet" href="/css/art-direction/{{ page.style }}">
{% endif %}

{% if site.posts.first.googlewebfonts %}
  <link href='http://fonts.googleapis.com/css?family={{ site.posts.first.googlewebfonts }}'>
{% elsif page.googlewebfonts %}
  <link href='http://fonts.googleapis.com/css?family={{ page.googlewebfonts }}'>
{% endif %}


<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Ads1 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-8829897225279483"
     data-ad-slot="2104974859"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>


## About the (damn) author 
Hi, my name is Prisco. I make software. In this blog you’ll find articles about my passions: **Maths**, **Physics** and **Computer Science**. Hope you’ll enjoy it! 

Wait wait wait!!! ... I know what someone of you is already thinking *"how could be this kind of blog enjoyable? Couldn't be better a cooking blog?"* 
 ... my dear readers, if I had decided to write a cooking blog, probably you follow the risk of die poisoned among the fourth and sixth post. So, for safety of you and your families, please settle of this :-) 

Don't worry... I promise that I'll not bore you too much.  Anyway, in any case, please keep in yours mind the phrase on the cover of [The Hitchhiker's Guide to the Galaxy](http://en.wikipedia.org/wiki/The_Hitchhiker%27s_Guide_to_the_Galaxy)  

<div style="text-align:center" markdown="1">
![]({{ site.url }}/assets/images/don_t_panic.jpg)
</div>


If someone of you is curious to know more about myself and my experience, feel free to contact me on [linkedin](http://ie.linkedin.com/in/prisconapoli/). 

So let's start... the time has come to talk of many things....

## Recent Posts

Take a look at my **last posts**:

<ul class="posts">
  {% for post in site.posts %}
    <li>
    <span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a>
    <p>{% if post.content contains '<!--more-->' %}
        {{ post.content | split:'<!--more-->' | first }}
    {% endif %}</p>
    </li>
  {% endfor %}
</ul>