# IMPORT PACKAGES
import os
import requests
import speech_recognition as sr

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        print("Listening.....")
        audio = r.listen(source, 0,4)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"Sir Said: {query}")
        return query.lower()

    except sr.UnknownValueError:
        print("Sorry Sir! I didn't understand what you said.")
        return ""

    except sr.RequestError:
        print("Sorry Sir! I am unable to access the Google API.")
        return ""

# NEWS FUNCTION
def latestNewsIndia():
    api_dict = {"headlines": "https://newsapi.org/v2/top-headlines?country=in&apiKey=d5f01453dfd94f1d8011d1ab9b71c2d0",
                "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=d5f01453dfd94f1d8011d1ab9b71c2d0",
                "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=d5f01453dfd94f1d8011d1ab9b71c2d0",
                "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=d5f01453dfd94f1d8011d1ab9b71c2d0",
                "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=d5f01453dfd94f1d8011d1ab9b71c2d0"
                }

    content = None
    url = None
    while True:
        print("Which Topic news you want to hear, Sir? [headlines], [business], [entertainment], [sports], [technology]")
        say("Which Topic news you want to hear, Sir? [headlines], [business], [entertainment], [sports], [technology]")
        field = takeCommand().lower()

        if field not in api_dict:
            print("Invalid news. Please try again.")
            say("Invalid news. Please try again.")
        else:
            break

    for key, value in api_dict.items():
        if key.lower() in field:
            url = value
            print("News Found")
            break
        else:
            say("Sorry, News not Found!")
            print("Exit")
            return

    response = requests.get(url)
    news = response.json()
    say("Here are the latest news headlines.")

    articles = news.get("articles", [])
    for article in articles:
        title = article["title"]
        print(title)
        say(title)
        news_url = article["url"]
        print(f"Read full news at: {news_url}")

        say("Do you want to continue or exit?")
        response = takeCommand()
        if "continue" in response:
            pass
        elif "exit" in response:
            break

    say("That's all, Sir")