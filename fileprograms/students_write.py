f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\students.txt","r")
students=[]
for stud in f:
    students.append(stud.rstrip("\n"))
print(students)