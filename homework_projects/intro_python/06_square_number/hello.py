# Ask the user for a number and print its square (the product of the number times itself).

def square():
    try: 
        num:float = float(input("Enter a number to find its square: "))
        print("The square of " + str(num)+" " + "is " +str(num**2))
    except ValueError:
        print("Oops! That doesn't look like a valid number. Please try again.")
    
if __name__ == "__main__":
    square()
else:
    print("""----------------------------------------------
          We are sorry! 
          we could not find the square""")