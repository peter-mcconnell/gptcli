gpt cli
=======

A simple CLI for interacting with ChatGPT, written entirely by ChatGPT

Run
---

Get an API key from Open AI - you will pass this in as a CLI arg.

```sh
./main.py --api-key=$(cat api.key)
```

gpt voice
=========

hands-free mode. speak to it and have it speak back to you. requires speech_recognition

```sh
pip3 install --user SpeechRecognition pyttsx3
./voice.py --api-key=$(cat api.key)
```
