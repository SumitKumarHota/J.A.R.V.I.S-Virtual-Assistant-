import os
import webbrowser
import wikipedia
import pywhatkit as kt
import pyjokes
from pytube import YouTube
from pathlib2 import Path
import csv
import random
import datetime
import subprocess
import winshell

from modules.speech_engine import speak
from modules.system_utils import low_vol, high_vol
from modules.news_reader import india_news, covid_india, covid_world, science_news, business_news, sports_news, world_news, state_news, city_news, latest_news, gadget_news, politics_news, crazy_news
from modules.weather_checker import temperature, weather
from modules.system_utils import tellDay, tellTime, tellDate

def birthday():
    try:
        sample = []
        birth_date = ""
        with open("config/birthday.txt", "r") as f:
            a = f.readlines()
            for i in a:
                sample.append(i)
            for i in sample:
                birth_date += i
        dm = birth_date[5:10]
        today_date = str(datetime.datetime.now())
        dm2 = today_date[5:10]
        if dm == dm2:
            speak("and Happy Birthday")
    except:
        print("")

def wishMe(name):
    hour = datetime.datetime.now().hour
    greeting = ""

    if hour >= 0 and hour < 12:
        greeting = "Good Morning"

    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon"

    else:
        greeting = "Good Evening"

    speak(f"{greeting}")
    speak(name)

from modules import user_data

