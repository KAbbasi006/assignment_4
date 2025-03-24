# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def animal():
    fav_animal = input("Enter you Favourite Animal: ")
    print(f"My favourite animal is also {fav_animal}!")

if __name__ == "__main__":
    animal()