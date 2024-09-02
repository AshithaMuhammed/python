# student={"name":"ashitha","course":"fullstack"}
# print(student.keys())

# student={"name":"ashitha","course":"fullstack"}
# student["name"]="yamir"        #update
# print(student)

# student={"name":"ashitha","course":"fullstack"}
# student["place"]="kochi"   #add new key
# print(student)

# student={"name":"ashitha","course":"fullstack"}
# student["place"]="kochi"
# new=student.items()
# print(new)

# student={"name":"ashitha","course":"fullstack","course":"datascience"}
# student["place"]="kochi"
# new=student.items()  #key will overwrite
# print(new)



#------------------------------------------------------

# student={"name":"ashitha","course":"datascience"}
# for i in student:
#     print(f"{i} = {student[i]}")

#------------------------------------------------
#wrp the course as fullstack in student in iteration
# student={"name":"ashitha","course":"datascience"}
# for i in student:
#     if i=="course":
#         student[i]="fullstack"
# print(student)
# #--------------------------------------------

# #delete a key 'place' if it is inthe dict using iteration

# student={"name":"ashitha","course":"datascience","place":"kochi"}
# for i in list(student):
#      if place[i]:
#         new= student.pop(i)
# print(new)



