# list_of_strings = [9 0 32 8 2 8 64 29 42 99].split()','

# List comprehension to convert strings to integers
convert = [int(n) for n in list_of_strings]

# list comprehension to filter on even numbers
result = [num for num in convert if num % 2 == 0]

print(result)


list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
converted = [int(n) for n in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [x for x in converted if x % 2 == 0]

# Write your code 👆 above:
print(result)