---
layout: page
title: Simulations
permalink: /simulations/
---

<div class="cards">
{% for sim in site.simulations %}
  <a class="card" href="{{ sim.url | relative_url }}">
    <h3>{{ sim.title }}</h3>
    <p>{{ sim.description }}</p>
  </a>
{% endfor %}
</div>
