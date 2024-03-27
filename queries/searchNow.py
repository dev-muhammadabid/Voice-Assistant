# IMPORT PACKAGES
import webbrowser
import os
import pywhatkit
import wikipedia
import wikipedia as googleScrap

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f'say -v {voice} "{text}"')

# MAIN FUNCTION
def searchNow(query):
    if "google search" in query or "on google" in query:
        googleSearch(query)
    elif "youtube search" in query or "on youtube" in query:
        youtubeSearch(query)
    elif "wikipedia search" in query or "on wikipedia" in query:
        wikipediaSearch(query)

# GOOGLE FUNCTION
def googleSearch(query):
    query = query.replace("google search", "")
    query = query.replace("google", "")
    query = query.replace("on", "")
    query = query.replace("open", "")
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
    query = query.replace("play", "")
    query = query.replace("on", "")
    web =  "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    say("That is what I found on Youtube")

# WIKIPEDIA FUNCTION
def wikipediaSearch(query):
    query = query.replace("wikipedia search", "")
    query = query.replace("wikipedia", "")
    query = query.replace("on", "")
    result = wikipedia.summary(query, sentences = 1)
    say("According to Wikipedia...")
    print(result)
    say(result)

