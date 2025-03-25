# Q. Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math # importing math to use sqrt function
def main():
    ab:float = float(input("\nEnter the length of AB : "))
    bc: float = float(input("Enter the length of BC : "))

    ac : float = math.sqrt(ab**2 + bc**2)
    print(f"The length of the AC (hypotenuse) is: {ac:.2f}\n")


if __name__ == "__main__":
    main()