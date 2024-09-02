#read a number from user
#print fizz if num is / by 3
#print buzz if num is / by 5
#print fizzbuzz if num is / by 15


num=int(input("Enter The Number :"))
if num %3 ==0:
    print("fizz")
elif num %5 ==0:
    print("Buzz")
elif num %15 ==0:
    print("fizzBuzz")

else:
    print("INVALID")

