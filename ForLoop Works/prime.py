#wrp to check a number prime or not

num = int(input("Enter a number: "))
isPrime=True
for i in range(2, num):
    if num%i==0:
        isPrime=False
        break
print(f"{num} is prime" if  isPrime==True else f"{num} is not prime")


