f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fileprograms\\news.txt","r")
# word_list=[]
# for line in f:
#     word=line.rstrip("\n")
#     words=word.split(" ")

# word_list=[w for line in f for w in line.rstrip("\n").split(" ")]
# print(word_list)



word_list=[]
for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        word_list.append(w)
word_count={w:word_list.count(w) for w in word_list}
print(word_count)
def get_value(key):
    return word_count.get(key)
srt=sorted(word_count,key=get_value,reverse=True)
print(srt)



