# #wrp to find GCD of 2 numbers
# num1 =int(input("Enter Number ="))
# num2 =int(input("Enter Number ="))
# gcd = 1
# for i in range(1,num1+1):
#         if num1 % i == 0 and num2 % i == 0:
#             gcd = i

# print(f"The GCD of {num1}and {num2}"is f" gcd(num1, num2)")



# #1,,,,,,,,,,,,,smallest_number

# def gcd(a, b):
#     for i in range(min(a, b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i
#     return 1

# print(gcd(16, 24))


num1=int(input("Enter Number1="))
num2=int(input("Enter Number2="))
gcd=1
for i in range(1,num1+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(f"gcd of{num1},{num2},={gcd}")
