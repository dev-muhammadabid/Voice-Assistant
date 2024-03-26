# IMPORT PACKAGES
import os
import requests
import wolframalpha

def say(text, voice="Zoe"):
    os.system(f"say -v {voice} {text}")

# WOLFRAMALPHA FUNCTION
def Wolframalpha(query):
    apikey = "HXLY9P-JURRUYUTK5"
    url = f"http://api.wolframalpha.com/v1/result?appid={apikey}&i={query}"

    try:
        response = requests.get(url, verify=True)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error: {e}"

# CALCULATOR FUNCTION
def numCalc(query):
    query = query.replace("multiply", "*")
    query = query.replace("add", "+")
    query = query.replace("minus", "-")
    query = query.replace("divide", "/")

    result = Wolframalpha(query)
    print(result)
    say(result)