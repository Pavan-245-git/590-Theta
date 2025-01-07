students = {
    1 : {"name": "google","age":14},
    2 : {"name": "deloite","age":20},
    3 : {"name": "pavan","age":20},
    4 : {"name": "super","age":18},

}

for student_id, details in students.items():
    print(f"Student ID:  {student_id}, Name: {details['name']}, Age:{details['age']}")
