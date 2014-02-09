---
layout: page
#title: prisconapoli
tagline: ...the time has come to talk of many things
---
{% include JB/setup %}

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



