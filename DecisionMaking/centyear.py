#read a year from user and
#print Century Year if year ends with two zeros
#else print non century year 

year = int(input("Enter Year:"))
if year%100 == 0:
        print(f"{year}century year")

else:
        print(f"{year}non century year")