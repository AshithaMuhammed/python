# print 2 numbers num1 num2
# print largest of 2 numbers
# if both are equal print both are equal
#*********************************************
num1=int(input("Enter Number1 :"))
num2=int(input("Enter Number2 :"))
if(num1>num2):
    print(f"The Largest Number is : {num1}")
elif(num2>num1):
    print(f"The Largest Number is :{num2}")
elif(num1==num2):
    print(f"Both Numbers Are Equal")
else:
    print("default stmt")

