# Sum of all even numbers
target = int(input("Enter a number between 1 and 1000"))

even_sum = 0
for number in range(2, target + 1, 2):
    # Accumulate even sum here
    even_sum += number
print(even_sum)

# Or

# Sum of all odd numbers

alternative_sum = 0

for number in range(1, target +1):
    if number % 2 != 0:
        alternative_sum += number
print(alternative_sum)