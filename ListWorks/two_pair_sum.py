arr=[2,3,4,5]
# result=6
#(2,4)
result=6
for i in range(0,len(arr)):
 for j in range(i+1,len(arr)):
        if result==arr[i]+arr[j]:
            print(arr[i],arr[j])
