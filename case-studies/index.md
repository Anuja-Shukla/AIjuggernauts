---
layout: page
title: Case Studies
permalink: /case-studies/
---

<div class="cards">
{% for cs in site.case_studies %}
  <a class="card" href="{{ cs.url | relative_url }}">
    <h3>{{ cs.title }}</h3>
    <p>{{ cs.description | default: cs.content | strip_html | truncatewords: 20 }}</p>
  </a>
{% endfor %}
</div>
