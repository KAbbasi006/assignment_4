# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.




# def temp():
#     while True: 
#          try:
#              farenheit= float(input("Enter temperature in Fahrenheit: ")) 
#              celsius = (farenheit-32)* 5.0/9.0
#              print(f"The temperature in Celsius is: {celsius:.2f}")
#              break
         
#          except ValueError:
#              print("Invalid Input! Please enter a valid number.")
   
# if __name__ == "__main__":
#     temp()



def temp():
    while True:
        try:
            farenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (farenheit -32) * 5/9
            print(f"The temperature in celsius is : {celsius:.2f}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    temp()