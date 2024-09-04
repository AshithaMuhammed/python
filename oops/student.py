class student:
    name:str
    id:str
    gender:str
    age:str
    course:str
    contact:str
    address:str
    def set_student(self,id,name,gender,age,course,contact,address):
        self.id=id
        self.name=name
        self.gender=gender
        self.age=age
        self.course=course
        self.contact=contact
        self.address=address
    def display_student(self):

        print(self.id,self.name)
student_instance=student()
student_instance.set_student(100,"hari","male",29,"django",1244656458,"avd")
student_instance.display_student()


