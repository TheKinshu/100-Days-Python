import random
name = ['Alex', 'Beth', 'Eric', 'Jonn', 'Amber']

students_scores = {student:random.randint(1,100) for student in name}

print(students_scores)


passed_students = {student:score for (student, score) in students_scores.items() if students_scores[student] > 60}

print(passed_students)