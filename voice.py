import time
import sys

import openai
import speech_recognition as sr
import pyttsx3
import argparse

# Set the API key for the OpenAI service
parser = argparse.ArgumentParser()
parser.add_argument('--api-key', required=True, help='Your OpenAI API key')
args = parser.parse_args()

# Initialize the OpenAI API client
openai.api_key = args.api_key

# Create a speech engine for text-to-speech
engine = pyttsx3.init()

# create a microphone instance
mic = sr.Microphone(device_index=13)

# Listen for audio input
print("Listening for audio...")

# Create a recognizer object
r = sr.Recognizer()

# define the callback function
def callback(recognizer, audio):
    # try to recognize the speech in the recording
    print("callback")
    try:
        # convert the speech to text
        text = recognizer.recognize_google(audio)
        print("I heard:")
        print(text)
        if "stop" in text.lower():
            print("ok, im not listening any more. ctrl+c to quit")
            sys.exit(0)
        query = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            max_tokens=1024,
            n=1,
            temperature=0.5,
        )
        response = query.choices[0].text

        # Read the response aloud using the speech engine
        print(f"Reading response: {response}")
        engine.say(response)
        engine.runAndWait()
    except sr.UnknownValueError:
        # speech was not recognized
        print("speech not recognized")
        pass
    except sr.RequestError as e:
        # API was unreachable or unresponsive
        print("API error: {}".format(e))

# start listening in the background
r.listen_in_background(mic, callback)

# run the script indefinitely until the user presses Ctrl+C
try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    # stop listening
    print("dying")
