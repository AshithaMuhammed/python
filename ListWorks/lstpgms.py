# numbers= [1,2,[3,[100,200,300],4],5,6]
# print(len(numbers)) #5
# print(numbers[2])           #[3,[100,200,300],4]

# print(numbers[2][1])        #[100,200,300]
# numbers[2][1].append(500)   #[100,200,300,500]
# print(numbers)              #[1,2,[3,[100,200,300,500],4],5,6]


#**********************************************************************

#wrap to swap first and last elements in a list

# numbers=[1,2,3,4,5,6,7]
# # numbers.pop(0) ,numbers.append(1)
# # print(numbers)

# numbers[-1],numbers[0]=numbers[0],numbers[-1]

# print(numbers)

#***********************************************************

#wrap to return the odd numbers in a list

# num=[1,2,3,4,5,6,7,8]
# odd_num=[]
# for i in num:
#     if i%2!=0:
#         odd_num.append(i)
# print(odd_num)

#**************************************************

# wrap to return the odd numbers in a list
# num=[1,2,3,4,5,6,7,8]
# even_num=[]
# for i in num:
#     if i%2==0:
#         even_num.append(i)
# print(even_num)



num=[1,2,2,3,4,5,3,6,4,7]
for i in num:
    if num.count(i)==1:
        print(i)


# name=["t","h","o","m","a","s"]
# name.sort()
# print(name)

# num=[2,3,6,5,1]
# num.sort()
# num.reverse()
# print(num)


#-----------------------------------------------

# number=[0,2,6,8]
# last=number.pop()
# for n in range(0,last+1):
#     if n%2==0:
#         for n in number(2):
#             break
#         else:
#             print(n)
#Q2:












