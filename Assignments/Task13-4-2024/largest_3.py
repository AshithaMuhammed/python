#Q6:largest of three numbers
num1=int(input("Enter The First Number="))
num2=int(input("Enter The Second Number="))
num3=int(input("Enter The Third Number="))
if num1>num2 and num1>num3:
    print(f"{num1} Is The Largest Number")
elif num2>num3 and num2>num1:
    print(f"{num2} Is The Largest Number")
elif num3>num2 and num3>num1:
    print(f"{num3} Is The Largest Number")
else:
    print("All Numbers Are Same")