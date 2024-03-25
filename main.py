# IMPORT PACKAGES
import os
import speech_recognition as sr
from queries.greetMe import greetMe
from queries.conversation import convo
from queries.dateTime import dateNow, timeNow, tempNow
from queries.navApps import navApps
from queries.navWeb import navWebsites, navDomain, closeTab
from queries.searchNow import searchNow

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# COMMAND FUNCTION+
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


# MAIN FUNCTION
if __name__ == "__main__":
    say("Assalamu alaykum Sir, I am your personal Voice Assistant", voice="Zoe")
    while True:
        query = takeCommand()

        # TURN OFF QUERY
        if "allah hafiz" in query:
            say("Allah Hafiz, Sir. You can call me anytime. I will always there for you!")
            exit()

        # GREET QUERY
        if "walekum assalam" in query:
            greetMe()

        # CONVERSATION QUERY
        if query:
            convo(query)

        # DATETIME QUERY
        if "date" in query:
            dateNow()
        if "time" in query.lower() and "facetime" not in query.lower():
            timeNow()
        # TEMPERATURE QUERY
        if "temperature" in query:
            tempNow()

        # APPLICATIONS NAVIGATION QUERY
        if query:
            navApps(query)

        # WEBSITES NAVIGATION QUERY
        if query:
            navWebsites(query)
        if query:
            navDomain(query)
        if query:
            closeTab(query)

        # SEARCH ON WEB QUERY
        if query:
            searchNow(query)