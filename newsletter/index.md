---
layout: page
title: AI Newsletter
permalink: /newsletter/
---

<p style="color: var(--muted); margin-bottom: 8px;">Past issues of the AIjuggernauts newsletter — practical AI updates for educators and trainers.</p>

<div class="cards">
{% assign issues = site.newsletter | sort: "date" | reverse %}
{% for issue in issues %}
  <a class="card" href="{{ issue.url | relative_url }}">
    <h3>{{ issue.title }}</h3>
    <p>{{ issue.date | date: "%B %-d, %Y" }}{% if issue.description %} &middot; {{ issue.description }}{% endif %}</p>
  </a>
{% endfor %}
</div>
