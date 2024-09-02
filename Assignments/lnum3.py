# read 3 nmbrs from user num1 num2 num3
# print largest among the three numbers
#**********************************************

num1=int(input("Enter a Number :"))
num2=int(input("Enter a number :"))
num3=int(input("Enter a number :"))
if(num1>num2):
    if(num1>num3):
     print(f"The Largest Number is : {num1}")
elif(num2>num3):
     if(num2>num1):
      print(f"The Largest Number is : {num2}")
elif(num3>num2):
     if(num3>num1):
      print(f"The Largest Number Is : {num3}")
else:
   print(f"default stmt")
