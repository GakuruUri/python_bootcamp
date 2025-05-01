names = ["Uri", "Jane", "Peter", "Albert", "Henry"]
# names = names.string.split(", ")

import random

# Get the total number of items on the list
num_items = len(names)

# Generate random numbers between 0 and last index.
random_choice = random.randint(0, num_items - 1)

# Pick out random person from the list of names using a random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

