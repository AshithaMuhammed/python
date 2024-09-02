#Armstrong
num=int(input("Enter Number="))
def is_armstrong(num):
    is_armstrong=False
    original=num
    total=0
    digit_count=len(str(num))
    while(num!=0):
        digit=num%10
        sum=digit**digit_count
        total=total+sum
        num=num//10
    if total==original:
        is_armstrong=True
    return(is_armstrong)
print(is_armstrong(num))

