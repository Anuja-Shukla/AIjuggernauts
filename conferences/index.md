---
layout: page
title: Upcoming Conferences
permalink: /conferences/
---

<div class="cards">
{% for event in site.data.conferences.events %}
  <a class="card" href="{{ event.url }}" target="_blank" rel="noopener">
    <h3>{{ event.title }}</h3>
    <p>{{ event.date }}{% if event.location %} &middot; {{ event.location }}{% endif %}</p>
  </a>
{% endfor %}
</div>
