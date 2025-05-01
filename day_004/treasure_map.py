line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") # Where do you want to put the treasure? i.e a2


letter = position[0].lower()
abc = ['a', 'b', 'c']

letter_index = abc.index(letter)
number_index = int(position[1]) - 1

map[number_index][letter_index] = "x"



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")