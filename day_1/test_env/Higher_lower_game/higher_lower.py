import random
from art import logo, vs
from game_data import data
import os

## TODO 3: Format the account data into a printable format.

def format_data(account):
    """ Format the account data into a printable format."""
    account_name =  account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, from {account_country}"

## TODO 7: Use if statements to check if user is correct

def check_answer(guess, a_follower, b_follower):
    """Takes the user input and follower count and returns true if they got the answer."""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

## TODO 1: Display art

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(date)

## TODO 10: Make the game repeatable

while game_should_continue:
    ## TODO 2: Generate a random account from game data
    ## TODO 11: Make account at position B become the next account at position A

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)







## TODO 4: Ask  the user for input

## TODO 5: Check if user is correct

## TODO 6: Get follower count for each account.



## TODO 8: Give user feedback on their guess

## TODO 9: Score keeping





## TODO 12: Clear screen between rounds