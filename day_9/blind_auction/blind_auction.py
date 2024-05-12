from art import logo
import os

print(logo)


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Uri": 123, "Jack": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")
    

while not bidding_finished:
    name = input("What is your name? \n")
    price = int(input("What your bid price? \n$ "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    # elif should_continue == "yes":
    # clear()
    elif should_continue == "yes":
        # Clearing the Screen
        os.system('clear')
