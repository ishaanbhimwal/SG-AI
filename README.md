# SG-AI Voice Assistant

## Overview

This is a Python-based voice assistant using OpenAI's GPT-3.5 language model. The assistant is named "SG-AI" (Suraksha Glove AI) and is designed to provide information and assistance related to the Suraksha Glove project. The project is focused on providing a safety solution for women using a wearable device that can notify family and police for assistance, generate a loud sound, and provide a self-defence mechanism.

## Requirements

- Python 3.x
- speech_recognition
- openai
- gtts
- pyfiglet
- ffplay

## Usage

- Clone the repository
- Install the required libraries: `pip install -r resources/requirements.txt`
- Append your [OpenAI API Key](https://platform.openai.com/docs/quickstart/add-your-api-key) in `openai.api_key` variable in `sg_ai.py`
- Run the `sg_ai.py` file: `python sg_ai.py`

## Working

The SG-AI voice assistant uses OpenAI's GPT-3.5 language model to generate responses to user queries. The assistant first provides a brief introduction about the Suraksha Glove project and its objectives. Then, it waits for the user to speak a query. The user's speech is converted into text using the `speech_recognition` library. The text query is then passed to the GPT-3.5 model which generates a response based on the input. The response is converted into speech using Google's text-to-speech library `gtts` and played back to the user using `ffplay`.
Sample Questions

Here are some sample questions that can be asked to the SG-AI voice assistant:

- "Hello! I am Ishaan. What is your name?"
- "Can you give me a short description about the Suraksha-Glove?"
- "Do you have a 3d model for the Suraksha-Glove?" (requires `blender` installed to work)
- "What are matter waves?"
- "Can you write a short code in Python to print hello world?"
- "Alright, thank you. You can exit now." (requires `unimatrix` installed to work)

## Applications

The SG-AI voice assistant can be used to demonstrate the Suraksha Glove project and its features. It can be used in presentations or events related to women's safety. It can also be extended to provide assistance in other areas such as healthcare, education, and finance by integrating other APIs and models with the voice assistant.

## Example

[![SG-AI Demo](https://img.youtube.com/vi/ZLmNFSJydcM/0.jpg)](https://www.youtube.com/watch?v=ZLmNFSJydcM)