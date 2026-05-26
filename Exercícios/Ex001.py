def cs():
    import os

    os.system('cls')

cs()

# Basically, I decided to study operators today.

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print(a == b)
print(a is b)

input("Press enter to continue...")
cs()
    # Why are the values returned different? Because `is` compares the exact location of that variable, while `==` compares the content inside that variable

# Short-circuiting
print("ok" and "algo") 
     # Basically "And" operator works   by trying to return the first false value; if it doesn't find one in the first one, it returns the last value! And the "or" does the same but the exact opposite.

print("ok" or "algo") # Returns the first truthy value.

    
# The ternary operator in Python allows you to write a simple if-else statement in a single line. Example:
    
age = 20
status = "Adult" if age >= 18 else "Teenager"

# A simple practice exercise:

n1 = int(input("First number: "))
n2 = int(input("Second number: "))
cs()

greater = n1 if n1 > n2 else n2
print(f"The greatest is {greater}")

total = n1 + n2
res = "Even" if total % 2 == 0 else "Odd"
print(f"The sum {total} is {res}")
if n1 > 0 and n2 > 0:
    print("Both are positive")
else:
    print("at least one is negative")