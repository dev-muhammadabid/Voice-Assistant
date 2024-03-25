# IMPORT PACKAGES
import webbrowser
import os
import pyautogui

def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# SITES WITH URLS
sites = [["Gmail", "https://mail.google.com/mail/u/0/#inbox"], ["Instagram", "https://www.instagram.com/"], ["Facebook", "https://www.facebook.com/"], ["Twitter", "https://www.twitter.com/"], ["Linkedin", "https://www.linkedin.com/"], ["Amazon", "https://www.amazon.in/"], ["Flipkart", "https://www.flipkart.com/"], ["Netflix", "https://www.netflix.com/"], ["Github", "https://www.github.com/"], ["ChatGPT", "https://chat.openai.com/"]];

# DIRECT NAVIGATE FUNCTION
def navWebsites(query):
    for site in sites:
        if f"Open {site[0]}".lower() in query:
            say(f"Opening {site[0]}, sir.....")
            webbrowser.open(site[1])

# DOMAIN WEBSITES OPEN FUNCTION
def navDomain(query):
    if ".com" in query or ".co.in" in query or ".org" in query or ".in" in query or ".me" in query:
        query = query.replace("open", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https:///www.{query}")

# CLOSE TAB
def closeTab(query):
    if "close tab" in query.lower() or "tab close" in query.lower():
        pyautogui.hotkey("command", "w")
        say("Closing, Tab")

