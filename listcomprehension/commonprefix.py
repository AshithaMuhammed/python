# words=["fly","float","flower","flat"]
# smallest_word=min(words,key=len)
# common_prefix=""
# for w in words:
#     if smallest_word==words:
#         print(words)
#     else:
#         break
words=["fly","float","flower","flat"]
l = len(words[0])
common_prefix=""
for i in range(1, len(words)):
        length = min(l, len(words[i]))
        while length > 0 and words[0][0:length] != words[i][0:length]:
            length = length - 1
            if length == 0:
                  return 0
    return words[0][0:length]

print(longestCommonPrefix(words))
