# IMPORT PACKAGES
import webbrowser
import os
import pyautogui

def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# DOMAIN WEBSITES OPEN FUNCTION
def navDomain(query):
    if any(keyword in query.lower() for keyword in [".com", ".co.in", ".org" ".in", ".me"]):
        query = query.replace("open", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https:///www.{query}")
        say(f"Opening {query}, sir.....")
        return

# CLOSE TAB
def closeTab(query):
    if any(keyword in query.lower() for keyword in ["close tab", "close the tab", "tab close"]):
        pyautogui.hotkey("command", "w")
        say("Closing, Tab")

