num=int(input("Enter The number"))
original=num
total=0
digit_count=len(str(num))
while(num!=0):
    digit=num%10
    exponent=digit**digit_count
    total=total+exponent
    num=num//10
print("Armstrong Number" if original==total else "not armstrong")


