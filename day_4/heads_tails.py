import random


# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads.")
# else:
#     print("Tails.")


coin_toss = random.randint(1, 2)

if coin_toss == 1:
    print("heads.".title())
else:
    print("tails.".title())