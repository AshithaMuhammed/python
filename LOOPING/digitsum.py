#read a number print sum of digit
# #input=543
# output=12


num=int(input("Enter Number"))
total=0
while(num!=0):
    digit=num%10
    total=total+digit
    num=num//10
print(total)