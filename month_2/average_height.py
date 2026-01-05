#This program calculates the average heights of students without employing the sum() and len() fuctions.

students_heights = input("Input a list of students heights:  ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
    print(students_heights[n])

total_height = 0
for height in students_heights:
    total_height += height
print(total_height)

number_of_students = 0
for students in students_heights:
    number_of_students += 1
print(number_of_students)

average_height = total_height/number_of_students
print(average_height)

# # Use the math below to confirm the result in your code
# sum_of_num = 45 + 56 + 78 + 90 + 43 + 26
# print(sum_of_num/6)