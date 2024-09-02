#Palindrome

num=int(input("Enter Number="))
def is_palindrom(num):
    is_palindrom=False
    result=0
    origin=num
    while(num!=0):
        digit=num%10
        result=result*10+digit
        num=num//10
    if (result==origin):
        is_palindrom=True
    return(is_palindrom)
print(is_palindrom(num))



