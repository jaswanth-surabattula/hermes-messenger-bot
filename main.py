import feedparser
from src.processor import summarize_article

# A few tech RSS feeds for testing
FEEDS = [
    "https://news.google.com/rss/search?q=AI+news&hl=en-IN&gl=IN&ceid=IN:en"
]

def main():
    print("🚀 Hermes is fetching your news...")
    
    for url in FEEDS:
        feed = feedparser.parse(url)
        # Just take the top 3 for now to save time
        for entry in feed.entries[:3]:
            print(f"\n--- Processing: {entry.title} ---")
            summary = summarize_article(entry.title, entry.description)
            print(f"Gemma says: {summary}")

if __name__ == "__main__":
    main()