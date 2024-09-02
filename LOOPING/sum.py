#wrp find sum of start to end sum

start=10
end=15
total=0
while(start <= end):                #10<=15,11<=15,12<=15,13<=15
    total=total+start               #0+10,10+11=21,12+21,32+13,
    start=start+1                    #10+1=11,12,13,14
print(total)

    