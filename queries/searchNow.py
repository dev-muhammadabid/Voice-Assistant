# IMPORT PACKAGES
import webbrowser
import os
import pywhatkit
import wikipedia
import wikipedia as googleScrap

def say(text, voice="Zoe"):
    os.system(f'say -v {voice} "{text}"')

# MAIN FUNCTION
def searchNow(query):
    if "google search" in query or "google" in query:
        googleSearch(query)
    elif "youtube search" in query or "youtube" in query:
        youtubeSearch(query)
    elif "wikipedia search" in query or "wikipedia" in query:
        wikipediaSearch(query)

# GOOGLE FUNCTION
def googleSearch(query):
    query = query.replace("google search", "")
    query = query.replace("google", "")
    say("That is what I found on Web")

    try:
        pywhatkit.search(query)
        result = googleScrap.summary(query, 1)
        say(result)

    except:
        say("Output Not Found")

# YOUTUBE FUNCTION
def youtubeSearch(query):
    query = query.replace("youtube search", "")
    query = query.replace("youtube", "")
    web =  "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    # pywhatkit.playonyt(query)
    say("That is what I found on Youtube")

# WIKIPEDIA FUNCTION
def wikipediaSearch(query):
    query = query.replace("wikipedia search", "")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences = 2)
    say("According to Wikipedia...")
    print(result)
    say(result)

