---
layout: page
title: Articles
permalink: /articles/
---

<div class="cards">
{% for post in site.posts %}
  <a class="card" href="{{ post.url | relative_url }}">
    <h3>{{ post.title }}</h3>
    <p>{{ post.description | default: post.excerpt | strip_html | truncatewords: 20 }}</p>
  </a>
{% endfor %}
</div>
