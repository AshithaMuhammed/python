# f=open("C:\\Users\\\user\\Desktop\\PythonJuneWorks\\fileprograms\\years.txt","w")
# for year in  range(1800,2025):
#     f.write(str(year)+"\n")


f_read=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\years.txt","r")
f_century=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\year_century.txt","w")
f_non_century=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\year_noncentury.txt","w")

for year in f_read:
    y=int(year.rstrip("\n"))

    if y % 100 == 0:
        f_century.write(str(y)+"\n")
    else:
        f_non_century.write(str(y)+"\n")
