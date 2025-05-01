# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = 6 this reproduces the error.
dice_num = randint(0, 5)
print(dice_imgs[dice_num])