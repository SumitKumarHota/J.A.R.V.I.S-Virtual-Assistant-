import os
import subprocess
import shutil
import winshell
import time  # Required for time.sleep()
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime, date
from modules.speech_engine import speak

def tellTime():
    current_time = datetime.now()
    hour = current_time.strftime("%I")  # 12-hour format
    minute = current_time.strftime("%M")
    speak("It is " + hour + " hours and " + minute + " minutes.")
    time.sleep(1)

def tellDay():
    day = datetime.today().weekday() + 1
    Day_dict = {
        1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
        4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'
    }
    if day in Day_dict:
        day_of_the_week = Day_dict[day]
        speak("The day is " + day_of_the_week)

def tellDate():
    today = date.today()
    speak("Today's date is " + today.strftime("%B %d, %Y"))

def set_user_from_voice(filename):
    global name
    name = os.path.splitext(os.path.basename(filename))[0].capitalize()

def low_vol():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevel()
        speak("Volume down")
        volume.SetMasterVolumeLevel(current - 0.5, None)
    except:
        speak("Volume not lowered")

def high_vol():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevel()
        speak("Volume up")
        volume.SetMasterVolumeLevel(current + 0.5, None)
    except:
        speak("Volume not increased")
