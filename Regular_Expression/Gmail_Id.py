# Q2:VALIDATE GMAILID
# 1st alphanumeric
#  [a-zA-Z0-9._]
#   @gnail.com

from re import fullmatch
Gmail_id=input("Enter Mail Id")
pattern="\\w[\\w._]*@gmail.com"
matcher=fullmatch(pattern,Gmail_id)
print("invalid" if matcher==None else "valid")