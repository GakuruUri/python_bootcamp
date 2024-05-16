
from random import randint

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

turns = 0

def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        turns -= 0
        
    else:
        print(f"You've got it! The answer was {answer}.")


# Make a function to set the difficulty

def  set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

    #choosing a random number between 1 and 100
def game():
    print("welcome to the numbers Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psssst, the correct answe is {answer}.")


    turns = set_difficulty()

    print(f"You have {turns} attempts remaining to guess the number.")


    # Repeast the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        


        # Let the user choose a number
        guess = int(input("Make a guess: "))


        check_answer(guess, answer)

# Track number of turns and reduce by 1 if they get it wrong





