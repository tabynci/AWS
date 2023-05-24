# x=1
# y=2
# z= 1+2
# print(z)


# # Example 2: Adding two numbers with user input.

# In the below program to add two numbers in Python, the user is first asked to enter two numbers, and the input is scanned using the Python input() function and stored in the variables number1 and number2. Then, the variable’s number1 and number2 are added using the arithmetic operator +, and the result is stored in the variable sum.

# def add(x, y):
#     x= input("Enter you number")
#     y=input("ENter your secod number")

#     Z= int(x)+int(y)
#     print(f"The sum of two number are", Z)

# add(2, 3)


num1=15
num2=12

import operator
su = operator.add(num1, num2)

print("Sum of {0} and {1} is {2}".format(num1, num2, su))


# Python program to find the
# maximum of two numbers


# def maximum(a, b):
#     if a>=b:
#         print("a is maximum number")
#     else:
#         print(" b is maximum number")

# maximum(2, 3)

# print(maximum)


# Python program to find the
# maximum of two numbers


def max(a,b):
    if a>=b:
        return a
    else:
        return b
    
    # # dreiver code
    # a=2
    # b=4
    # print(maximum(a,b))

# a=2 
# b=4
# maximums=max(2, 3)

# print(maximums)



# another method

# a=2
# b=3
# c=4
# x=[a, b, c]

# x.sort()
# print(x[-1])


# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"

# var="Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# print(var)

# Write a Python program to find out what version of Python you are using.
# import sys

# print("Python version")
# print(sys.version)


#  Write a Python program to display the current date and time.
# import datetime

# now = datetime.datetime.now()
# print ("Current date and time : ")
# print(now)
#Write a Python program that calculates the area of a circle based on the radius entered by the user.

# import math

# def Area_of_Circle(radius):
#     area= math.pi*radius ** 2
#     return area
# radius=float(input("enter radius please"))

# Circle_area= Area_of_Circle(radius)
# print(Circle_area)


# 5. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.


# first_name=input("Please enter your first name")
# last_name=input("Please enter second name")
# full_name=last_name +" " +first_name

# print(f"Fullname: {full_name}")


# 6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

numbers = int(input("please enter number"))

for num in numbers:
    print(num + "," )