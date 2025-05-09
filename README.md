# 🤖 Chatur – Your AI-Powered Voice Assistant

**Chatur** is a Python-based, voice-activated virtual assistant that mimics smart assistants like Alexa and Google Assistant. It uses cutting-edge AI models (OpenAI GPT-4 and Google's Gemini Pro) to have intelligent conversations and perform real-world tasks via simple voice commands.

---

## 🌟 Features

* 🗣️ **Wake Word Activation**: Listens for the keyword **"Chatur"** to activate.
* 💬 **Smart Conversations**: Uses **OpenAI GPT-4** or **Google Gemini Pro** for contextual answers.
* 🌐 **Web Browsing**: Opens popular websites (Google, YouTube, Facebook, LinkedIn, GitHub) on command.
* 📰 **News Headlines**: Fetches and reads latest news from **NewsAPI**.
* 🎵 **Music Playback**: Plays songs from a custom music library with the "play \[song]" command.
* 🔊 **Text-to-Speech Output**: Speaks responses using `gTTS` or `pyttsx3`.
* ♻️ **Continuous Listening**: Waits for commands after activation in real-time.

---

## ⚙️ Tech Stack

* Python 3.x
* `speech_recognition`
* `pyttsx3`, `gTTS`, `pygame`
* `openai`, `google.generativeai`
* `webbrowser`, `requests`
* `NewsAPI`

---

## 🚀 How It Works

1. The assistant continuously listens for the wake word **"Chatur"**.
2. Once activated, it listens for your next voice command.
3. Executes specific tasks (open sites, play music, fetch news) or passes general queries to GPT-4/Gemini.
4. Speaks the AI-generated response out loud.

---

## 🔐 Setup & API Keys

You will need:

* **OpenAI API Key** – For GPT-based responses
* **Google API Key** – For Gemini Pro model
* **NewsAPI Key** – For fetching live headlines

Set these securely as environment variables:

```bash
export OPENAI_API_KEY="your-openai-key"
export GOOGLE_API_KEY="your-google-api-key"
export NEWS_API_KEY="your-newsapi-key"
```

---

## 📅 Sample Voice Commands

* "Chatur, open Google"
* "Chatur, play Alan"
* "Chatur, what is AI?"
* "Chatur, tell me the news"

---

## 🔧 Future Improvements

* Add support for calendar events
* Integration with email and file systems
* GUI interface

---

## ✉️ Contact
Created by **Jay Dhodi**  
🔗 [GitHub](https://github.com/jaydhodi09)  
🔗 [LinkedIn](https://www.linkedin.com/in/jaydhodi14/)

---

> “Chatur, smarter than ever. Your voice, your assistant.”
