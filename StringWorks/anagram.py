def  is_anagram(source_word,target_word):
    return sorted(source_word)==sorted(target_word)
source_word=input("Enter The First String :")
target_word=input("Enter The Second String :")
if is_anagram(source_word,target_word):
    print("The Strings are anagrams")
else:
    print("The Strings are not anagrams")
