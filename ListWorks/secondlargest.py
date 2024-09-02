#Q:wrp to find secondlargest number
# number=[3,2,5,7,1,9,10,4]
# number.sort()
# print(number[-2])

#********************************************


number=[1,2,5,7,1,11,10,4]
largest_num = number[0]
second_largest=0
for i in number:
    print(i)
    if i >second_largest and i >largest_num:
        second_largest=largest_num
        print(second_largest)
        largest_num= i
        print(largest_num)
    elif i >second_largest and i <largest_num:
        second_largest=i
    print(f"second largest number= {second_largest}") 