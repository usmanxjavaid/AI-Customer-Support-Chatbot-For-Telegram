# 🤖 AI Customer Support Chatbot for Telegram

An intelligent, production-ready customer support chatbot for Telegram powered by Groq (LLaMA 3) with HuggingFace as fallback. Built for small to medium businesses to automate customer support 24/7.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-supported-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 🧠 **AI Replies** — Powered by Groq (LLaMA 3) with HuggingFace as automatic fallback
- 💾 **Conversation Memory** — Remembers context within each session
- 📄 **Knowledge Base** — Reads client's PDF, Word (.docx), TXT files and websites automatically
- 🗄️ **Database** — Saves all users and conversations permanently in SQLite
- 📊 **Admin Panel** — View stats, users and conversation history via Telegram commands
- ⭐ **Feedback System** — Users can rate every response with 👍 👎
- 🛡️ **Rate Limiting** — Prevents spam and API abuse
- 🐳 **Docker Support** — Fully containerized for easy deployment
- ✅ **CI/CD** — GitHub Actions automatically tests Docker build on every push

---

## 📁 Project Structure

```
├── bot.py              → Telegram handlers and buttons
├── ai.py               → AI replies (Groq + HuggingFace fallback)
├── memory.py           → In-memory conversation history
├── faq.py              → Business knowledge loader
├── extractor.py        → Reads PDF, DOCX, TXT, websites
├── database.py         → SQLite database operations
├── admin.py            → Admin commands
├── rate_limiter.py     → Spam prevention
├── knowledge/          → Drop client files here
├── Dockerfile          → Docker configuration
├── .github/workflows/  → GitHub Actions CI
└── requirements.txt    → Python dependencies
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/usmanxjavaid/AI-Customer-Support-Chatbot-For-Telegram
cd AI-Customer-Support-Chatbot-For-Telegram
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
```env
TELEGRAM_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
ADMIN_ID=your_telegram_user_id
```

### 5. Add client knowledge files
Drop any of these into the `knowledge/` folder:
- PDF files (`.pdf`)
- Word documents (`.docx`)
- Text files (`.txt`)

Or pass a website URL in `bot.py`:
```python
faq.load(website_url="https://yourclient.com/faq")
```

### 6. Run the bot
```bash
python bot.py
```

---

## 🐳 Docker

### Build and run
```bash
docker build -t telegram-support-bot .
docker run --env-file .env telegram-support-bot
```

---

## 📊 Admin Commands

| Command | Description | Access |
|---|---|---|
| `/admin` | View total users, messages, feedback stats | Admin only |
| `/users` | List all registered users | Admin only |
| `/history [id]` | View conversation history of a user | Admin only |
| `/start` | Welcome menu with buttons | All users |
| `/reset` | Clear conversation history | All users |

---

## 🔑 API Keys (All Free)

| Service | Purpose | Get it |
|---|---|---|
| Telegram BotFather | Bot token | [@BotFather](https://t.me/botfather) |
| Groq | Primary AI (LLaMA 3) | [console.groq.com](https://console.groq.com) |
| HuggingFace | Fallback AI | [huggingface.co](https://huggingface.co) |

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Telegram Framework | python-telegram-bot 21.5 |
| Primary AI | Groq API (LLaMA 3.1) |
| Fallback AI | HuggingFace Inference API |
| Database | SQLite |
| Containerization | Docker |
| CI/CD | GitHub Actions |

---

## 📦 Per Client Customization

This bot is designed to be easily customized per client:

1. Get their bot token from [@BotFather](https://t.me/botfather)
2. Drop their business files into `knowledge/` folder
3. Update `.env` with their tokens
4. Deploy — done in under 30 minutes

---

## 📄 License

MIT License — feel free to use this project for commercial purposes.

---

## 👨‍💻 Author

**Usman Javaid**
- GitHub: [@usmanxjavaid](https://github.com/usmanxjavaid)