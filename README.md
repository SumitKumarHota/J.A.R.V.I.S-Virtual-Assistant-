# Jarvis – Python Voice Assistant

A modular Python-based voice assistant created by **Sumit Kumar Hota**, originally built as a CBSE 12th-grade final project and continuously improved through college. Jarvis handles real-time speech recognition, user authentication, media playback, weather/news scraping, system control, dynamic voice interactions, and AI-powered Q&A — all using customizable `.txt` configuration files.

## 👤 About the Developer

**Sumit Kumar Hota**\
B.Tech CSE Student, ITER, Siksha 'O' Anusandhan University, Bhubaneswar\
Currently entering 3rd year (5th semester)

---

## 🚀 Key Features

- 🔐 Multi-user voice authentication via recorded `.wav` profiles
- 🎵 Local music/video playback with custom search fallback to YouTube
- 📁 Auto-generated playlists (`hindi.txt`, `english.txt`, `mix.txt`) for random playback
- 🌐 Voice-activated web search (Google, YouTube, Wikipedia)
- 💬 Custom command-to-response via `custom_commands.txt` with multiple randomized responses
- 📅 Time-based greetings + birthday wish (uses `birthday.txt` + system date)
- 🌤️ Location-based news & weather (via web scraping with `state.txt`, `city.txt`)
- 📂 Voice-based app launcher using file paths defined in `.txt` files
- 🗑️ System utilities: empty recycle bin, shutdown, restart, sign out, close apps
- 🌍 Location finder: open earth.google.com with specific landmarks
- 🌐 Web access to Gmail, Instagram, WhatsApp, YouTube, Facebook, Spotify, Discord, Maps, Drive, and more
- 📡 Smart startup: retries internet connection 3 times before exit if offline
- 🤖 AI fallback via the free Groq API — say "Jarvis" then ask any question not covered by a predefined command

---

## 📁 Directory Structure

```
jarvis/
├── main.py
├── groq_api_key_input.py    # Double-click to enter/save your Groq API key
├── modules/                 # Python modules (auth, commands, ai_qa, etc.)
├── user voice input.py      # Profile voice sample recorder script
├── voice_profiles/          # Stores user .wav samples
├── config/                  # .txt files (birthday, city, state, custom_commands, song_dir, groq_key etc.)
├── assets/                  # .mp4 demo file (jarvis demo.mp4)  
├── requirements.txt
├── README.md
├── LICENSE.txt
```

## 🎥 Demo

▶️ [Watch Jarvis Voice Assistant Demo (2:22)]\(./assets/Jarvis demo.mp4)

---

## 🛠️ How to Use

### ✅ Step 1: Install Required Dependencies

Make sure Python is installed. Then:

1. Open the folder that contains this project (where `requirements.txt` is located).

2. Click the folder's address bar and type `cmd`, then press **Enter** to open Command Prompt.

3. Before running pip, you may need to install C++ build tools required by some packages (e.g., `resemblyzer`):

   **⚙️ Prerequisites for Resemblyzer and Other Native Extensions**

   1. Download and install **Visual Studio Build Tools 2022** (with Windows 11 SDK):
      - Visit: [https://visualstudio.microsoft.com/vs/preview/#download-preview](https://visualstudio.microsoft.com/vs/preview/#download-preview)
      - Click **“Download Preview”** for **Visual Studio Community**.
   2. In the installer, select the following components:
      - ✅ **MSVC v143 – VS 2022 C++ x64/x86 build tools (Latest)**
      - ✅ **Windows 11 SDK (10.0.26100.3916)**
      - ✅ **C++ CMake tools for Windows**
      - ✅ **C++ ATL for latest v143 build tools (x86 & x64)**
      - ✅ **C++/CLI support for v143 build tools (Latest)**

4. Now run:

   ```bash
   pip install -r requirements.txt
   ```

📌 This installs all necessary modules — like `speechrecognition`, `pyttsx3`, `resemblyzer`, `groq`, etc.

💡 If `pip` isn’t recognized, try:

```bash
python -m pip install -r requirements.txt
```

### ✅ Step 2: Set Up Configuration Files

Inside the `config/` folder:

- `custom_commands.txt` – define your custom voice commands and responses
- `song_dir.txt`, `video_dir.txt` – add full directory paths to your local media folders
- `state.txt`, `city.txt` – for news and weather scraping
- `birthday.txt` – your birthdate in `DD-MM` format
- `groq_key.txt` – your free Groq API key, generated automatically the first time you run `groq_api_key_input.py` (see [AI Fallback](#-ai-fallback-groq) below)

Also:

- Add your voice profiles in `voice_profiles/` using the recorder script `user voice input.py`.

### ✅ Step 3: Run Jarvis

Launch Jarvis with:

```bash
python main.py
```

Say **"Jarvis"** to activate and give commands like:\
🕒 "What time is it?"\
🎶 "Play Faded"\
🌤️ "What’s the weather?"\
📺 "Play video XYZ"\
📚 "Search dogs on Wikipedia"

---

## 🤖 AI Fallback (Groq)

If you say **"Jarvis"** first (to activate, as usual), then ask something that isn't one of the fixed commands above — e.g. "what is the capital of France", "why is the sky blue", "how do planes fly" — it's automatically answered by an LLM through the free [Groq API](https://console.groq.com/keys), spoken back through the same text-to-speech engine.

**Setup:**
1. Get a free API key from [console.groq.com/keys](https://console.groq.com/keys).
2. Double-click `groq_api_key_input.py` (or run `python groq_api_key_input.py`) and paste your key when prompted. It's saved locally to `config/groq_key.txt` (git-ignored, never uploaded anywhere).

That's it no other setup needed. If no key has been saved yet, Jarvis will let you know once via voice instead of failing silently.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).\
Please do not re-upload or claim this work as your own. Learning from or contributing is welcome with credit.

> Made with 💻 by **Sumit Kumar Hota**\
> B.Tech CSE, ITER – Siksha 'O' Anusandhan University\
> Started in 12th grade | Actively maintained and improved during college
