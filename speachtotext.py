import speech_recognition as sr
import pyttsx3 as tts
from automationoptions.wek_auto import *
from automationoptions.google_auto import *
from automationoptions.video_auto import *

def exitengine(recognised_text):
    if recognised_text.__contains__("close") or recognised_text.__contains__("exit"):
        exit()
    return 1

def holdengine(recognised_text):
    if recognised_text.__contains__("nothing") or recognised_text.__contains__("no"):
        engine.runAndWait()
        r.adjust_for_ambient_noise(source=source)
        text = r.listen(source=source)
        recognised_text = r.recognize_google(text)
    return recognised_text

def enginecomands(recognised_text):
    if recognised_text.__contains__("about"):
        search = recognised_text.split("about",1)[1]
        result = Info()
        result.get_info(search, engine)
        return 1
    if recognised_text.__contains__("play"):
        music = recognised_text.split("play",1)[1]
        result = Music()
        result.play(music)
        return 1
    if recognised_text.__contains__("search"):
        search = recognised_text.split("search",1)[1]
        result = GoogleSearch()
        result.search_result(search)
        return 1

def excutecomand(recognised_text):
    text = "filler"
    while text != "":
        print(recognised_text)
        try:
            exitengine(recognised_text)
            recognised_text = holdengine(recognised_text)
            enginecomands(recognised_text)
            engine.say("Anything else?")
            engine.runAndWait()
            r.adjust_for_ambient_noise(source=source)
            text = r.listen(source=source)
            recognised_text = r.recognize_google(text)
        except sr.UnknownValueError:
            engine.say("Sorry I didn't understand")
            engine.runAndWait()
            r.adjust_for_ambient_noise(source=source)
            text = r.listen(source=source)
            recognised_text = r.recognize_google(text)
        except sr.RequestError as e:
            engine.say("Error! please try again later!")
            engine.runAndWait()
            exit()



r = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.say("Hello, how can i help?")
engine.runAndWait()


with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source=source)
    text = r.listen(source=source)
    while text != "":
        try:
            recognised_text = r.recognize_google(text)
            exitengine(recognised_text)
            excutecomand(recognised_text)
        except sr.UnknownValueError:
            engine.say("Sorry I didn't understand")
            engine.runAndWait()
            r.adjust_for_ambient_noise(source=source)
            text = r.listen(source=source)
        except sr.RequestError as e:
            engine.say("Error! please try again later!")
            engine.runAndWait()
            exit()

