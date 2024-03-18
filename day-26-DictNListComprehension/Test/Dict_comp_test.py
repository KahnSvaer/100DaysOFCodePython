import random

names = 'Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie'
students_score = {name: random.randint(0, 100) for name in names}
print(students_score)

passed_students = {name: result for (name, result) in students_score.items() if result>50}
print(passed_students)
