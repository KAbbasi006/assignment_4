# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light



#Speed of light in m/s
C : int = 299792458

def main():
    while True:
        try:
            mass = input("Enter mass in Killos or type 'exit' to quit: ")
            if mass.lower() == "exit":
                print("---------- Exiting ----------")
                break
            mass = float(mass)

            energy = mass * (C**2) # calculate energy
            
            print("e = m*C^2")
            print(f"m = {mass} Kg")
            print(f"C = {C} m/s")
            print(f"Energy in joules is {energy:.2f}!\n")

        except ValueError:
            print("Invalid input. Please enter a valid numeric value to find Energy or type 'exit' to quit.\n")

if __name__ == "__main__":
    main()


