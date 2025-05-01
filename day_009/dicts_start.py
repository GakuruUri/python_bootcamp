programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
  
}


#Retrieving items from dictionary.
print(programming_dictionary["Bug"])


#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

empyt_dictionary = {}

#Add items to an empty discctionary.
empyt_dictionary["Loop"] = "The action of doing something over and over again."
empyt_dictionary["Sum"] = "The action of adding two numbers."

# Wipe out an entire dictionary.

programming_dictionary = {}
print(programming_dictionary)

# Editing an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

print(programming_dictionary)

# looping through a dictionary
# the below just gives you the key
for i in programming_dictionary:
  print(i)
  
  
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

# Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
  "Spain": "Madrid",
}


# Nesting a list in a dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# Nesting a dictionary in a dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Dijon", "Lille"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgurt"], "site_visited": "Bayern"}
}


# Nesting dictionaries inside lists
travel_log = [
  {
    "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12
  },
  
  {
    "country": "Germany", 
  "cities_visited": ["Berlin", "Hamburg", "Stuttgurt"], 
  "total_visits": 5
  },
  
  {
    "country": "Spain", 
  "cities_visited": ["Madrid", "Barcelona", "Valencia"], 
  "total_visits": 6
  }
]