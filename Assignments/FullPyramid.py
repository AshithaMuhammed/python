#Print The Following Pattern Given Below
#Full Pyramid

#             *
#            * *  
#           * * *
#          * * * *
#         * * * * *
#        * * * * * *

for row in range(0,6):
    for col in range(0,5-row):
        print(end=" ")
    for col in range(0,row+1):
        print("*",end=" ")
    
    print()


