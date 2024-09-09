import speech_recognition as sr
import gtts
from playsound import playsound
import os

class SpeechRecognizer:

    r = sr.Recognizer()

    activation_command = "hello"
    deactivation_command = "bye"

    def get_audio(self):
        with sr.Microphone() as source:
            print("Say something")
            audio = self.r.listen(source)
        return audio

    def audio_to_text(self, audio):
        text = ""
        try:
            text = self.r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError:
            print("could not request results from API")
        return text

    def play_sound(self, text):
        try:
            tts = gtts.gTTS(text)
            tempfile = "./temp.mp3"
            tts.save(tempfile)
            playsound(tempfile)
            os.remove(tempfile)
        except AssertionError:
            print("could not play sound")