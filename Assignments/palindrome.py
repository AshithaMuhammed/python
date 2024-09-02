#wrp to check a number palindrome or not



number=int(input("Enter A Number ="))
result=0
origin=number
while(number!=0):                           #123!=0
    digit=number%10                         #123%10=3,
    result=result*10+digit                  #3=3*10+123
    number=number//10
print("palindrome" if result==origin else "not palindrome")
