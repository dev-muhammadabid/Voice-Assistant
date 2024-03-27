# IMPORT PACKAGES
import os
import random
import speech_recognition as sr

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# TAKE COMMAND FUNCTION
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

# MAIN GAME FUNCTION
def gameRPS(query):
    say("I have one game ROCK, PAPER, SCISSORS")
    say("Do you want to play? Yes or No?")
    choice = takeCommand().lower()
    if choice != "yes":
        say("Okay, maybe next time!")
        return

    say("Great! Let's play!")
    print("Let's Play! ROCK, PAPER, SCISSORS")
    meScore = 0
    comScore = 0

    for i in range(3):
        say("Choose ROCK, PAPER, or SCISSORS")
        query = takeCommand().lower()

        choose = ("rock", "paper", "scissors")
        comChoose = random.choice(choose)

        if query not in choose:
            print("Invalid choice. Please choose ROCK, PAPER, or SCISSORS.")
            continue

        if query == comChoose:
            say(comChoose.upper())
            print(f"Score: Me - {meScore} & Com - {comScore}")
        elif (query == "rock" and comChoose == "scissors") or \
                (query == "paper" and comChoose == "rock") or \
                (query == "scissors" and comChoose == "paper"):
            say(comChoose.upper())
            meScore += 1
            print(f"Score: Me - {meScore} & Com - {comScore}")
        else:
            say(comChoose.upper())
            comScore += 1
            print(f"Score: Me - {meScore} & Com - {comScore}")

    print(f"FINAL SCORE: ME - {meScore} & COM - {comScore}")

    if meScore > comScore:
        winner = "You win!"
    elif meScore < comScore:
        winner = "Computer wins!"
    else:
        winner = "It's a tie!"

    say(winner)
    print(winner)