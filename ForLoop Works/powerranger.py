# #power ranger
# #2=24[2+22])
# 3=369[3+33+333]
# 4=4936[4+44+444+4444]

number=int(input("Enter The Number="))
pattern=0
total=0
for i in range(1,number+1):                
    pattern=pattern*10+number 
    total=total+pattern                       
print(total)                                 





#  print pattern
# ******************************
# number=int(input("Enter The Number="))
# pattern=0
# for i in range(1,number+1):                 #1,2,3
#     pattern=pattern*10+number                #0*10+3=3,0*10+3,0*10+33
#     print(pattern)                         #3,33,333