#create a function is_prime(number) to return true if the number is prime and false if the number is not prime
num=int(input("Enter Number ="))
def is_prime(Num):
    is_prime=True
    for i in range(2,Num):
        
        if Num%i==0:
            is_prime=False
            break
    return(is_prime)

print(is_prime(num))
