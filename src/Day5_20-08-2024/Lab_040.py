num1 = int(input("Enter the Number1\n"))
num2 = int(input("Enter the Number2\n"))
num3 = int(input("Enter the Number3\n"))

if num1 > num2 and num1 > num3:
    print(f"Max is {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Max is {num2}")
else:
    print(f"Max is {num3}")

result = max(num1,num2,num3)
print(result)