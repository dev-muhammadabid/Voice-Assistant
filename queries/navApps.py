# IMPORT PACKAGES
import os

def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# APPS AND THEIR PATHS
apps = [["App Store", "/System/Applications/App Store.app"], ["Brave", "/Applications/Brave Browser.app"], ["Calculator", "/System/Applications/Calculator.app"], ["Calender", "/System/Applications/Calendar.app"], ["Chess", "/System/Applications/Chess.app"], ["Clock", "/System/Applications/Clock.app"],  ["Contacts", "/System/Applications/Contacts.app"], ["FaceTime", "/System/Applications/FaceTime.app"],  ["Find My", "/System/Applications/FindMy.app"],  ["Maps", "/System/Applications/Maps.app"],  ["Messages", "/System/Applications/Messages.app"],  ["Safari", "/System/Volumes/Preboot/Cryptexes/App/System/Applications/Safari.app"], ["Spotify", "/Applications/Spotify.app"], ["System Settings", "/System/Applications/System Settings.app"], ["VLC", "/Applications/VLC.app"], ["WhatsApp", "/Applications/WhatsApp.app"], ["Terminal", "/System/Applications/Utilities/Terminal.app"]]

# NAVIGATION APPS FUNCTION
def navApps(query):
    for app in apps:
        if f"open {app[0]}".lower() in query.lower():
            say(f"Opening {app[0]}, sir.....")
            os.system(f"open -a '{app[1]}'")
            return
        elif f"close {app[0]}".lower() in query.lower():
            say(f"Closing {app[0]}, sir.....")
            os.system(f"pkill -f '{app[1]}'")
            return