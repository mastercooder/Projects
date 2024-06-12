import pyttsx3
import speech_recognition as sr # pip install speechRecognition 
import datetime
import webbrowser
import os
import smtplib
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak ("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak ("Good Afternoon")

    else:
        speak ("Good Evening")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes Microphone input from the user and return string ourput
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold  = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said:  {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dellf15ryzenedition@gmail.com', 'DELL@G15@75K')
    server.sendmail('dellf15ryzenedition@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    # Logick for executing task on the basis on query
        if "wikipedia" in query:
            speak('Searching in wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("Accourding to wikipedia")
            print(result)
            speak(result)
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open facebook'in query:
            webbrowser.open("https://www.facebook.com")
        
        elif 'play music' in query:
            music_dir = "C:\\Users\\tejes\\Music\\Music\\Agar Tum Sath Ho X Can we kiss forever  Sush & Yohan Remix.mp3"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\Tejesh Patel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email to tejesh' in query:
            try:
                speak("What shoud I say?")
                content = takeCommand()
                to = "TejeshYourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:
                print(e)
                speak("Some thig went wrong! Your email is not send")
