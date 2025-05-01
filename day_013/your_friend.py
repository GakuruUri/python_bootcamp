# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page

# Add print statements for debugging
print(f"Pages = {pages}.")
print(f"Words per page = {word_per_page}.")

print(total_words)