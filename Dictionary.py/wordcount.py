# words=["hello","hai","hello","hai","hi","hello"]
# hello_count=words.count("hello")
# print("The Word hello in the list=",hello_count)


#-----------------------------------2nd approach

# words=["hello","hello","hi","hello","hai","hai"]
# word_count={}
# for w in words:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)
#------------------------------------ home work
numbers=[12,22,15,87,22,12,13,12,87,22]
num_count={}
for n in numbers:
    if n in num_count:
        num_count[n]+=1
    else:
        num_count[n]=1
print(num_count)