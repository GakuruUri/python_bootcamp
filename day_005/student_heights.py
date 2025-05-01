# Input a list of student heights
student_heights = input("Enter a list of student heights:").split()
print(student_heights)

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
    
total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height = {total_height}")


number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"Average height = {average_height}")

