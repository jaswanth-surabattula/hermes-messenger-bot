import feedparser
from src.processor import summarize_article
from src.processor import create_markdown_report
from src.cleanup import delete_old_reports

# A few tech RSS feeds for testing
FEEDS = [
    "https://news.google.com/rss/search?q=AI+news&hl=en-IN&gl=IN&ceid=IN:en"
]

def main():
    
    print("🗑️ Deleting files older than 14 days...")
    delete_old_reports(days=14)
    
    print("🚀 Hermes is fetching your news...")

    all_summaries = []
    
    for url in FEEDS:
        feed = feedparser.parse(url)
        # Just take the top 5 for now to save time
        for entry in feed.entries[:5]:
            print(f"\n--- Processing: {entry.title} ---")
            summary = summarize_article(entry.title, entry.description)
            print(f"Gemma says: {summary}")

            all_summaries.append({
                "title": entry.title,
                "summary": summary,
                "link": entry.link
            })

        report_path = create_markdown_report(all_summaries)
        print(f"✅ Briefing generated at: {report_path}")

if __name__ == "__main__":
    main()