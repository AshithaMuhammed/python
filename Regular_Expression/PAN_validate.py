# validate pancard number
# first 3 characters are alphabets
# 4th place pcafht
# 5th place alphabet
# 4digit
# 1 alphabet

#AFZPK7190K
from re import fullmatch
PAN_number=input("Enter Number")
pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"
matcher=fullmatch(pattern,PAN_number)
print("invalid" if matcher==None else "valid")


