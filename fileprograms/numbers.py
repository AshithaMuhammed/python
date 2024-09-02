f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\num_process.py","r")
f_odd=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\numodd.txt","w")
f_even=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\numeven.txt","w")
n=[1,2,3,4,5,6,7,8,9,10]
for number in f:
   n=int(number.rstrip("\n"))
   if n % 2 == 0:
       f_even.write(str(n)+"\n")
else:
       f_odd.write(str(n)+"\n")
print(n)

