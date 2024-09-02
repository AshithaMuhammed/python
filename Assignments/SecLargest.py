num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))
num3=int(input("Enter num3 :"))
if num1>num2 and num1>num3:                                         #num1 is largest
  if num2>num3:                                                #psblty 4 2nd largest num2 or num3
     print(f"The Second largest number = {num2}")
  else:
     print(f"The Second largest number = {num3}")


elif num2>num1 and num2>num3:                                 #num2 is largest
  if num1>num3:                                                  #psblty 4 2nd largest num1 or num3
    print(f"The Second largest number = {num1}")
  else:
    print(f"The Second largest number = {num3}")


elif num3>num1 and num3>num2:   
  if num1>num2:                                                                   #num3 is largest
    print(f"The Second largest number = {num1}")                         #psblty 4 2nd largest num1 or num2
  else:
    print(f"The Second largest number = {num2}")
                                                      
elif num1==num2==num3:
    print(f"Three Numbers are Equal")

