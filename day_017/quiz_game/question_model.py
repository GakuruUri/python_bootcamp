"""
Create a new class Question, with an __init_-() method with 2 attributes:
text and answer attributes
"""


class Question:  # Create a new model for a question in our quiz
    """Holds  a text attribute and answer attribute to the question text"""

    def __init__(self, q_text, q_answer):  # Set up 2 attributes below indented
        self.text = q_text
        self.answer = q_answer
