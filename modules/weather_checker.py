import requests
from bs4 import BeautifulSoup
from modules.speech_engine import speak

def temperature():
    try:
        sample = []
        city = ""
        with open("config/city.txt", "r") as f:
            a = f.readlines()
            for i in a:
                sample.append(i)
            for i in sample:
                city += i
        start = "https://www.indiatoday.in/weather/"
        last = " weather forecast today"
        end = city + last
        modified = end.split()
        ready = '-'.join(modified)
        url = start + ready
        resp = requests.get(url)

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            l = soup.find("div", {"class": "wtr_tmp_rhs"})
            temp = ""
            for i in l:
                temp += i.text.strip()

            # Replace degree symbol and lowercase c with proper words
            temp = temp.replace("°", " degrees ").replace("c", "Celsius").strip()

            # Optional: Add a pause before speaking value
            time.sleep(0.4)  # Give engine time to settle

            speak(f"The current temperature is {temp}")
        else:
            speak("Temperature unavailable")
    except Exception as e:
        speak("Unable to fetch temperature.")


def weather():
    try:
        sample=[]
        city=""
        with open("config/city.txt","r") as f:
            a=f.readlines()
            for i in a:
                sample.append(i)
            for i in sample:
                city+=i
        start="https://www.indiatoday.in/weather/"
        last=" weather forecast today"
        end=city+last
        modified=end.split()
        ready='-'.join(modified)
        url=start+ready
        resp=requests.get(url)
        if resp.status_code==200:
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("p",{"class":"aqi_wtr_txt"})
            for i in l:
                speak(i.text)
    except:
        speak("Unable to fetch weather data")
