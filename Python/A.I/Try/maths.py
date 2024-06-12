'''
def mathsSum(num):
    return (num[0] + num[1] + num[2] + num[3] + num[4] + num[5] + num[6] + num[7] + num[8] + num[9] + num[10] + num[11] + num[12] + num[13]) 

query1 = [5, 5, 5, 5]
Addition = mathsSum(query1)
print(Addition)
'''



# ---------------------------------------------------------------------------------------------------------------------------------

import urllib.parse
import webbrowser

def takeCommand():
    query = input("Enter the value: ")
    return query

while True:
    query = takeCommand()

    maths = [
        ["addition", "+"],
        ["subtraction", "-"],
        ["multipication", "*"],
        ["divistion", "/"],
    ]

    
    if "calculate" in query.lower():
        search_query = query.lower().replace("calculate", "")
        replaced_query = urllib.parse.quote(search_query)
        calculator_url = "https://www.google.com/search?q="
        serach_url = calculator_url + replaced_query
        print(f"Opning {search_query} sir...")
        webbrowser.open(serach_url)


'''

    for math in maths:
        if f"{math[0]}" in query().lower():
            print(f"{math[0]} sir...")
            webbrowser.open(math[1])
'''
