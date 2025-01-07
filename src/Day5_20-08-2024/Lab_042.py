Score = int(input("Enter your score: "))
Grade = "F"
if 90 <= Score <= 100:
    Grade = "A"
    print(Grade)
elif 80 <= Score <= 89:
    Grade = "B"
    print(Grade)
elif 70 <= Score <= 79:
    Grade = "C"
    print(Grade)
elif 60 <= Score <= 69:
    Grade = "D"
    print(Grade)
else:
    Grade = "F"
    print(Grade)