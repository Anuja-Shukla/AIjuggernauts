---
layout: page
title: Upcoming Conferences
permalink: /conferences/
---

<p style="color: var(--muted); margin-bottom: 8px;">
  Data pulled from <a href="{{ site.data.conferences.source }}" target="_blank" rel="noopener">conferencealerts.in</a>,
  refreshed automatically once a day. Last updated: {{ site.data.conferences.updated_at }}.
</p>

<div class="cards">
{% for event in site.data.conferences.events %}
  <a class="card" href="{{ event.url }}" target="_blank" rel="noopener">
    <h3>{{ event.title }}</h3>
    <p>{{ event.date }}{% if event.location %} &middot; {{ event.location }}{% endif %}</p>
  </a>
{% endfor %}
</div>
