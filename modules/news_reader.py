import requests
from bs4 import BeautifulSoup
from modules.speech_engine import speak

def india_news(): #works
    try:
        url='https://timesofindia.indiatimes.com/india'
        resp=requests.get(url)
        if resp.status_code==200:
            speak("India news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("div",{"class":"vertical_12 vertical_list_padding w_1 left_spacing right_spacing bottom_v_spacing undefined"})
            m=soup.find("div",{"class":"vertical_12 w_1 left_spacing right_spacing bottom_v_spacing undefined"})
            n=soup.find("div",{"class":"vertical_12 vertical_list_padding w_1 left_spacing right_spacing top_v_spacing undefined"})
            o=soup.find("div",{"class":"horizontal_4 w_1 left_spacing right_spacing undefined"})
            for i in l.find_all("a"):
                speak(i.text)
            for i in m.find_all("a"):
                speak(i.text)
            for i in n.find_all("a"):
                speak(i.text)
            for i in o.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def world_news(): #works
    try:
        url="https://timesofindia.indiatimes.com/world"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("World news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("div",{"class":"vertical_12 vertical_list_padding w_1 left_spacing right_spacing bottom_v_spacing undefined"})
            m=soup.find("div",{"class":"vertical_12 w_1 left_spacing right_spacing bottom_v_spacing undefined"})
            n=soup.find("div",{"class":"vertical_12 vertical_list_padding w_1 left_spacing right_spacing top_v_spacing undefined"})
            o=soup.find("div",{"class":"horizontal_4 w_1 left_spacing right_spacing undefined"})
            for i in l.find_all("a"):
                speak(i.text)
            for i in m.find_all("a"):
                speak(i.text)
            for i in n.find_all("a"):
                speak(i.text)
            for i in o.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def business_news(): #works
    try:
        url="https://timesofindia.indiatimes.com/business"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("Business news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("div",{"class":"row"})
            for i in l.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def sports_news(): #works
    try:
        url="https://timesofindia.indiatimes.com/sports"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("Sports news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("div",{"class":"vertical_12 vertical_list_padding w_1 left_spacing right_spacing bottom_v_spacing undefined"})
            m=soup.find("div",{"class":"vertical_12 w_1 left_spacing right_spacing bottom_v_spacing undefined"})
            n=soup.find("div",{"class":"vertical_12 vertical_list_padding w_1 left_spacing right_spacing top_v_spacing undefined"})
            o=soup.find("div",{"class":"horizontal_4 w_1 left_spacing right_spacing undefined"})
            for i in l.find_all("a"):
                speak(i.text)
            for i in m.find_all("a"):
                speak(i.text)
            for i in n.find_all("a"):
                speak(i.text)
            for i in o.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")
        
def latest_news(): #works
    try:
        url="https://timesofindia.indiatimes.com/home/headlines"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("Latest news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("div",{"class":"top-newslist"})
            for i in l.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def gadget_news(): #works
    try:
        url="https://timesofindia.indiatimes.com/gadgets-news"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("Gadget news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("ul",{"class":"top-newslist clearfix"})
            for i in l.find_all("a"):
                speak(i.text)

    except:
        speak("Unable to fetch requested data")

def crazy_news(): #works
    try:
        url="https://timesofindia.indiatimes.com/world/mad-mad-world"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("Crazy news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("ul",{"class":"top-newslist clearfix"})
            for i in l.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def politics_news(): #works
    try:
        url="https://timesofindia.indiatimes.com/politics"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("Politics news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("ul",{"class":"cvs_wdt clearfix"})
            for i in l.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def science_news(): #works
    try:
        url="https://timesofindia.indiatimes.com/home/science"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("Science news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("ul",{"class":"top-newslist clearfix"})
            for i in l.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def covid_india(): #works
    try:
        url="https://timesofindia.indiatimes.com/coronavirus/india"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("Indian covid news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("ul",{"class":"top-newslist clearfix"})
            for i in l.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def covid_world(): #works
    try:
        url="https://timesofindia.indiatimes.com/coronavirus/world"
        resp=requests.get(url)
        if resp.status_code==200:
            speak("World covid news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("ul",{"class":"top-newslist clearfix"})
            for i in l.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def state_news(): #works
    try:
        sample=[]
        state=""
        with open("config/state.txt","r") as f:
            a=f.readlines()
            for i in a:
                sample.append(i)
            for i in sample:
                state+=i
        start="https://timesofindia.indiatimes.com/india/"
        url=start+state
        resp=requests.get(url)
        if resp.status_code==200:
            speak("State news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("ul",{"class":"top-newslist clearfix"})
            for i in l.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data")

def city_news(): #works
    try:
        sample=[]
        city=""
        with open("config/city.txt","r") as f:
            a=f.readlines()
            for i in a:
                sample.append(i)
            for i in sample:
                city+=i
        start="https://timesofindia.indiatimes.com/city/"
        url=start+city
        resp=requests.get(url)
        if resp.status_code==200:
            speak("City news is as follows")
            soup=BeautifulSoup(resp.text,'html.parser')
            l=soup.find("div",{"class":"lSIdy col_l_6 col_m_6"})
            f=soup.find("div",{"class":"row"})
            for i in l.find_all("a"):
                speak(i.text)
            for i in f.find_all("a"):
                speak(i.text)
    except:
        speak("Unable to fetch requested data") 
