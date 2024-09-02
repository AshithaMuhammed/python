from re import fullmatch
f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\Regular_Expression\\domain.text")
pattern="[\w\w]+\\.com"

for line in f:
    domain=line.rstrip("\n")
    matcher=fullmatch(pattern,domain)
    if matcher !=None:
        print(domain)