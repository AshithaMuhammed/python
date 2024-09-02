# Q:wrp to find the largest num

# num=[1,3,2,5,7,9,10,4]
# num.sort()
# print(f"the largest number = ",num[-1])


num=[1,3,2,5,7,9,10,4]
largest_num=num[0]
for i in num:
    if i>largest_num:
        largest_num=i
print(f"The Largest Number={largest_num}")