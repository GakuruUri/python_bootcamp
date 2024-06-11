import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1, 100) for student in names}

passed_students = {new_key:new_value for (key, value) in dictionary.items()}

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}