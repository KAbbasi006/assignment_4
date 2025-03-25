# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.



import random

num_of_sides = 6 # constant value for the number of sides on a dice(6 sides on a dice)


def roll_dice():
    dice1 :int = random.randint(1, num_of_sides) # local variable only visible inside function
    dice2 :int = random.randint(1, num_of_sides) # local variable only visible inside function
    total :int = dice1 + dice2
    print("Total of two dice: ", total)


def main():
    dice1 : int = 10
    # The name dice1 is reused inside roll_dice(), but it’s local to roll_dice() and completely separate.
    print("---------- dice1 in main() starts as : " + str(dice1)+" ----------")

    roll_dice()
    roll_dice()
    roll_dice()

    print("---------- dice1 in main() is: " + str(dice1)+" ----------")


if __name__ == "__main__":
    main()


