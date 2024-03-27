# IMPORT PACKAGES
import os
from pynput.keyboard import Key, Controller

# VOICE FUNCTION
def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# DEFINE FUNCTION
keyboard = Controller()

# PLAY PAUSE FUNCTION
def playPause():
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)

# VOLUME UP/DOWN FUNCTION
def volumeUp():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
def volumeDown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)

# MUTE/UN MUTE FUNCTION
def muteMedia():
    keyboard.press(Key.media_volume_mute)
    keyboard.release(Key.media_volume_mute)

# NEXT/PREVIOUS MEDIA FUNCTION
def nextMedia():
    keyboard.press(Key.media_next)
    keyboard.release(Key.media_next)
def previousMedia():
    for i in range(2):
        keyboard.press(Key.media_previous)
        keyboard.release(Key.media_previous)


# MEDIA CONTROL TAB
def mediaControl(query):
    if any(keyword in query.lower() for keyword in ["paused", "stop"]):
        say("Paused, Sir")
        playPause()
    elif any(keyword in query.lower() for keyword in ["play video", "play the video", "play media", "play the media", "play music", "play the music"]):
        say("Played, Sir")
        playPause()
    elif "mute" in query:
        say("Media, Muted")
        muteMedia()
    elif "un mute" in query:
        say("Media, Un muted")
        muteMedia()
    elif "volume up" in query:
        say("Turning Volume, Up")
        volumeUp()
    elif "volume down" in query:
        say("Turning Volume, Down")
        volumeDown()
    elif any(keyword in query.lower() for keyword in ["next", "next video", "next music", "next media"]):
        say("Go to The Next, Media")
        nextMedia()
    elif any(keyword in query.lower() for keyword in ["previous", "previous video", "previous music", "previous media"]):
        say("Back on previous, on")
        previousMedia()