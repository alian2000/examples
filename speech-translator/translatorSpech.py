import googletrans
from googletrans import Translator
from deep_translator import GoogleTranslator

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS



translator = Translator()
print(googletrans.LANGUAGES)
translator = GoogleTranslator(source='ar', target='en')
result = translator.translate("الحرب على غزة مباشر.. قصف مكثف على القطاع والقسام تحبط محاولة إسرائيلية لاستعادة جندي أسير", src='ar', dest='en')

#print(result.src)
#print(result.dest)
print(result)
def speak(text):
    tts = gTTS(text=text, lang="ar")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

speak(result)

