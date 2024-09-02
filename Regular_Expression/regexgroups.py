
# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[abf]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q:check a-z lowecase
# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[a-z]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q:check A-Z uppercase
# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[A-Z]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())



#Q: a-zA-Z pattern for matching all alphabets
# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[a-zA-Z]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())


#Q:pattern a-zA-Z0-9

# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[a-zA-Z0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q:pattern 0-9

# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q:pattern ALL 

# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[^0-9]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())


#Q:patter=[^a-zA-Z0-9\s]

# from re import finditer
# text="abc123 @k#7LMdef"
# pattern="[^a-zA-Z0-9\s]"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q:pattern \s
from re import finditer
text="abc123 @k#7LMdef"
pattern="[\s]"
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),"==",m.group())
