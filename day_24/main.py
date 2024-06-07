# # file = open("my_file.txt")
# """
# Reading a file
# """
# with open("my_file.txt") as file: # by adding the with and as keywords, we don't have to close the file.
#     # The with key word manages the file and notices when we're done with it, and it closes it.
#     contents = file.read()
#     print(contents)
# # file.close()


"""
Writing to a file
# """
# with open("my_file.txt", mode="w") as file: # To write to a file you have to change the mode from
#                                             # read only default to write.
#     file.write("New text.")
#
# # You can use the "a" option to append instead of "W which overwrites.
# with open("my_file.txt", mode="a") as file:
#     file.write("New Shit!")


with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


with open("new_file.txt", mode="w") as file:
    file.write("New Shit!")