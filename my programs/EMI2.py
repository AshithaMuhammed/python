import math
loan_amount=2000000
interest=10
tenure=60
interest_per_month=interest/12/100               #P x R x (1+R)^N / [(1+R)^N-1]
EMI=loan_amount*interest_per_month*(1+interest_per_month)**tenure/((1+interest_per_month)**tenure-1)
print(f"the  loan amount of {loan_amount} for a Tenure of {tenure} months where the interest rate charged {interest}% emi is {round(EMI) } ")     #if you avail a loan of Rs.20 lakh for a tenure of 5 years where the interest rate charged is around 10%

Total_payable_amount=EMI*tenure
print(f"total amount paid is {round(Total_payable_amount)}")

Total_interest_payable=Total_payable_amount-loan_amount
print(f"total interest paid is {round(Total_interest_payable)}")

