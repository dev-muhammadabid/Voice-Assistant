# IMPORT PACKAGES
import os

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

#MAIN PASSWORD FUNCTION
def passwordPin():
    for i in range(3):
        a = input("Enter the 6 Digit PIN to Open the Voice Assistant: ")
        pswrd_file = open("/Users/abii/Desktop/Programming StuFF/Projects/Personal Voice Assistant/voice-assistant/text file/password_pin.txt", "r")
        pswrd = pswrd_file.read()
        pswrd_file.close()
        if (a==pswrd):
            say("Assalamu alaykum Sir, I am your personal Voice Assistant", voice="Zoe")
            break
        elif (i==2 and a!=pswrd):
            exit()
        elif (a!=pswrd):
            say("Try Again!")

#CHANGE PASSWROD FUNCTION
def changePin():
    say("So, What's the new password or a pin")
    new_pswrd = input("Enter The mew Password or PIN: ")
    new_password = open("/Users/abii/Desktop/Programming StuFF/Projects/Personal Voice Assistant/voice-assistant/text file/password_pin.txt", "w")
    new_password.write(new_pswrd)
    new_password.close()
    say("Done Sir, Hope you remember you password or PIN.")
    say(f"Your new password or PIN is {new_pswrd}")