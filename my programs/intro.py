name = "ashitha muhammed"
age = 29
course = "mca"
place = "ekm"
print(name.swapcase())
print(course.swapcase())
print(place.swapcase())
print(f"The girl named {name}  age of {age}. she compleated {course} in 2017. she coming from {place}" )
sentence1 = "THIS SHOULD ALL BE LOWERCASE."


#*****************************************************************************

# converts uppercase to lowercase
print(sentence1.swapcase())

sentence2 = "this should all be uppercase."

# converts lowercase to uppercase
print(sentence2.swapcase())

sentence3 = "ThIs ShOuLd Be MiXeD cAsEd."

# converts lowercase to uppercase and vice versa
print(sentence3.swapcase())
#*************************************************************
text = "groß "

# converts text to uppercase
print(text.swapcase()) 

# performs swapcase() on text.swapcase() 
print(text.swapcase().swapcase()) 

print(text.swapcase().swapcase() == text)