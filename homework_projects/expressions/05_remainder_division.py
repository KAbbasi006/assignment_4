# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.



def main():
    dividend : int = int(input("\nEnter integer to be divided: "))
    divisor : int = int(input("Enter integer to divide by: "))

    quotient : int = dividend // divisor # floor division
    remainder : int = dividend % divisor # modulus
    print("The result of the division is " + str(quotient) + ", with a remainder of "+ str(remainder)+".\n")

if __name__ == "__main__":
    main()