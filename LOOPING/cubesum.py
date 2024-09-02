#read a number print sum of digit
#input=543
#cube sum



num=int(input("Enter The Number"))
total=0
while (num!=0):
    digit=num%10
    exponent=digit**3
    total=total+exponent
    num=num//10
print(total)
    





# i = 1
# while i <= 50:
#     cube = i **3
#     print(f"The cube of {i} is {cube}")
#     i=i+1

# while(num!=0):
#     digit=num%10
#     total=total+digit
#     num=num//10
# print(total)