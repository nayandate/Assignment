"""pyttsx3 is a Python library used for Text-to-Speech (TTS).

engine = pyttsx3.init() : it creates engine to make changes
Ye speech engine initialize karta hai.

engine ke through hum:

text speak kar sakte hain
voice change kar sakte hain
speaking speed change kar sakte hain
volume change kar sakte hain
available voices dekh sakte hain
speech ko file mein save kar sakte hain



engine.say("Hello, welcome to Python.")

Ye text ko speech queue mein add karta hai.
Important:
engine.say() generally immediately speech complete nahi karta.




engine.say("Hello, welcome to Python.")

Ye text ko speech queue mein add karta hai.
Important:
engine.say() generally immediately speech complete nahi karta.

engine.say()
      ↓
Text queue mein
      ↓
engine.runAndWait()
      ↓
🔊 Speech



voice changing :
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

to get voices:
for i, voice in enumerate(voices):
    print(i, voice.name, voice.id)




change rate of voice 0-1 tak 0 min 1 max        
engine.setProperty("rate", 150) : Change the speed of the audio voice

Available voices
       ↓
User selects voice
       ↓
setProperty()
       ↓
say()
       ↓
runAndWait()
       ↓
🔊 Selected voice speaks


"""


import pyttsx3
"""
engine = pyttsx3.init()

engine.say("Hello, welcome to Python")

engine.runAndWait()"""


engine = pyttsx3.init()
voices = engine.getProperty("voices")

for voice in voices:
    print(voice)

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",150)
engine.setProperty("volume", 1)
#a = input("enter your name :")
engine.say("Welcome to python code ")
'''
engine.runAndWait()pyttsx3 is a Python library used for Text-to-Speech (TTS).

engine = pyttsx3.init() : it creates engine to make changes
Ye speech engine initialize karta hai.

engine ke through hum:

text speak kar sakte hain
voice change kar sakte hain
speaking speed change kar sakte hain
volume change kar sakte hain
available voices dekh sakte hain
speech ko file mein save kar sakte hain



engine.say("Hello, welcome to Python.")

Ye text ko speech queue mein add karta hai.
Important:
engine.say() generally immediately speech complete nahi karta.




engine.say("Hello, welcome to Python.")

Ye text ko speech queue mein add karta hai.
Important:
engine.say() generally immediately speech complete nahi karta.

engine.say()
      ↓
Text queue mein
      ↓
engine.runAndWait()
      ↓
🔊 Speech



voice changing :
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

to get voices:
for i, voice in enumerate(voices):
    print(i, voice.name, voice.id)




change rate of voice 0-1 tak 0 min 1 max        
engine.setProperty("rate", 150) : Change the speed of the audio voice

Available voices
       ↓
User selects voice
       ↓
setProperty()
       ↓
say()
       ↓
runAndWait()
       ↓
🔊 Selected voice speaks

import pyttsx3
"""
engine = pyttsx3.init()

engine.say("Hello, welcome to Python")

engine.runAndWait()"""


engine = pyttsx3.init()
voices = engine.getProperty("voices")

for voice in voices:
    print(voice)

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",150)
engine.setProperty("volume", 1)
#a = input("enter your name :")
engine.say("diggy hero welcome to python code ")
engine.runAndWait()
'''