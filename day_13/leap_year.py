year = int(input("Enter the year to check if it's a leap year or not: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Is a leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Is  a leap year")
else:
    print("Not a leap year.")