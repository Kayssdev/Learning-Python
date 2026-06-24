# How to use Walrus Operator? :=

print(x := 10)

# Basically assign values to variables as part of an expression. The walrus operator allows you to assign a value to a variable and return that value in the same expression. 

"""
Ternary Operator: Takes three operands: a condition, a value if the condition is true, and a value if the condition is false.
Simple example of using the ternary operator in Python:

"""
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult 

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

fruits = ['apple', 'banana', 'cherry']
if 'banana' in fruits:
    potato = "Banana is present in the list."
print(potato)
