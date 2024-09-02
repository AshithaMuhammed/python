Num1=int(input("Enter the last number to find fibonacci series "))
prev=0
current=1
print(f"{prev},{current}",end=",")

for i in range (0,Num1+1):
    next=prev+current
    print(f"{next}",end=",")
    prev=current
    current=next
