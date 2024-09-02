#   take words end with at


from re import findall
text="the fat cat run very fast to catch rat the fall into a mat"
pattern=".at"
matcher=findall(pattern,text)
print(matcher)