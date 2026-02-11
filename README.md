# hermes-messenger-bot
### AI News Curator & Orchestrator (LLMOps)
Serverless AI News Curator: A daily LLMOps digest bot using local LLMs for intelligent summarization and Telegram for delivery. Automated via GitHub Actions. The personal intelligence engine that aggregates high-signal AI news from YouTube, Medium, and ArXiv, summarizes them using local LLMs (Llama 3.2), and delivers a daily digest via Telegram.

## 🚀 Developments So Far
- **Project Architecture:** Implemented a modular `src/` structure to decouple scrapers from processing logic.
- **Environment Setup:** Configured a secure `.venv` virtual environment and `.env` for credential management.
- **Data Ingestion:** - Integrated **YouTube Data API v3** for creator-specific monitoring.
  - Built a **Universal RSS Scraper** for Medium and technical blogs.
  - Prepared **ArXiv** integration for research paper tracking.

## 🛠️ Tech Stack
- **Language:** Python 3.12+
- **APIs:** YouTube Data API, Telegram Bot API
- **Libraries:** `feedparser`, `python-dotenv`, `google-api-python-client`
- **Infrastructure:** GitHub Actions (Planned for automation)

## 📦 Project Structure
```text
ai-news-curator/
├── src/
│   ├── scrapers/          # Source-specific scraping logic
│   ├── processor.py       # LLM summarization engine (Pending)
│   └── telegram_bot.py    # Notification delivery
├── .env                   # Secrets (Not committed)
└── main.py                # Core orchestrator
```