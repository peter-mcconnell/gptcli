#!/usr/bin/env python3
import openai
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--api-key', required=True, help='Your OpenAI API key')
parser.add_argument('--model', default='text-davinci-002', help='The model to use for completion')
args = parser.parse_args()

# Initialize the OpenAI API client
openai.api_key = args.api_key

# Create a new instance of ChatGPT
completion = openai.Completion.create(
  engine=args.model,
  prompt="Hello, how are you today?",
  max_tokens=1024,
  temperature=0.5
)

# Continuously prompt the user for input and send to ChatGPT
while True:
    try:
      # Get user input
      input_text = input("Enter your message: ")

      # Send user input to ChatGPT and get response
      response = openai.Completion.create(
        engine=args.model,
        prompt=input_text,
        max_tokens=1024,
        temperature=0.5
      )

      # Print ChatGPT response
      print(response["choices"][0]["text"])
    except KeyboardInterrupt:
        break
