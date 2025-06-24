# Jarvis – Python Voice Assistant

A modular Python-based voice assistant created by **Sumit Kumar Hota**, originally built as a CBSE 12th-grade final project and continuously improved through college. Jarvis handles real-time speech recognition, user authentication, media playback, weather/news scraping, system control, and dynamic voice interactions — all using customizable `.txt` configuration files.

## 👤 About the Developer

**Sumit Kumar Hota**  
B.Tech CSE Student, ITER, Siksha 'O' Anusandhan University, Bhubaneswar  
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

---

## 📁 Directory Structure

```
jarvis/
├── main.py
├── modules/                 # Python modules (auth, commands, etc.)
├── user voice input.py      # Profile voice sample recorder script
├── voice_profiles/          # Stores user .wav samples
├── config/                  # .txt files (eng_playlist, birthday, city, state, custom_commands, song_dir etc.) 
├── assets/                  # .mp4 demo file (jarvis demo.mp4)
├── requirements.txt
├── README.md
├── LICENSE
```

## 🎥 Demo

▶️ [Watch Jarvis Voice Assistant Demo (2:22)](./assets/Jarvis demo.mp4)

---

## 🛠️ How to Use

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. Add your '.wav' voice sample using the provided profile recorder script (user voice input.py)

3. Set up your '.txt' files:  
   - 'song_dir.txt', 'video_dir.txt' – directory paths to local files  
   - 'custom_commands.txt' – map commands to responses  
   - 'state.txt', 'city.txt' – for local news & weather  
   - 'birthday.txt' – your DOB in `DD-MM` format

4. Run 'main.py' and speak:  
   ```bash
   jarvis
   ```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Please do not re-upload or claim this work as your own. Learning from or contributing is welcome with credit.

---

> Made with 💻 by **Sumit Kumar Hota**  
> B.Tech CSE, ITER – Siksha 'O' Anusandhan University  
> Started in 12th grade | Actively maintained and improved during college
