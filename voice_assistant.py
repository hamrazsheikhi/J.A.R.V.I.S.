import datetime
import os
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia


class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def greet(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour < 12:
            self.speak("Good Morning!")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon!") 
        else:
            self.speak("Good Evening!") 
        self.speak("Welcome, I am your personal Google assistant")

    def voice_command(self): 
        r = sr.Recognizer() 
        with sr.Microphone() as source:
            print("Recognizing...")
            r.pause_threshold = 1
            audio = r.listen(source) 
        try:
            print("Recognizing...")   
            query = r.recognize_google(audio, language ='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)   
            print("Unable to Recognize your voice.") 
            return "None" 
        return query

    def run(self):
        self.greet()
        while True: 
            command = self.voice_command().lower()
            if 'hello' in command:
                self.speak('Hi, how can I help you?')
            elif "wikipedia" in command:
                self.speak("Searching Wikipedia...")
                command = command.replace("wikipedia", "")
                results = wikipedia.summary(command, sentences=5)
                self.speak("According to Wikipedia")
                print(results)
                self.speak(results)
            elif 'open notepad' in command:
                self.speak('Opening Notepad for you...')
                os.startfile("c:\\windows\\system32\\notepad.exe")
            elif 'close notepad' in command:
                self.speak('Closing Notepad...')
                os.system('taskkill /F /IM notepad.exe')
            elif 'open youtube' in command:
                self.speak("Here you go to YouTube")
                webbrowser.open("https://www.youtube.com/")
            elif 'open google' in command:
                self.speak("Here you go to Google")
                webbrowser.open("https://www.google.co.in/")
            elif 'play music' in command:
                self.speak('Opening music player...')
                os.startfile("C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
            elif 'open mail' in command:
                self.speak("Here you go to mail")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            elif 'open whatsapp' in command:
                self.speak("Opening WhatsApp for you")
                webbrowser.open("https://web.whatsapp.com/")
            elif 'exit' in command:
                self.speak("Thanks for giving me your time. Have a nice day.")
                exit()


if __name__ == '__main__':
    try:
        assistant = VoiceAssistant()
        assistant.run()
    except Exception as ex:
        print(f"An error occurred: {ex}")
    finally:
        print("Thank you. Bye. Have a nice day.")