# Printing a string
# print("Hello World\n Hello World\n  Hello World")

# String Concatenation
# print("Hello " + "Uri")
# print("Hello" + " " + "Uri")

#length of a string
#1
# name = input()
# print(len(name))

# #2
# print(len(input()))


#1
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

a, b = b, a


# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


#2

#There are two variables, a and b from input
a = input()
b = input()

# Crete a third variable to help switch  the values
c = a
a = b
b = c

# Printing the switch
print("a: " + a)
print("b: " + b)


# Variables

name = "Jack"
print(name)

name = "Angela"
print(name)