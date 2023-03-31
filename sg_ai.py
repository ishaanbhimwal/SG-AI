import speech_recognition as sr
import openai
import os
import threading
from time import sleep
from gtts import gTTS
from ctypes import *
from contextlib import contextmanager
import pyfiglet

openai.api_key = "OPENAI API KEY"

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)


def py_error_handler(filename, line, function, err, fmt):
    pass


c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)


@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary("libasound.so")
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)


def GenerateReply(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"You are Suraksha Glove AI Assistant or SG-AI. You are created by Ishaan Bhimwal for his Physics project. He has to show this project to his Physics teacher, Kartik Shastry. Women safety has always been an issue even in these modern times with so much advancement in technology. Women are not safe anywhere and are most vulnerable when traveling alone into lonely roads and deserted places. According to a report by Thomson Reuters Foundation, India is ranked as a highly dangerous place for women worldwide, India has the greatest number of child brides as well. In 2016, the number of reported rapes is almost 39,000. Experts that were interviewed for the reason why India is presumed to be dangerous for women said India is on top of the list because its government has done almost nothing to provide safety to women since the rape and murder of a student in early 20’s in 2012 which prompted changes in the rape laws of the country. Most of the attacks on women happen when they are traveling alone or are in a remote area where they are not able to find any help or proper assistance. Existing handheld devices that are available for women safety require women intervention to activate them such as pressing the button or shake the device etc after sensing the danger. However, for some reason if a woman has no time to activate it when she is danger, then the purpose of the safety device is not solved. Suraksha glove proposes a smart solution to address the problem of women safety and that overcome the shortcomings of existing devices. The proposed design comprises of features to notify family members and nearby police station for immediate assistance when women are not safe. Moreover, a shock wave generator is a part of the proposed design which women can use to attack the perpetrator. Some of the other features in the proposed work that provide additional support to women are as follows: Sending group messages from the device as well as from the victim's phone. Locating safe place from victim’s current location on the map. Generating loud sound to inform nearby people for help. Generating a 30kv charge for self-defence. The women safety device provides assistance to a woman who might be in an unsafe situation. The device is essentially ready for all the situations that might go against the will of the woman. Fig.1 shows the hardware design of the safety device. Right now, the design comprises of a primary switch to activate the device, buzzer for alerting the environment, shock wave generator (a higher power module) for self-defence and a secondary push switch to prevent accidental shocks. It has 2 replaceable pencils cells.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def print_with_typing_effect(text, delay=0.07):
    for char in text:
        print(char, end="", flush=True)
        sleep(delay)
    print()


def get_user_input():
    r = sr.Recognizer()
    with noalsaerr() as n, sr.Microphone() as source:
        print("-" * os.get_terminal_size().columns)
        print_with_typing_effect("Listening for input...")
        r.adjust_for_ambient_noise(source)
        audio_data = r.listen(source)
    try:
        text = r.recognize_google(audio_data)
        print_with_typing_effect(f"User: {text}")
        return text
    except:
        print_with_typing_effect("Sorry, I could not understand you.")
        return None


def play_audio(audio_file):
    os.system(f"ffplay -nodisp -autoexit {audio_file} >/dev/null 2>&1")


def blender_model():
    ai_response = "Yes I can show you a blender model of the Suraksha Glove."
    print_with_typing_effect("Generating the output...")
    tts = gTTS(text=ai_response, lang="en", tld="us")
    tts.save("resources/output.mp3")
    t1 = threading.Thread(target=play_audio, args=("resources/output.mp3",))
    t1.start()
    print_with_typing_effect(f"SG-AI: {ai_response}\n")
    t1.join()
    os.system("blender -W ~/Documents/programming/suraksha-glove/resources/glove.blend")
    main()


def exit_animation():
    os.system("foot -F unimatrix")
    exit()


def print_sgai():
    result = pyfiglet.figlet_format("SG-AI")
    print(result)


def main():
    while True:
        user_input = get_user_input()
        if not user_input:
            continue
        if "model" in user_input:
            blender_model()
        ai_response = GenerateReply(user_input)
        print_with_typing_effect("Generating the output...")
        tts = gTTS(text=ai_response, lang="en", tld="us")
        tts.save("resources/output.mp3")
        t1 = threading.Thread(target=play_audio, args=("resources/output.mp3",))
        t1.start()
        print_with_typing_effect(f"SG-AI: {ai_response}\n")
        t1.join()
        if "exit" in user_input:
            exit_animation()


if __name__ == "__main__":
    print_sgai()
    main()
