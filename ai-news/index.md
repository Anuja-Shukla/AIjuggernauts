---
layout: page
title: AI News
permalink: /ai-news/
---

<div class="cards">
{% for article in site.data.ai_news.articles %}
  <a class="card" href="{{ article.url }}" target="_blank" rel="noopener">
    <h3>{{ article.title }}</h3>
    <p>{{ article.date }}</p>
  </a>
{% endfor %}
</div>

<p style="color: var(--muted); font-size: 0.82rem; margin-top: 30px;">
  Headlines sourced from <a href="https://www.artificialintelligence-news.com/" target="_blank" rel="noopener">artificialintelligence-news.com</a>.
</p>
