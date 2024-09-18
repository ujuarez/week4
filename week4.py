# Advanced Problem Set: Delving Deeper with Numbers in Python --- Bell Ringer

#################### PROBLEM 1: Basic Arithmetic & Order of Operations ####################
# Task 1: Using the order of operations (PEMDAS/BODMAS), evaluate the following expression:
# 3 + 6 * (5 + 4) / 3 - 7. Print the result.

#5+4 , 6*9 , 54/3 , 18+3 , 21 - 7
print("3+6*(5+4) / 3 - 7 = " + "14")

# Task 2: Calculate the remainder when 145 is divided by 12 using modulo and print the result.
print("The remainder when 145 is divided by 12 is", 145%12)

# Task 3: Raise 7 to the power of 3 and print the result.
print("7 to the power of 3 is" , 7**3)

#################### PROBLEM 2: Working with Functions ####################
# Task 4: Given a list of numbers:
numbers = [23, 89, 12, 54, 92, 65, 71, 13, 45]
# Use the max() and min() functions to find the highest and lowest number respectively.
print("The Maximum of the numbers is" , max(numbers))

print("The Minimum of the numbers is" , min(numbers))

# Task 5: Round the number 12.5678 to 2 decimal places.
number12 = 12.5678
# rounding the above number
rounded_number = format(number12,".2f")
print("12.5678 rounded up to 2 decimal places is:", rounded_number)

# Task 6: Find the absolute value of -45.
print("The absolute value of -45 is" , abs(-45))

#################### PROBLEM 3: Advanced Math Functions ####################
from math import *

# Task 7: Using the math library, find the floor value of 15.7.
print("The floor value of 15.7 is" , floor(15.7))

# Task 8: Find the ceiling value of 15.2.
print("The ceiling value of 15.2 is" , ceil(15.2))

# Task 9: Calculate the square root of 625.
print("The square root of 625 is" , sqrt(625))

#################### PROBLEM 4: Problem Solving ####################
# Task 10: You are given two lists:
prices = [34.56, 45.78, 23.89, 12.34, 78.90]
quantities = [3, 5, 2, 4, 6]


Sum= sum(prices)
print("The sum of the prices is", round (Sum, 2))
Sum2 = sum(quantities)
print("The sum of the number of objects is", round(Sum2, 2))
# Calculate the total cost for each item (price multiplied by quantity).
# Then, find the average cost of all items after rounding it to 2 decimal places.

#################### END OF ADVANCED PROBLEM SET  -- end Bell Ringer  ####################