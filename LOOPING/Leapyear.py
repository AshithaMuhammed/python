#print leap year from 1800 to 2024


year=1800
while(year<=2024):                 #year%400==0
    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
        print(year)
    year=year+1