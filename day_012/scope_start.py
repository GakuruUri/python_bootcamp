# ################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local scope



# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()
# #print(potion_strength)


# # Global scope

# player_health = 10

# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(player_health)
#   drink_potion()

# print(player_health)


# # There is no block scope
# if 3 > 2:
#   a_variable = 10


# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#   new_enemy = enemies[0]

# print(new_enemy)



# game_level = 3
# def create_enemy():
#   enemies = ["Skeleton", "Zombie", "Alien"]
#   if game_level < 5:
#     new_enemy = enemies[0]
  
#   print(new_enemy)
  
  
  # Modifying global scope
  
enemies = "skeleton"

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
  