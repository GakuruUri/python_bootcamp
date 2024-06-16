"""
try:
except:
else:
finally:
"""

#FileNotFoundError

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdadgbhaj"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError:
    print("That key doesn't exist")
