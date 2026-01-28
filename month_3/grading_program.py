 # This program calculates the grades of students based on their scores

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Create another dictionary called 'student_grade'

student_grades = {}

# Loop through the student scores dictionary
# for student in student_scores:
#     grade = ""
#     if (student_scores[student] >= 91):
#         grade = "Outstanding"
#     elif (student_scores[student] >= 81):
#         grade = "Exceeds expectation"
#     elif (student_scores[student] >= 71):
#         grade = "Acceptable"
#     else:
#         grade = "Fail"
#     student_grades[student] = grade

# Method 2

# for student in student_scores:
#     if (student_scores[student] > 90):
#         student_grades[student] = "Outstanding"
#     elif (student_scores[student] > 80):
#         student_grades[student] = "Exceeds expectation"
#     elif student_scores[student] > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# Method 3

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
# print the dictionary
print(student_grades)