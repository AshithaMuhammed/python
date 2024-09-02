text="ABCCDDBB"
word_count={}
for c in text:
    if c in word_count:
        print(c,"first recursive character")
        break
    else:
     word_count[c]=1


# text="ABCCDDBB"
# word_count={}
# for char in text:
#     if char in word_count:
#         print(char,"first recursive character")
#         break
# else:
#     word_count[char]=1
