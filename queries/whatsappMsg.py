# IMPORT PACKAGES
import os
from datetime import timedelta, datetime
import pywhatkit

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# WHATSAPP SEND MESSAGE FUNCTION
def sendMsg():
    say("Who do you want to message on WhatsApp? Enter 1 for TestCase1 or 2 for TestCase2.")
    recipient = input("Enter 1 or 2: ")

    if recipient == '1':
        phone_number = "+91900000000"
        recipient_name = "XYZ"
    elif recipient == '2':
        phone_number = "+91900000000"
        recipient_name = "ABCD"
    else:
        say("Invalid recipient number.")
        return

    say(f"What's the message you want to send to {recipient_name}?")
    message = input("Enter the message: ")

    pywhatkit.sendwhatmsg(phone_number, message, datetime.now().hour, datetime.now().minute + 1)
    say("Message sent successfully!")
