# Q. Converts feet to inches.

inches_in_foot : int = 12 # fixed value

def main():
    while True:
        try:
            feet:float = input("Enter number of feet or type 'exit' to quit: ")
            if feet.lower() == "exit":
                print("--------------- Exiting the program ---------------\n")
                break
            feet = float(feet)
            inches: float = feet* inches_in_foot
            print(f"{feet} in inches is: {inches} inches!\n ")
        
        except ValueError:
            print("Invalid input! Please enter a valid numeric value or type 'exit' to quit.\n ")


if __name__ == "__main__":
    main()
            

            


        

