students=[
        {"id":100,"name":"vipin","course":"django","mark":450},
        {"id":101,"name":"hari","course":"testing","mark":470},
        {"id":100,"name":"ashitha","course":"mern","mark":490},
        {"id":100,"name":"yamir","course":"php","mark":420},
]

student_name=[st.get("name")for st in students]
print(student_name)
all_course={st.get("course")for st in students}
print(all_course)