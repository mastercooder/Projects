import os
import subprocess



def takeCommand():
    query = input("Enter your command: ")
    print(f"User Said: {query}")
    return query
query = takeCommand()

'''
# 1 WAY (NOT WORKING)
def open_windows_settings():
    os.startfile("ms-settings:")

if "open setting" in query.lower():
    if __name__ == "__main__":
        open_windows_settings()
'''

# 2 WAY (WORKING)
def open_windows_apps():
    
    if "open setting" in query.lower():
        subprocess.run("start ms-settings:", shell=True)

    if "open edge" in query.lower():
        subprocess.run("start ms-photos:", shell=True)
    '''
    subprocess.run("start ms-:", shell=True)
    subprocess.run("start ms-:", shell=True)
    '''

if "open setting" in query.lower():
    if __name__ == "__main__":
        open_windows_apps()

if "open photos" in query.lower():
    if __name__ == "__main__":
        open_windows_apps()
