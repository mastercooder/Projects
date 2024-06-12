import speech_recognition as sr
import win32com.client
import urllib.parse
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")
selected_voice_index = 1

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pause_threshold = 0.3
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print("Recognizing...")
            print(f"User Said: {query}")
            return query
        except Exception as e:
            return "Something went wrong. Please check the code."

while True: 
    speaker.Voice = speaker.GetVoices().Item(selected_voice_index)
    speaker.Speak("Testing...")
    while True:
        print("Listening...")
        query = takeCommand()


        if "search in youtube" in query.lower():
            search_query = query.lower().replace("search in youtube", "")
            reaplaced_query = urllib.parse.quote(search_query)
            youtube_url = "https://www.youtube.com/results?search_query="
            search_url = youtube_url + reaplaced_query
            speaker.Speak(f"Searching for {search_query} in youtube")
            webbrowser.open(search_url)

        if "search in google" in query.lower():
            search_query = query.lower().replace("search in google", "")
            reaplaced_query = urllib.parse.quote(search_query)
            google_url = "https://www.google.com/search?q="
            search_url = google_url + reaplaced_query
            speaker.Speak(f"Searching in google {search_query}")
            webbrowser.open(search_url)


