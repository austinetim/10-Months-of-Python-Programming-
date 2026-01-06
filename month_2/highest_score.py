#This program calculates the highest score of students without employing the max() or min() fuctions.

student_scores = input("Input a list of students scores:  ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    print(student_scores[n])
# Initialize a highest score tracker
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")
    