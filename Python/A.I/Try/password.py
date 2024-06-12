
#                                            Code Writtne by Me
#                                           --------------------
import webbrowser

def takeCommand():
    query = input("Enter the command: ")
    print("Recognnizing...")
    print()
    print(f"User Said: {query}")
    return query

while True:
    print("Hello sir!")
    while True:
        password_correct = False
        while not password_correct:
            query = takeCommand()

            secures = [
                ["google", "https://www.google.com"]
            ]

            for secure in secures:
                if f"open {secure [0]}" in query.lower():
                    password = input("Enter the passord to login")
                    if password=="1234":
                        print()
                        print("The password is correct")
                        print(f"Opening {secure[0]} sir...")
                        print()
                        webbrowser.open(secure[1])
                        password_correct = True
                    else:
                        print("Access Denied!")













'''
                                           Code Writtne by ChatGPT
                                         -------------------------

import webbrowser

def takeCommand():
    query = input("Enter the command: ")
    print("Recognizing...")
    print()
    print(f"User Said: {query}")
    return query

while True:
    print("Hello sir!")
    password_correct = False  # Flag variable to control the password loop
    while not password_correct:  # Loop until the password is correct
        query = takeCommand()

        secures = [
            ["google", "https://www.google.com"]
        ]

        for secure in secures:
            if f"open {secure[0]}" in query.lower():
                password = input("Enter the password: ")
                print()
                if password == "1234":  # Compare the entered password as a string
                    print("The password is correct.")
                    print()
                    webbrowser.open(secure[1])
                    password_correct = True  # Set the flag to True to exit the password loop
                else:
                    print("Access Denied. Password wrong.")

'''