def handle_command(query):
    query = query.lower()
    print("Waiting for command...")
    print(f"Query detected: {query}")

    matched = False

    try:
        with open('config/custom_commands.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    command, responses = line.strip().split(':', 1)
                    if query == command.strip().lower():
                        options = [r.strip() for r in responses.split('|') if r.strip()]
                        if options:
                            speak(random.choice(options))
                            matched = True
                            return
    except Exception as e:
        print(f"Error reading custom_commands.txt: {e}")
        speak("Custom command unavailable.")

    if matched:
        return

    if "jarvis" in query:
        wishMe(user_data.name)
        speak("How may I assist you?")
        return

    if "lower volume" in query or "lower the volume" in query or "volume down" in query:
        low_vol()

    elif "increase volume" in query or "increase the volume" in query or "volume up" in query:
        high_vol()

    elif query=="youtube":
        speak("Opening Youtube")
        webbrowser.open_new_tab("https://www.youtube.com/")

    elif "indian covid news" in query or "covid india" in query or "coronavirus india" in query:
        covid_india()

    elif "world covid news" in query or "covid world" in query or "coronavirus world" in query:
        covid_world()

    elif "india news" in query:
        india_news()

    elif "science news" in query:
        science_news()

    elif "business news" in query:
        business_news()

    elif "sports news" in query:
        sports_news()

    elif "world news" in query or "international news" in query:
        world_news()

    elif "state news" in query:
        state_news()

    elif "city news" in query:
        city_news()

    elif "latest news" in query or "news headlines" in query:
        latest_news()

    elif "gadget news" in query:
        gadget_news()

    elif "politics news" in query:
        politics_news()

    elif "crazy news" in query or "mad news" in query:
        crazy_news()

    elif "temperature" in query:
        temperature()

    elif "weather" in query:
        weather()

    elif 'system shutdown' in query:
        speak("Initiating system shutdown in T-minus 5 seconds. 5 . 4 . 3 . 2 . 1 . 0")
        os.system("shutdown /s /t 1")

    elif "system reboot" in query or "restart" in query:
        speak("Initiating system reboot in T-minus 5 seconds. 5 . 4 . 3 . 2 . 1 . 0")
        os.system("shutdown /r /t 1")

    elif "log off" in query or "sign out" in query:
        speak("Initiating system sign out in T-minus 5 seconds. 5 . 4 . 3 . 2 . 1 . 0")
        os.system("shutdown -l")

    elif "where is" in query:
        query=query.replace("where is ","")
        location=query
        webbrowser.open("https://earth.google.com/web/search/"+location)
        speak("Location found")

    elif 'empty recycle bin' in query:
        speak("Emptying recycle bin")
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)

    elif "which day is it" in query or "what day is it" in query:
        tellDay()

    elif "what time is it" in query or "what's the time" in query:
        tellTime()

    elif "date" in query:
        tellDate()

    elif 'search' in query:
        query=query.replace("search", "")
        speak("Searching for"+query)
        kt.search(query)

    elif "from youtube" in query:
        query=query.replace("from youtube", "")
        speak("Searching for"+query)
        kt.playonyt(query)

    elif "joke" in query:
        speak(pyjokes.get_joke())

    elif "wikipedia" in query:
        try:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=4)
            speak("According to Wikipedia")
            speak(result)
        except wikipedia.exceptions.PageError:
            speak("No result found")

    elif query=='google':
        speak("Opening Google")
        webbrowser.open_new_tab("www.google.com")

    elif "instagram web" in query or "instagram online" in query:
        speak("Opening Instagram")
        webbrowser.open_new_tab("https://www.instagram.com/")

    elif "whatsapp web" in query or "whatsapp online" in query:
        speak("Opening Whatsapp")
        webbrowser.open_new_tab("https://web.whatsapp.com/")

    elif "reddit web" in query or "reddit online" in query:
        speak("Opening Reddit")
        webbrowser.open_new_tab("https://www.reddit.com/")

    elif "facebook web" in query or "facebook online" in query:
        speak("Opening Facebook")
        webbrowser.open_new_tab("https://www.facebook.com/")

    elif "discord web" in query or "discord online" in query:
        speak("Opening Discord")
        webbrowser.open_new_tab("https://discord.com/login")

    elif "spotify web" in query or "spotify online" in query:
        speak("Opening Spotify")
        webbrowser.open_new_tab("https://open.spotify.com/")

    elif "netflix web" in query or "netflix online" in query:
        speak("Opening Netflix")
        webbrowser.open_new_tab("https://www.netflix.com/in/login")

    elif "twitter web" in query or "twitter online" in query:
        speak("Opening Twitter")
        webbrowser.open_new_tab("https://twitter.com/")

    elif "outlook web" in query or "outlook online" in query:
        speak("Opening Outlook")
        webbrowser.open_new_tab("https://outlook.office.com/")

    elif "zoom web" in query or "zoom online" in query:
        speak("Opening Zoom")
        webbrowser.open_new_tab("https://us04web.zoom.us/signin#/login")

    elif "teams web" in query or "teams online" in query or "microsoft teams online" in query:
        speak("Opening Microsoft Teams")
        webbrowser.open_new_tab("https://teams.microsoft.com/")

    elif query=="google meet":
        speak("Opening Google Meet")
        webbrowser.open_new_tab("https://meet.google.com/")

    elif query=="google maps":
        speak("Opening Google Maps")
        webbrowser.open_new_tab("https://www.google.co.in/maps/")

    elif query=="gmail":
        speak("Opening Gmail")
        webbrowser.open_new_tab("https://mail.google.com/")

    elif query=="google drive":
        speak("Opening Google Drive")
        webbrowser.open_new_tab("https://drive.google.com/")

    elif query=="amazon":
        speak("Opening Amazon")
        webbrowser.open_new_tab("https://www.amazon.in/")

    elif query=="hotstar":
        speak("Opening Hotstar")
        webbrowser.open_new_tab("https://www.hotstar.com/in")

    elif "morning" in query or "afternoon" in query or "evening" in query:
        wishMe(user_data.name)

    elif "good night" in query:
        hour = datetime.datetime.now().hour
        if hour >= 21 and hour < 24:
            speak("Good night")
            speak(user_data.name)
        else:
            wishMe(user_data.name)

    elif "play a song" in query or "play song" in query:
        try:
            l1 = []
            with open("config/song_dir.txt", "r") as f:
                l1 = f.readlines()
            music = []
            dir = "".join(l1)
            songs = os.listdir(dir)
            for i in songs:
                if ".mp3" in i:
                    music.append(i)
            speak("Playing a song")
            a = random.choice(music)
            os.startfile(os.path.join(dir, a))
        except:
            speak("Music directory unavailable")

    elif "play music" in query or "play some music" in query:
        try:
            with open("config/playlist.txt", "r") as f:
                playlists = f.readlines()
            speak("Playing music")
            a = random.choice(playlists)
            webbrowser.open_new_tab(a)
        except:
            speak("Playlist links unavailable")

    elif "play hindi music" in query or "play some hindi music" in query or "play hindi song" in query or "play a hindi song" in query:
        try:
            with open("config/hin_playlist.txt", "r") as f:
                playlists = f.readlines()
            speak("Playing hindi music")
            a = random.choice(playlists)
            webbrowser.open_new_tab(a)
        except:
            speak("Playlist links unavailable")

    elif "play english music" in query or "play some english music" in query or "play english song" in query or "play an english song" in query:
        try:
            with open("config/eng_playlist.txt", "r") as f:
                playlists = f.readlines()
            speak("Playing english music")
            a = random.choice(playlists)
            webbrowser.open_new_tab(a)
        except:
            speak("Playlist links unavailable")

    elif "open" in query:
        try:
            query = query.replace('open ', '')
            filename = query + '.txt'
            with open(filename, "r") as f:
                app_path = "".join(f.readlines())
            speak("Opening the app")
            os.startfile(app_path)
        except:
            speak("App path unavailable")

    elif "close" in query:
        try:
            query = query.replace('close ', '')
            exe_name = query + '.exe'
            command = ["taskkill", "/F", "/IM", exe_name]
            speak("Closing the app")
            subprocess.call(command)
        except:
            speak("App failed to close")

    elif "play" in query:
        try:
            s1 = query.replace('play ', '')
            s2 = s1 + '.mp3'
            with open("config/song_dir.txt", "r") as f:
                dir = "".join(f.readlines())
            songs = os.listdir(dir)
            music = [i for i in songs if ".mp3" in i]
            if s2 in music:
                speak("Playing" + s1)
                os.startfile(os.path.join(dir, s2))
            else:
                speak("Playing" + s1)
                kt.playonyt(s1)
        except:
            speak("Audio unavailable")

    elif "video" in query:
        try:
            s1 = query.replace(' video', '')
            s2 = s1 + '.mp4'
            with open("config/video_dir.txt", "r") as f:
                dir = "".join(f.readlines())
            videos = os.listdir(dir)
            video_files = [i for i in videos if ".mp4" in i]
            if s2 in video_files:
                speak("Playing" + s1)
                os.startfile(os.path.join(dir, s2))
            else:
                speak("Playing" + s1)
                kt.playonyt(s1)
        except:
            speak("Video directory unavailable")

    else:
        print("Please repeat")
