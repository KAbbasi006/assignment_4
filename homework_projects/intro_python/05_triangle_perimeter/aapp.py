# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).


def perimeter():
    side1 :float = float(input("Enter the length of side 1 of a triangle: "))
    side2 :float = float(input("Enter the length of side 2 of a triangle: "))
    side3 :float = float(input("Enter the length of side 3 of a triangle: "))
    triangle_perimeter :int = side1 + side2 + side3
    print(f"The perimeter of a triangle is {triangle_perimeter}")



if __name__ == "__main__":
    perimeter()
else: 
    user_input = input("Enter the length of three sides of a triangle separated by spaces: ")
    input_list = user_input.split()
    number = [int(num) for num in input_list]
    print(sum(number))

    