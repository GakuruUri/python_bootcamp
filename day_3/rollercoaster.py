# import sys
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cms? "))

bill = 0

if height >= 120:
    print("You can ride the roller coaster.")
    
    age = int(input("What is your age? "))
    # if age >= 45:
    #     print("Your ride is free.")
    #     sys.exit()
    if age < 12:
        bill = 5
        print("The child ticket is $5.")
    elif age <= 18:
        bill = 7
        print("The youth ticket is $7.")
    elif  age >= 45 and age <= 55:
        print("Everything will be alright. Have a free ride on us.")
    else:
        bill = 12
        print("Adult ticket is $12.")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add 3 dollars to their bill
        # bill = bill + 3
        bill += 3
        
    print(f"Your final bill is {bill}.")
else:
    print("Sorry, you have to grow taller before you can ride the rollercoaster.")





# print("Welcome to the rollercoaster")
# height = int(input("What is your height?"))

# if height >= 120:
#     print("You can ride the rollercoster")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("You will pay $5")
#     elif age <= 18:
#         print("You will pay $7")
#     else:
#         print("You will pay $12")
# else:
#     print("You will cannot ride the rollercoaster")
