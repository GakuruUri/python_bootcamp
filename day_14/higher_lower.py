import random
from art import logo, vs
from game_data import data
import os

def format_data(account):
    """Format the account data into a printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"



## Use if statements to check if user is correct
def check_answer(guess, a_follower, b_follower):
    """Takes the user guess and follower count and returns if they got it right."""
    # if a_follower > b_follower and guess == "a":
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:
    

    # Generate a random account from game data
    
    # Make account at position B bacome the next account at position A
    account_a = account_b
    account_b = random.choice(data)


    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")


    # # Format the account data into a printable format.
    # account_name = account_a["name"]
    # account_descr = account_a["description"]
    # account_country = account_a["country"]
    # print(f"{account_name}, a {account_descr}, from {account_country}")


    # Ask  the user for input

    guess = input("Who has more followers? Type 'A' or 'B' ").lower()

    # Check if user is correct
    ## Get follower count for each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]


    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Clear screen between rounds
    os.system('clear')
    print(logo)
    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score is: {score}.")
        
    else:
        game_should_continue = False
        print(f"sorry, thats wrong. Final score: {score}.")