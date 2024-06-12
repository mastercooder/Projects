import webbrowser
import urllib.parse
import win32com.client

query = ("Enter the command:")


'''
if "search in flipkart" in query.lower():
    search_query = query.lower().replace("search in flipkart", "")
    reaplaced_query = urllib.parse.quote(search_query)
    flipkart_url = "https://www.flipkart.com/search?q="
    search_url = flipkart_url + reaplaced_query
    speaker.Speak(f"Searching in flipkart {search_url}")
    webbrowser.open(search_url)


if "search in flipkard" in query.lower():
    search_query = query.lower().replace("search in flipkard", "")
    reaplaced_query = urllib.parse.quote(search_query)
    amazon_url = "https://www.flipkart.com/search?q="
    search_url = amazon_url + reaplaced_query
    print(f"Searching in flipkard {search_query}")
    print(search_url)
    # webbrowser.open(search_url)

if "search in flipkard" in query.lower():
    search_query = query.lower().replace("search in flipkard", "")
    reaplaced_query = urllib.parse.quote(search_query)
    flipkart_url = "https://www.flipkart.com/search?q="
    search_url = flipkart_url + reaplaced_query
    speaker.Speak(f"Searching in flipkard {search_query}")
    webbrowser.open(search_url)

if "search in wikipedia" in query.lower():
    search_query = query.lower().replace("search in wikipedia", "")
    reaplaced_query = urllib.parse.quote(search_query)
    wikipedia_url = "https://en.wikipedia.org/wiki/Special:Search?search="
    search_url = wikipedia_url + reaplaced_query
    speaker.Speak(f"Searching {search_query} in wikipedia")
    print(search_url)
    webbrowser.open(search_url)
if "search in map" in query.lower():
    search_query = query.lower().replace("search in map", "")
    replaced_query = urllib.parse.quote(search_query)
    map_url = "https://www.google.com/maps/search/"
    search_url = map_url + replaced_query
    speaker.Speak(f"Locating {search_query} on Google Maps")
    webbrowser.open(search_url)

if "search in google" in query.lower() or "search on google" in query.lower() or "in google" in query.lower() or "on google" in query.lower():
    search_query = query.lower().replace("search in google", "")
    reaplaced_query = urllib.parse.quote(search_query)
    google_url = "https://www.google.com/search?q="
    search_url = google_url + reaplaced_query
    speaker.Speak(f"Searching in google {search_query}")
    webbrowser.open(search_url)
'''

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
sites = [
    ["instagram", "https://www.instagram.com/"],
    ["insta", "https://www.instagram.com/"]
]

for site in sites:
    if f"open {site[0]}".lower() in query.lower():
        print(f"Opening {site[0]} sir...")
        webbrowser.open(site[1])


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
if"show my orders of flipkart" in query.lower() or "order of flipkart" in query.lower() or "flipkart order" in query.lower():
    speaker.Speak("Shoing all your orders of flipkart sir...")
    webbrowser.open("https://www.flipkart.com/account/orders?link=home_orders")
'''
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------