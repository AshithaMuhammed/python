#Q1:working all except numeric

# from re import finditer
# text="abc 7Klefg@#"
# pattern="\\D"
# matcher=finditer(pattern,text)
# for m in matcher:
#      print(m.start(),"==",m.group())

#Q2:working all except space and special characters
# from re import finditer
# text="abc 7Klefg@#"
# pattern="\\w"
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),"==",m.group())

#Q3:working only space
# from re import finditer
# text="abc 7Klefg@#"
# pattern="\\s"
# matcher=finditer(pattern,text)
# for m in matcher:
#      print(m.start(),"==",m.group())


#Q3:working all without space
from re import finditer
text="abc 7Klefg@#"
pattern="\\S"
matcher=finditer(pattern,text)
for m in matcher:
     print(m.start(),"==",m.group())