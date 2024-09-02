#wrp to print sum of all odd numbers from 1 to 100


sum=0
for num in range(1,100):
    if num% 2 != 0:
        sum += num
print("sum of all odd numbers from 1 to 100 :",sum)
