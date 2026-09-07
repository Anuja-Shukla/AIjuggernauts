---
layout: page
title: Faculty Jobs
permalink: /jobs/
---

<div class="cards">
{% for job in site.data.faculty_jobs.jobs %}
  <a class="card" href="{{ job.url }}" target="_blank" rel="noopener">
    <h3>{{ job.title }}</h3>
    <p>{{ job.date }}</p>
  </a>
{% endfor %}
</div>

<p style="color: var(--muted); font-size: 0.82rem; margin-top: 30px;">
  Listings sourced from <a href="https://www.facultyplus.com/" target="_blank" rel="noopener">facultyplus.com</a>.
  Always verify details directly with the hiring institution before applying.
</p>
