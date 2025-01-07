Score = int(input("Enter your score: "))
Grade = "F"
if Score >= 90 and Score <= 100:
    Grade = "A"
    print(Grade)
elif Score >= 80 and Score <= 89:
    Grade = "B"
    print(Grade)
elif Score >= 70 and Score <= 79:
    Grade = "C"
    print(Grade)
elif Score >= 60 and Score <= 69:
    Grade = "D"
    print(Grade)
else:
    Grade = "F"
    print(Grade)