# IMPORT PACKAGES
import os
import datetime
import requests
from bs4 import BeautifulSoup


def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# DATE FUNCTION
def dateNow():
    strfDate = datetime.datetime.now().strftime("%A, %B %d, %Y")
    say(f"Sir the date is {strfDate}")

# TIME FUNCTION
def timeNow():
    strfTime = datetime.datetime.now().strftime("%H:%M:%S")
    say(f"Sir the time is {strfTime}")


# TEMPERATURE FUNCTION
def tempNow():
    search = "temperature in lucknow"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    say(f"current{search} is {temp}")