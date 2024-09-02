
# --------------------------------  
# #duplicates not allowed
#elements are unordered
#it doesnt have index position
#mutable
#-----------------------------------------------

#to add an element to a set object
# names={"hari","hello","chennai","hari"}
# names.add("kochi")
# print(names)
#---------------------------------------------
 #to remove all elements from the object emptly set remains
# names={"hari","hello","chennai","hari"}
# names.clear()
# print(names)
#----------------------------------------------------

#to remove a random element from a set

# names={"hari","hello","chennai","hari"}
# names.pop()
# print(names)

#-----------------------------------

#removing an element from the set if its a member in the object

# names={"hari","hello","chennai","hari","kollam"}
# names.discard("hello")
# print(names)

#--------------------------------------------------

# to add element from any collection to the set
# names={"hari","hello","chennai","hari"}
# new_names=["hp","dell","lenovo"]
# names.update(new_names)
# print(names)
#-------------------------------------------------

#combined 2 sets and returned a new one
# names={"hari","hello","chennai","hari","hp"}
# new_names={"hp","dell","lenovo"}
# new_set=names.union(new_names)
# print(new_set)
#-------------------------------------------

#combined common elements from two sets returned new one
# names={"hari","hello","chennai","hari","hp"}
# new_names={"hp","dell","lenovo",}
# new_set=names.intersection(new_names)
# print(new_set)
#----------------------------------------------

#returned difference of two sets and retunrned as a new set

# names={"hari","hello","chennai","hari","hp"}
# new_names={"hp","dell","lenovo",}
# new_set=names.difference(new_names)
# print(new_set)
#--------------------------------------------------

#combine all elements from 2 sets and remove common elements
names={"hari","hello","chennai","hari","hp"}
new_names={"hp","dell","lenovo",}
new_set=names.symmetric_difference(new_names)
print(new_set)
