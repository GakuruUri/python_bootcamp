print("Welcome to the tip calculatos!")

bill = float(input("What's the total bill amount? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))


tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / num_people
final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)


print(f"Each person should pay: ${final_amount}")