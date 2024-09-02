#speed=distance/time
#read distance and time print speed

# Distance= float(input("Enter The Distance In KM :"))
# Time= int(input("Enter The Time Take In Hours :"))
# Speed=Distance/Time
# print(f"Speed={Speed} km/hr")


#wrp to Enter Distance In Meter and Time In Minutes
#find The Speed In km/hr and m/s
#Also Ask To Continue Or Not

Dis_m=float(input("Enter The Distance in Meter :"))
Time_m=int(input("Enter The Time In Minutes :"))
Dis_km=Dis_m/1000
Time_hr=Time_m/60
Time_Sec=Time_m*60
Speed_kmh=Dis_km/Time_hr
Speed_mps=Dis_m/Time_Sec
print(f"Your Speed is : {Speed_kmh} km/hr and {Speed_mps} m/s")