#wrp to read start_limit and end_limit from the user 
#  print all the odd numbers from the start_limit to end_limit



start_limit = int(input("Enter the start limit: "))
end_limit = int(input("Enter the end limit: "))

i = start_limit
while i <= end_limit:
    if i % 2 != 0:
        print(i)
    i += 1





