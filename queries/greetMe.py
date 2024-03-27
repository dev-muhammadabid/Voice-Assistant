# IMPORT PACKAGES
import os
import datetime

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# GREET FUNCTION
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        say("Good Morning, Sir")
    elif hour > 12 and hour <= 18:
        say("Good Afternoon, Sir")
    else:
        say("Good Evening, Sir")
    say("Tell How can i help you?")
