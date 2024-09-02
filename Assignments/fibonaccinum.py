#fibonacci
num=int(input("Enter Number ="))
def is_fib(num):
    prev=0
    current=1
    next=prev+current
    is_fib=False
    if num in (0,1):
        is_fib=True
    else:
        while(next<=num):
            if (next==num):
                is_fib=True
                break
            else:
                prev=current
                current=next
                next=prev+current
    return(is_fib)
print(is_fib(num))
