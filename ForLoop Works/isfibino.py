Num1=int(input("Enter the number "))
prev=0
current=1
next=prev+current
if_fibo=False
if Num1 in (0,1):
    if_fibo=True
else:
    while(next<=Num1):
        if(next==Num1):
            if_fibo=True
            break
        else:
            next=prev+current
            prev=current
            current=next

print(f"The number {Num1} is fibonacci" if if_fibo==True else f"The number {Num1} is not fibonacci")
