student_dict = {
    "student": ['Angela', 'James', 'Lily'],
    "score": [56, 76, 98]
}

import pandas
student_frame = pandas.DataFrame(student_dict)

print(student_frame)

for (index, row) in student_frame.iterrows():
    if row.student == 'Angela':
        print(row.score)