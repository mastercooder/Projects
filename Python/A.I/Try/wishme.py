import datetime
import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
selected_voice_index = 1

def wishMe():
    timenow = datetime.datetime.now().hour

    if timenow >= 0 and timenow <= 12:
        timenow = "Good Morning"
    elif timenow > 12 and timenow <= 18:
        timenow = "Good Afternoon"
    else:
        timenow = "Good evening"
    return timenow
    

while True:
    timenow = wishMe()
    print(timenow)  # or do whatever you want with the timenow 
    speaker.Voice = speaker.GetVoices().Item(selected_voice_index)
    speaker.Speak(timenow)
    break
