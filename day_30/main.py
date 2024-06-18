"""
try:
except:
else:
finally:
"""


try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:   # This runs when the try runs successfully.
    content = file.read()
    print(content)

finally:    # This runs no matter what
    file.close()
    print("File was closed.")


