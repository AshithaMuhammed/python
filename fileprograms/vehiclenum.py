vehicle_numbers=[
    "KL668844",
    "AP849217",
    "MP125294",
]
f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\vehicles.txt","w")
for number in vehicle_numbers:
      f.write(number+"\n")