from os import close, error
import speech_recognition as sr
import pyttsx3 as tts
from automationoptions.wek_auto import *
from automationoptions.google_auto import *
from automationoptions.video_auto import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



def exitengine(message):
    if message.__contains__("close") or message.__contains__("exit"):
        exit()
    return 0

def holdengine(text_area,message,engine,source,r):
    if message.__contains__("nothing") or message.__contains__("no"):
        engine.runAndWait()
        r.adjust_for_ambient_noise(source=source)
        text = r.listen(source=source)
        message = r.recognize_google(text)
        display_new_messages(text_area,message)
    return message

def typeholdengine(text_area,message,engine):
    if message.text().__contains__("nothing") or message.text().__contains__("no"):
        engine.runAndWait()
        send_message(text_area,message)
        return 1
    return 0

def enginecomands(message,engine):
    if message.__contains__("about"):
        search = message.split("about",1)[1]
        result = Info()
        result.get_info(search, engine)
    if message.__contains__("play"):
        music = message.split("play",1)[1]
        result = Music()
        result.play(music)
    if message.__contains__("search"):
        search = message.split("search",1)[1]
        result = GoogleSearch()
        result.search_result(search)

def excutecomand(text_area,message,engine,source,r):
    text = "filler"
    while text != "":
        try:
            exitengine(message)
            message = holdengine(text_area,message,engine,source,r)
            enginecomands(message,engine)
            engine.say("Anything else?")
            engine.runAndWait()
            r.adjust_for_ambient_noise(source=source)
            text = r.listen(source=source)
            message = r.recognize_google(text)
        except sr.UnknownValueError:
            engine.say("Sorry I didn't understand")
            engine.runAndWait()
            r.adjust_for_ambient_noise(source=source)
            text = r.listen(source=source)
            message = r.recognize_google(text)
        except sr.RequestError as e:
            engine.say("Error! please try again later!")
            engine.runAndWait()
            exit()

def display_new_messages(text_area,new_message):
    if new_message:
        text_area.append(new_message)

def send_message(text_area,message):
    display_new_messages(text_area,message.text())
    message.clear()

def microphone(text_area,speach_button,exit_button,engine,speach_label,message_box):
    message_box.hide()
    speach_button.hide()
    speach_label.show()
    exit_button.show()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source)
        text = r.listen(source=source)
        while text != "":
            def recall():
                exit_button.hide()
                speach_label.hide()
                message.show()
                speach_button.show()
            exit_button.clicked.connect(recall)
            try:
                message = r.recognize_google(text)
                display_new_messages(text_area,message)
                exitengine(message)
                excutecomand(text_area,message,engine,source,r)
            except sr.UnknownValueError:
                srrymessage = "Sorry I didn't understand"
                engine.say(srrymessage)
                display_new_messages(srrymessage)
                engine.runAndWait()
                r.adjust_for_ambient_noise(source=source)
                text = r.listen(source=source)
                exit_button.clicked.connect(recall)
            except sr.RequestError as e:
                errormsg = "Error! please try again later!"
                engine.say(errormsg)
                display_new_messages(errormsg)
                engine.runAndWait()
                exit()

def typeexcutecomand(text_area,message,engine):
    while message.text() != "":
        try:
            exitengine(message.text())
            holdmessage = typeholdengine(text_area,message,engine)
            if holdmessage:
                return 
            else:
                enginecomands(message.text(),engine)
                engine.say("Anything else?")
                engine.runAndWait()
                send_message(text_area,message)
        except sr.UnknownValueError:
            engine.say("Sorry I didn't understand")
            engine.runAndWait()
            send_message(text_area,message)
        except sr.RequestError as e:
            engine.say("Error! please try again later!")
            engine.runAndWait()
            exit()

def typing(text_area,message,engine):
    try:
        exitengine(message.text())
        typeexcutecomand(text_area,message,engine)
        send_message(text_area,message)
    except error: 
        errormsg = "Error! please try again later!"
        display_new_messages(errormsg)
        exit()

def assisatant(text_area,speach_button,exit_button,speach_label,message,enter_button):
    engine = tts.init()
    #voices = engine.getProperty("voices")
    #engine.setProperty("voice",voices[1].id)
    #engine.say("Hello, how can i help?")
    #engine.runAndWait()
    def wrapper():
        typing(text_area,message,engine)
    enter_button.clicked.connect(wrapper)
    def wraper():
        microphone(text_area,speach_button,exit_button,engine,speach_label,message)
    speach_button.clicked.connect(wraper)