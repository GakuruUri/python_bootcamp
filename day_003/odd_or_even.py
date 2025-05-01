# Which number do you want to check.
number = float(input("Enter number you want to test. "))


# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
    print(f"The Number {number} is even")
# Otherwise number cannot be divided by 2 with 0 remainder
else:
    print(f"The Number {number} is odd.")