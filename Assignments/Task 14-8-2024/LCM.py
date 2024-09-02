number1=int(input("Enter number="))
number2=int(input("Enter Number="))
for i in range (max(number1,number2), 1 + (number1 * number2)):
    if i % number1 == i % number2 == 0:
        lcm = i
        break
print("LCM of", number1, "and", number2, "is", lcm)