#write a program to calculate  emi
# loan_amount 
# interest
# tenure
import math
loan_amount=100000
Interest=14
tenure=36
Interest_per_month=Interest/12/100

Emi=loan_amount*Interest_per_month*(1+Interest_per_month)**tenure/(((1+Interest_per_month)**tenure)-1) 

#P x R x (1+R)^N / [(1+R)^N-1]
# P = Principal loan amount
# R = Rate of Interest per month ie percentage interest per anum/12/100
# N = Number of instalments every month

# Emi_round=round(Emi)
# Emi_a=math.ceil(Emi)
# Emi_b=math.floor(Emi)
# print(f"The emi for a loan amount of {loan_amount} for an Interest of {Interest}% for {tenure} month is {Emi}")
# print(f"Rounded Emi per month is {Emi_round} , {Emi_a} and {Emi_b}")

print(f"The emi for a loan amount of {loan_amount} for an Interest of {Interest}% for {tenure} month is {round(Emi)}")

# Total_payable_amount=Emi*tenure
# print(f"Monthly Emi={Emi}")

# print(f"Total Payable Amount={Total_payable_amount}")

# Total_intrest_payable=Total_payable_amount-loan_amount

# print(f"Total interest payable amount={Total_intrest_payable}")


Total_payable_amount=round(Emi)*tenure
print(f"Monthly Emi={round(Emi)}")

print(f"Total Payable Amount={Total_payable_amount}")

Total_intrest_payable=Total_payable_amount-loan_amount

print(f"Total interest payable amount={Total_intrest_payable}")