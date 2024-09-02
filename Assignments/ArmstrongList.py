# Q:print amstrong numbers from given numbers

numbers=[151,153,154,370,371,372,373,1634,1635]
print("The amstrong numbers are: ")
for i in range(0,len(numbers)):
    total=0
    num=numbers[i]
    count=len(str(num))     
    while(num!=0):
        digit=num%10
        sum=digit**count
        total=total+sum
        num=num//10
    if numbers[i]==total:
        print(numbers[i])



    













#     #total=0
#     digit_count=len(str(num))
#     while(num!=0):
#         digit=num%10
#         sum=digit**digit_count
#         total=total+sum
#         num=num//10
#     if total==original:
#         is_armstrong=True
#     return(is_armstrong)
# print(is_armstrong(num))

