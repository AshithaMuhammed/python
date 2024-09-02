# read 3 numbers from user num1 num2 num3
# print second largest from 3 numbers
#*************************************************

num1=int(input("Enter a Number :"))
num2=int(input("Enter a number :"))
num3=int(input("Enter a number :"))
# if(num1>num2):
#     if(num1>num3):
#         if(num2>num3):
#             print(f"The Second Largest Number is : {num2}")
#         else:     
#              print(f"The Second Largest Number is : {num3}")  
#     else: 
#         print(f"The Second Largest Number is : {num1}")
# elif(num2>num3):
#     if(num3>num1):
#         print(f"The Second Largest Number is : {num3}")
#     else:
#        print(f"The Second Largest Number is : {num1}")
# elif(num2>num1):
#     print(f"The Second Largest Number is : {num2}")
# else:
#      print(f"The Second Largest Number is : {num1}")
if (num1>num2 and num1>num3):
    if (num2>num3):
        print(f"second largest number = {num2}")
    else:
        print(f"second largest number = {num3}")
elif (num2>num3 and num2>num1):
    if (num1>num3):
        print(f"second largest number  = {num1}")
    else:
        print(f"second largest number  = {num3}")
elif (num3>num1 and num3>num2):
    if(num1>num2):
        print(f"second largest number = {num1}")
    else:
        print(f"second largest number = {num2}")



    






