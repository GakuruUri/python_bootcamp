student_scores = input("Enter students scores. ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")



# heights = [100, 2, 300, 10, 11, 1000]
# largest_number = heights[0]
# for number in heights:
#     if number > largest_number:
#         largest_number = number
# print(largest_number)

# highest_score = student_scores[0]
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score
# print(highest_score)
  