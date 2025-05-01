# Which year do you want to check?
year = int(input("Enter year."))

if year % 4 == 0:
    if year % 100 == 0:
        # Not a leap year unless special case
        if year % 400 == 0:
            print("This is a leap year")
        else:
            print("Not a leap year")
    else:
        print("That's a leap year.")
else:
    print("Not a leap year.")





#  # Which year do you want to check?

# year = int(input("Year."))

# if year % 4 == 0:
#     if year % 100 == 0:
#         # Not a leap year, unless special case.
#         if year % 400 == 0:
#             print("Leap Year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

