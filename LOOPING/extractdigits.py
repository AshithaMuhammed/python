#read a number and extract digits from number
#sample input1 num=123


num=int(input("Enter The Number"))
while(num!=0):
    digit=num%10
    print(digit)
    num=num//10
    