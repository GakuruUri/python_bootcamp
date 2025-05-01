# Enter your height in meters a.g 1.55
height = float(input("What is your height in meters? "))

# Enter your weight in kilograms e.g 72
weight =  int(input("Enter your weight in kilograms: "))

bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")  
else:
    print(f"Your BMI is {bmi}, you are clinically obese.") 


# bmi = weight / (height ** 2)

# print(f"Your bmi is {bmi}.\n")

# if bmi < 18.28:
#     print("You are underweight.")
# elif bmi <= 22.0:
#     print("Your weight is normal.")
# elif bmi <= 28.51:
#     print("You are slightly overweight.")
# elif bmi <= 32.56:
#     print("You are obese.")
# else:
#     print("You are clinically obese.")



