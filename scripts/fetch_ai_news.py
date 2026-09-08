"""
Fetches latest articles from artificialintelligence-news.com and writes them
to _data/ai_news.json for the Jekyll site to render.

Targets links matching /news/<slug>/ (the article URL pattern on this site)
while excluding known non-article paths (event listings, video hub, category
archives), since that's more stable across site redesigns than guessing
exact CSS classes.
"""

import json
import re
import sys
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

SOURCE_URL = "https://www.artificialintelligence-news.com/"
OUTPUT_PATH = "_data/ai_news.json"
MAX_ARTICLES = 20

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}

EXCLUDE_PATTERNS = [
    r"/news/event-type/", r"/news/videos", r"^/news/?$",
]


def is_article_link(href):
    if not href or "artificialintelligence-news.com" not in href:
        return False
    if not re.search(r"/news/[a-z0-9-]+/?$", href):
        return False
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, href):
            return False
    return True


def extract_articles(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = []
    seen_urls = set()

    for link in soup.find_all("a", href=True):
        href = link["href"]
        if not is_article_link(href):
            continue
        if href in seen_urls:
            continue

        title = link.get_text(strip=True)
        if not title or len(title) < 8:
            continue

        articles.append({
            "title": title,
            "date": "",
            "url": href,
        })
        seen_urls.add(href)

        if len(articles) >= MAX_ARTICLES:
            break

    return articles


def main():
    try:
        response = requests.get(SOURCE_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch source page: {e}", file=sys.stderr)
        sys.exit(1)

    articles = extract_articles(response.text)

    if not articles:
        print("No articles extracted — site structure may have changed. Keeping previous data.", file=sys.stderr)
        sys.exit(1)

    output = {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "source": SOURCE_URL,
        "articles": articles,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote {len(articles)} articles to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
