#wrp to calculate
#monthly Emi
#Total Payment
#Total Interest payable
#Read Loan amount ,tenure ,Interest rate from the user

#****************************************************************


Loan_amount=int(input("Enter Loan Amount :"))
Tenure=int(input("Enter Total Duration of Time : "))
Interest=int(input("Enter The Interest Rate :"))
Interest_per_month=Interest/12/100
Emi=round(Loan_amount*Interest_per_month*(1+Interest_per_month)**Tenure/(((1+Interest_per_month)**Tenure)-1))
print(f"EMI ={Emi}  ")
Total_payable_amount=round(Emi)*Tenure
print(f"Total Payable Amount={Total_payable_amount}")

Total_intrest_payable=Total_payable_amount-Loan_amount

print(f"Total interest payable amount={Total_intrest_payable}")