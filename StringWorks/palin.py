#create a function is palindrome(word) return true if word is palindromic string
#else return false


# def is_palindrome(word):
#     reversed_str=word[::-1]
#     return word==reversed_str
# print(is_palindrome("sos"))



def reverse(word):
    reversed_str=word[::-1]
    return reversed_str
print(reverse("hello"))





# email_id="ashithamuhd@gmail.com"
# at_index_pos=email_id.index("@")
# user_name=email_id[:at_index_pos]
# print(user_name)
# domain_name=email_id[at_index_pos:]
# print(domain_name)


# text="hello"
# srted_text=sorted(text,reverse=True)
# print(srted_text)