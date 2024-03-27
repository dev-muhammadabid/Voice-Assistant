import os
import pyautogui

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# SCREENSHOT FUNCTION
def screenshotSS():
    im = pyautogui.screenshot()
    im.save("/Users/abii/Desktop/Programming StuFF/Projects/Personal Voice Assistant/voice-assistant/screenshots/ss.png")
    say("Screenshot Take it!, Sir")
