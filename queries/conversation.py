# IMPORT PACKAGES
import os

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# CONVO FUNCTION
def convo(query):
    #GREET CONVO
    if "what is your name" in query:
        say("My Name is Zoe, I am your Personal Voice Assistant")
    elif "what's your name" in query:
        say("My Name is Zoe, I am your Personal Voice Assistant")
    elif "Hello Zoe" in query:
        say("Yes Sir, I am here!!")
    elif query.lower() == "assalam walekum" or query.lower() == "as-salamu alaykum":
        say("walekum assalam, Ji Farmaaiiye !")
    elif query.lower() == "hello":
        say("Hello, how are you ?")
    elif "hey" in query:
        say("Hey, how you doin ?")
    elif "namaste" in query:
        say("Namaste")
    elif "bye" in query:
        say("BaBye")

    #AFTER GREET CONVO
    elif any(keyword in query.lower() for keyword in ["i am fine", "i am also fine", "i am great", "i am awesome"]):
        say("Ohh its Great, So tell me What can i do for you?.")
    elif "i am fine what about you" in query:
        say("I am also Great, and here for your Personal Assistance.")
    elif "what about you" in query:
        say("I am Great, and here for your Personal Assistance.")
    elif "how are you" in query:
        say("I am Awesome, What about you?")
    elif any(keyword in query.lower() for keyword in ["thank you", "thank u", "thanks", "thank"]):
        say("You're Welcome! It's my pleasure to assist you.")
    elif any(keyword in query.lower() for keyword in ["okay", "hmm", "ok"]):
        say("okay, sir")
