
school = input()

student_list = []
for class_group in school:
    for student in class_group:
        student_list.append(student)

print(student_list)
