# 1st character upper case alphabet
# next character is a digit from 1-9
# next digit 0-9
#  4th place 0 or 1 space 
# next 4 characters any number from 0-9
# last character 1-9


from re import fullmatch
passport=input("Enter The Passport Number ")
pattern="[A-Z][1-9][0-9][0\\s]\\d{4}[1-9]"
matcher=fullmatch(pattern,passport)
print("invalid" if matcher==None else "valid")
