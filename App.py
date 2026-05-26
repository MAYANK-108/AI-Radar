import feedparser
import os
import requests
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

RSS_FEEDS = [
    "https://techcrunch.com/category/artificial-intelligence/feed/",
    "https://news.ycombinator.com/rss",
    "https://www.producthunt.com/feed",
]

def fetch_articles():
    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:  # top 5 from each feed
            articles.append({
                "title": entry.title,
                "summary": entry.get("summary", "No summary available"),
                "link": entry.link
            })
    return articles

def score_article(title, summary):
    prompt = f"""
You are an AI tool discovery expert.
Your ONLY job is to find NEW AI TOOLS or PRODUCTS that users can actually use.

Strict rules:
- A new AI tool/product launch = score 8-10
- If the tool is FREE with no subscription = add 2 points (max 10)
- If open source = add 1 point (max 10)
- Paid subscription only = subtract 1 point

Score 1-3 for ANY of these (hard rule, no exceptions):
- News about a company USING AI
- Research papers or academic articles
- Opinion pieces or analysis
- AI news that is NOT a tool you can go use right now

Article Title: {title}
Summary: {summary}

Reply with ONLY a number between 1 and 10. Nothing else.
"""
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        return int(response.choices[0].message.content.strip())
    except:
        return 0
    

def send_telegram(score, title, link):
    message = f"🚨 AI Radar Alert!\n\n⭐ Score: {score}/10\n📰 {title}\n🔗 {link}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})

def main():
    print("🔍 AI Radar scanning feeds...\n")
    articles = fetch_articles()
    print(f"Found {len(articles)} articles. Scoring with Groq...\n")
    
    hot_picks = []
    for article in articles:
        score = score_article(article["title"], article["summary"])
        if score >= 7:
            hot_picks.append((score, article))

    hot_picks.sort(reverse=True, key=lambda x: x[0])

    if hot_picks:
        print("🚨 HOT PICKS (Score 7+):\n")
        for score, article in hot_picks:
            print(f"⭐ Score: {score}/10")
            print(f"📰 {article['title']}")
            print(f"🔗 {article['link']}")
            print("-" * 50)
            send_telegram(score, article["title"], article["link"])
    else:
        print("😴 No hot AI tool news right now. Try again later.")

main()