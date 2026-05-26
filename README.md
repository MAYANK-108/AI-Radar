# 🎯 AI Radar

An AI-powered RSS feed scanner that automatically finds new AI tool launches, scores them using Groq AI, and sends real-time Telegram alerts.

## ✨ Features
- 📡 Monitors **3 RSS feeds** — TechCrunch AI, Hacker News, Product Hunt
- 🤖 Scores each article **1-10** using Groq AI (Llama 3.1)
- 🆓 Bonus points for **free & open source** tools
- 🚨 Sends **Telegram notifications** for scores 7+
- 🔐 Secure API key handling via `.env`

## 🛠️ Tech Stack
- **Python**
- **Groq API** — for AI-powered article scoring
- **feedparser** — for RSS feed parsing
- **Requests** — for Telegram notifications
- **python-dotenv** — for environment variable management

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/MAYANK-108/AI-Radar.git
cd AI-Radar
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API keys
Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

### 4. Run
```bash
python App.py
```

---

## 👨‍💻 Author
**Mayank** — BTech CSE Student
[GitHub](https://github.com/MAYANK-108)
