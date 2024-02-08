student_scores = {
    "Alice": [85, 90, 88],
    "Bob": [75, 80, 78],
    "Charlie": [92, 88, 95]
}




student_grades = [student_scores["Alice"],
                  student_scores["Bob"],
                  student_scores["Charlie"]
]

for student, grades in student_scores.items():
    print(student)
    for grade in grades:
        print(grade)
