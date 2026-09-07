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

<p style="margin-top: 32px;">
  <strong>Faculty:</strong> use the
  <a href="{{ '/tools/simulation-creator.html' | relative_url }}">Simulation Creator</a>
  to generate a custom role-play prompt for your students.
</p>
