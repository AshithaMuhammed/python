#wrp to read start_limit and end_limit from the user 
#  print all the odd numbers from the start_limit to end_limit

start_limit=int(input("Enter Limit ="))
end_limit=int(input("Enter Limit ="))
num=0
for num in range(start_limit, end_limit + 1):
    if num % 2 != 0:
     print(num)
