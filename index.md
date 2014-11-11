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

<script type='text/javascript' src='http://ads.qadservice.com/t?id=b29179b6-d61e-42a9-857e-816c753fc539&size=728x90'></script>


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

<script type="text/javascript">
  ( function() {
    if (window.CHITIKA === undefined) { window.CHITIKA = { 'units' : [] }; };
    var unit = {"calltype":"async[2]","publisher":"prisconapoli","width":550,"height":250,"sid":"Chitika Default"};
    var placement_id = window.CHITIKA.units.length;
    window.CHITIKA.units.push(unit);
    document.write('<div id="chitikaAdBlock-' + placement_id + '"></div>');
}());
</script>
<script type="text/javascript" src="//cdn.chitika.net/getads.js" async></script>

<script type="text/javascript" >var qadserve_pid = "388de3ac-5a4e-46f4-b4f7-e7609400c46e";var qadserve_width = "728";var qadserve_height = "90";</script><script type="text/javascript"  src="http://mmrm.qadservice.com/qadserve_stayon.min.js"></script>
<script type="text/javascript" src="//cdn.chitika.net/getads.js" async></script> 

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