from day_17.quiz_game.quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain    # From the quiz brain file import the QuizBrain

"""
Write a for loop to iterate over the question_data
Create a Question object for each entry in question_data.
Append each Question object to the question_bank.
"""

question_bank = []  # We create an empty question bank list
for question in question_data:  # We loop through the questions in question data - data.py
    question_text = question["question"]    # for each of these questions, create a local variable
    question_answer = question["correct_answer"]    # for each of these answers, create a variable
    new_question = Question(question_text, question_answer)  # From the Question class in question
    # model positional parameters
    question_bank.append(new_question)  # Append the new created question into the empty list

# print(question_bank)    # Print the now populated question bank list

quiz: QuizBrain = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")