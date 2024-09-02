#longest Palindrome substring from given string
#RACECAR


text="RACECAR"
     #01234556
longest_palindrom=""
for i in range(0,len(text)):
    left=i
    right=i
    while(left >=0 and right<len(text)and text[left]==text[right]):
        current_palindrom_text=text[left:right+1]
        if len(current_palindrom_text) > len(longest_palindrom):
            longest_palindrom=current_palindrom_text
        print(current_palindrom_text)
        left=left-1
        right=right+1
print(f"the longest palindrome is : {longest_palindrom}")
    
