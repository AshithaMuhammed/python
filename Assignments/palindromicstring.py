#words=["madam","aba","bcb","hello","python"]
# print palindromic string from the above words
#***************************************************    
  
words=["madam","aba","bcb","hello","python"]     
print("The Palindrome Strings Are :")
for i in range(0,len(words)):
  if words[i]==words[i][::-1]:
    print(words[i])