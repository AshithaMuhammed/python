weight_in_kg=int(input("Enter The Weight In kg :"))
height_in_cm=int(input("Enter The Height In cm :"))
height_in_meter=165/100
bmi=weight_in_kg/height_in_meter**2
print(f"bmi={bmi}")
if(bmi<19):
    print(f"You Are In Under Weight")
elif(bmi<=25):
    print(f"You Are In Normal Weight")
elif(bmi<=30):
    print(f"You Are In Over Weight")
else:
    print("obesity")

# if bmi <19 :
#     print(f"under weight")
# elif bmi>=19 and bmi<25:
#     print("normal weight")
# elif bmi>=25 and bmi<30:
#     print("over weight")
# else:
#     print("obesity")
