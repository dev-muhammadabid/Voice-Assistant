# IMPORT PACKAGES
import os
import speech_recognition as sr
from queries.passwordPin import passwordPin, changePin
from queries.genralPrupose import screenshotSS
from queries.greetMe import greetMe
from queries.conversation import convo
from queries.dateTime import dateNow, timeNow, tempNow
from queries.navApps import navApps
from queries.navWeb import navDomain, closeTab
from queries.searchNow import searchNow
from queries.mediaControl import mediaControl
from queries.newsRead import latestNewsIndia
from queries.numCalc import numCalc
from queries.whatsappMsg import sendMsg
from queries.gameRPS import gameRPS

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
    # PASSWORD PROTECTED
    passwordPin()

    # COMMAND LOOP
    while True:
        query = takeCommand()

        # TURN OFF QUERY
        if "allah hafiz" in query:
            say("Allah Hafiz, Sir. You can call me anytime. I will always there for you!")
            exit()

        # CHANGE PASSWORD QUERY
        if any(keyword in query.lower() for keyword in ["change my pin", "change pin", "change the password", "change password", "change my password"]):
            changePin()

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
        if any(keyword in query.lower() for keyword in ["temperature", "weather"]):
            tempNow()

        # APPLICATIONS NAVIGATION QUERY
        if query:
            navApps(query)

        # SCREENSHOT QUERY
        if "screenshot" in query:
            screenshotSS()

        # CALCULATOR QUERY
        if "calculate" in query:
            numCalc(query)

        # WEBSITES NAVIGATION QUERY
        if query:
            navDomain(query)
        if query:
            closeTab(query)

        # SEARCH ON WEB QUERY
        if query:
            searchNow(query)

        # MEDIA CONTROL QUERY
        if query:
            mediaControl(query)

        # NEWS QUERY
        if any(keyword in query.lower() for keyword in ["tell me the news", "tell me a news", "tell news", "tell me the latest news"]):
            latestNewsIndia()

        # WHATSAPP MESSAGE SEND QUERY
        if "whatsapp" in query:
            sendMsg()

        # GAME QUERY
        if any(keyword in query.lower() for keyword in ["You have games", "let's play a game", "play game"]):
            gameRPS(query)

