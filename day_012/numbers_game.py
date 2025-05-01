from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



# Function to check the user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Checks answer against guess and Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")
        
        
# Make a function to set the difficulty.
def set_difficulty():
    level = input("Choose a difficulty, Type 'easy' of 'hard': ")
    if level == 'easy':
       return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        
def game():
    print(logo)
    # Choosing a random number between 1 and 100.

    print("Welcome to the Number Guessing game!")
    print("I'm thinking of number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psssst, the correct answer is {answer}")


    turns = set_difficulty()
    
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer: 
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number.
        guess = int(input("Make a guess."))
        
        # Track the number oof turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've ran out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()



