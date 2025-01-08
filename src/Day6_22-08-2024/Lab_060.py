person = input("Enter who is the person\n")
match person:
    case "Admin":
        print("Hello, Admin!")
    case "Guest":
        print("Hello, Guest!")
    case _:
        print("Hello, There!")