# Match statement
# It will match the O/p & execute
from difflib import Match

browser = input("Enter the browser name\n")
match browser:
    case "Chrome":
        print("Ok")
    case "Edge":
        print("Ok")
    case "Firefox":
        if browser == "Firefox":
            print("Sorry! You can't use this browser")
        print("No")
