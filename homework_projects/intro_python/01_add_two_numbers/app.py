# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
# Prompt the user to enter the first number.
# Read the input and convert it to an integer.
# Prompt the user to enter the second number.
# Read the input and convert it to an integer.
# Calculate the sum of the two numbers.
# Print the total sum with an appropriate message.

""""
Program : ADD two numbers:
This function asks the users for two numbers and print their sum
"""

def add():
    print("We are going to perform Addition")
    num1 : str = input("Enter first number: ")
    num1 : int = int(num1)
    num2 : str = input("Enter second number: ")
    num2 : int = int(num2)

    total : int = num1 + num2
    print(f"The total is: {total} ")


if __name__ == "__main__":
    add()
else:
    print("""----------\nPerform your own Addition\n----------""")



