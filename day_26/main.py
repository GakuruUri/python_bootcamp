#new_numbers = [new_item for item in list]

"""
conditional list comprehensions
"""
#new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

long_names = [name.upper() for name in names if len(name) > 5]