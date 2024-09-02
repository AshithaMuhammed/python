#Q:same lowercase alphabets with 3
# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[a-z]{3}"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())


#Q:same ditis with 3
# from re import finditer
# text="abc123 @k#7LMdef678"
# pattern="[0-9]{3}"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q:alphabet with digit
# from re import finditer
# text="abc123 @k#7LMdef678"
# pattern="[a-z0-9]{3}"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q:c-h or t-z
# from  re import finditer
# text="abc123 @k#7LMdef678"
# pattern="([c-h]|[t-z])"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q:special only
from  re import finditer
text="abc123 @k#7LMdef678"
pattern="[^a-zA-Z0-9\s]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"==",m.group())


#Q:same groups
# from  re import finditer
# text="abc123 @k#7LMdef678"
# pattern="([a-z]{3}|[0-9]{3})"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())