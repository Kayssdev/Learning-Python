"""
today was just a simple coding practical exercise
trying to improve on while, break and continue.
"""
while True:
    count = int(input("Enter a number: "))
    if count == 0:
        print("Exiting")
        break

    if count < 0:
        print("Negative number entered, try again.")
        continue

# My first code 

count = 5
while count > 0:
    user_input = input("Enter a number: ")
    if user_input == "exit":
        print("Exiting the program.")
        break
    if int(user_input) % 2 == 0:
        print(f"{user_input} is even.")
    else:        print(f"{user_input} is odd.")
    count -= 1
    if user_input == "0":
        break