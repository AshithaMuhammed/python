# def merged_strings(word1,word2):
#     return word1+word2
# word1="PQR"
# word2="ABC"
# merged_string=merged_strings(word1,word2)
# print("merged string:", merged_string)
#************************************************



# word1="PQR"
# word2="ABC"
# merged_string=""
# for i in range(0,len(word1)):
#     merged_string=merged_string+word1[i]+word2[i]
# print(merged_string)

#*************************************************


word1="PQRS"
word2="ABCDEFG"

smallest_word=word1 if len(word1) < len(word2) else word2
merge_string=" "
for i in range(0,len(smallest_word)):
    merge_string=merge_string+word1[i]+word2[i]
if len(word1) > len(word2):
    balance=word1[len(smallest_word):]
else:
    balance=word2[len(smallest_word):]
merge_string=merge_string+balance
print(merge_string)