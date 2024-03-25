# IMPORT PACKAGES
import os
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
    elif "Assalam Walekum" in query:
        say("Walekum Assalam, Ji Farmaaiye !")
    elif "hello" in query:
        say("Hello, how are you ?")
    elif "hey" in query:
        say("Hey, how you doin ?")
    elif "namaste" in query:
        say("Namaste")
    elif "bye" in query:
        say("BaBye")

    #AFTER GREET CONVO
    elif "i am fine what about you" in query:
        say("I am also Great, and here for your Personal Assistance.")
    elif "what about you" in query:
        say("I am Great, and here for your Personal Assistance.")
    elif "how are you" in query:
        say("I am Awesome")
    elif "ok" in query:
        say("Hmmm")
