num1=int(input("Enter a Number :"))
num2=int(input("Enter a number :"))
num3=int(input("Enter a number :"))
if(num1>num2):
    if(num1>num3):
        if(num2>num3):
            print(f"The Sequence In Ascending Order Is : {num1} > {num2} > {num3}")
        else:
             print(f"The Sequence In Ascending Order Is : {num1} > {num3} > {num2}")  
    else: 
        print(f"The Sequence In Ascending Order Is : {num3} > {num1} > {num2}")
elif(num2>num3):
    if(num3>num1):
        print(f"The Sequence In Ascending Order Is : {num2} > {num3} > {num1}")
    else:
       print(f"The Sequence In Ascending Order Is : {num2} > {num1} > {num3}")
elif(num2>num1):
    print(f"The Sequence In Ascending Order Is : {num3} > {num2} > {num1}")
else:
     print(f"The Sequence In Ascending Order Is : {num3} > {num1} > {num2}")



# if num1>num2 and num1>num3:
#     print(f"Largest number ={num1}")
# elif num2>num1 and num2>num3:
#     print(f"Largest number ={num2}")
# elif num3>num1 and num3>num2:
#     print(f"Largest number ={num3}")

