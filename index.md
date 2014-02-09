---
layout: page
#title: prisconapoli
tagline: ...the time has come to talk of many things
---
{% include JB/setup %}

## About the (damn) author 
Hi, my name is Prisco Napoli. I make software. In this blog you’ll find articles about my three big passions: **Maths**, **Physics** and **Computer Science**. Hope you’ll enjoy it! 

Wait wait wait!!! ... I know what someone of you is already thinking *"how could be this kind of blog enjoyable? It couldn't be better a cooking blog?"* 
 ... my friends, if I had deciding to write a cooking blog, probably you follow the risk of die poisoned among the fourth and sixth post. So, for safety of you and your family, settle of this :-) 
 
## Recent Posts

Here's a list of the "last posts".

<ul class="posts">
  {% for post in site.posts %}
    <li>
        <span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a>
        <p>{{ post.excerpt }}</p>
    </li>
  {% endfor %}
</ul>



