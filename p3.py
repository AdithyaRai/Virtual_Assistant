import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3
import urllib.parse
import requests
from bs4 import BeautifulSoup

import webbrowser
import os
import datetime
import time
import sys

# recognizer and tts engine
recognizer = sr.Recognizer()
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[0].id)
except Exception as e:
    print(f"Error initializing TTS engine: {e}")
    engine = None

def speak(text):
    print(text)
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error speaking: {e}")
            pass

def listen():
    # try microphone first; fallback to typed input if microphone/PyAudio unavailable
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            recognizer.adjust_for_ambient_noise(source, duration=0.8)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
    except (OSError, AttributeError) as e:
        print(f"Microphone error, falling back to typed input: {e}")
        return input("Type command: ").strip().lower()
    except sr.WaitTimeoutError:
        print("Listen timeout (no speech detected).")
        return ""

    try:
        command = recognizer.recognize_google(audio)
        print(command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry! I didn't catch that")
        return ""
    except sr.RequestError as e:
        print(f"Speech service error: {e}")
        return input("Fallback - type command: ").strip().lower()

# Function to scrape Google search results
def scrape_google(query):
    try:
        url = f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}  # More specific User-Agent
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.content, 'html.parser')
        results = []
        for g in soup.find_all('div', class_='Gx5Zad'):  # Updated class name
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                if link.startswith('/url?q='):
                    link = link[7:]  # Remove /url?q=
                try:
                    title = g.find('h3', class_='zBAauu').text  # Updated class name
                    snippet = g.find('div', class_='BNeawe').text  # Updated class name
                    results.append(f"{title}: {snippet}")
                except AttributeError as e:
                    print(f"Error extracting title or snippet: {e}")
                except Exception as e:
                    print(f"Unexpected error extracting data: {e}")
        return results[:3]  # Return top 3 results

    except requests.exceptions.RequestException as e:
        print(f"Error during Google search: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error during scraping: {e}")
        return []

def processCommand(command):
    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif ("jarvis search" in command) or ("search" in command):
        query = command.replace("jarvis", "").replace("search", "").strip()
        if not query:
            speak("What do you want to search?")
            q = listen()
            query = q or query
        if query:
            speak(f"Searching Google for {query}")
            webbrowser.open("https://www.google.com/search?q=" + urllib.parse.quote_plus(query))
            # Scrape and speak search results
            results = scrape_google(query)
            if results:
                speak("Here's a summary of the search results:")
                for result in results:
                    speak(result)
            else:
                speak("Sorry, I couldn't retrieve any search results.")
        else:
            speak("I didn't get the search query.")

    elif any(word in command for word in ("shutdown", "shut down", "power off")):
        speak("Are you sure you want to shut down the system? Say yes to confirm.")
        confirm = listen()
        print(f"Confirmation: {confirm!r}")  # debug
        if confirm and any(word in confirm for word in ("yes", "y", "yeah", "sure", "ok", "okay", "confirm")):
            speak("Shutting down your computer. Goodbye!")
            try:
                os.system("C:\\Windows\\System32\\shutdown /s /t 1")  # delay 1 sec for TTS
            except Exception as e:
                speak(f"Shutdown failed: {e}")
        else:
            speak("Shutdown cancelled.")

    elif "test tts" in command:
        speak("This is a test of the text-to-speech engine.")

    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        sys.exit(0)

    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello, I'm Jarvice. How can I help you?")
    try:
        while True:
            cmd = listen()
            if not cmd:
                # give user chance to retry
                print("No command captured — try again.")
                continue
            processCommand(cmd)
    except KeyboardInterrupt:
        speak("Exiting. Goodbye.")
        sys.exit(0)