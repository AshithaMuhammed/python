#print the following pattern given below
#Half Pyramid
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *



for row in range(0,6):
    for col in range(0,row+1):
         print("*",end="\t")
    print()