# IMPORT PACKAGES
import os
import requests

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

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
    print("Which Topic news you want to hear, Sir? [headlines], [business], [entertainment], [sports], [technology]")
    say("Which Topic news you want to hear, Sir? [headlines], [business], [entertainment], [sports], [technology]")
    field = input("Type the Topic: ").lower()

    for key, value in api_dict.items():
        if key.lower() in field:
            url = value
            print("News Found")
            break
        else:
            print("News not Found!")
            return

    response = requests.get(url)
    news = response.json()
    say("Here are the latest news headlines.")

    articles = news.get("articles", [])
    for article in articles:
        title = article["title"]
        print(title)
        say(title)
        news_url = articles["url"]
        print(f"Read full news at: {news_url}")

        a = input("[Press 1 to Continue] and [Press 2 to Exit]: ")
        if int(a) == 1:
            pass
        elif int(a) == 2:
            break

    say("That's all, Sir")