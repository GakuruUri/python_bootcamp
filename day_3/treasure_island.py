print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? Type "Left" or "Right".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. "
                        "One red, one yellow, one blue. which color do you choose?\n").lower()
        
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game over!")
        else:
            print("You choose a door that doesn't exist. Game over.")
            
    else:
        print("You get attacked by an angry trout. Game over!")
else:
    print("You fell into a hole and died. Game over!")












# print('''
#                              __.------.                          
#                       (__  ___   )                         
#                         .)e  )\ /                          
#                        /_.------                           
#                        _/_    _/                           
#                    __.'  / '   `-.__                       
#                   / <.--'           `\                     
#                  /   \   \c           |                    
#                 /    /    )  GoT  x    \                   
#                 |   /\    |c     / \.-  \                  
#                 \__/  )  /(     (   \   <>'\               
#                      / _/ _\-    `-. \/_|_ /<>             
#                     / /--/,-\     _ \     <>.`.            
#                     \/`--\_._) - /   `-/\    `.\           
#                      /        `.     /   )     `\          
#                      \      \   \___/----'                 
#                      |      /    `(                        
#  ___________         \    ./\_   _ \                       
#    ______________    /     |  )    '|                      
#  __________________ |     /   \     \     ___________a:f   
#                    /     |     |____.)                     
#                   /      \  a88a\___/88888a.               
#                  \_      :)8888888888888888888a.           
#                 /` `-----'  `Y88888888888888888            
#                 \____|         `88888888888P'              
                                                           
                                                   
#       ''')

# print("Welcome to treasure island.")
# print("Your mission is to find the treasure.")

# direction = input("Which way do you want to go, left or right? ").lower()
# if direction == "left":
#     print("You find a lake.")
#     lake = input("What do you want to do, swim or wait for a boat? ").lower()
#     if lake == "wait":
#         print("You cross the lake and find a house with 3 doors.")
#         door = input("Which door do you choose, red, blue or yellow? ").lower()
#         if door == "yellow":
#             print("You found the treasure!")
#         else:
#             print("That's not good, the room if bobby trapped, Game over!")
#     else:
#         print("You are eaten by the Kraken, Game over!")
# else:
#     print("You are met by robbers and thieves, Game over!")