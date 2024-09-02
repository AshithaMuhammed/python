# from re import fullmatch
# variable_name=input("enter name ")
# pattern="[a-zA-Z][a-zA-Z0-9_]*"
# matcher=fullmatch(pattern,variable_name)
# print("invalid" if matcher==None else "valid")



# Q:variablename
# first character must be k-m
# second character must be /3
# followed by any numbr of alphabets and number @
from re import fullmatch
# variable_name="k6abc123@"
variable_name=input("Enter Name ")
pattern="[k-m][369][a-zA-Z0-9@]*"
matcher=fullmatch(pattern,variable_name)
print("invalid" if matcher==None else "valid")

