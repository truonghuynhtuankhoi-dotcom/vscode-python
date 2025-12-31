import random

def dice_roll():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    return dice1,dice2

def main():
    again="y"
    while again=="y" or again=="Y":
        input("Press enter to roll dice...")
        dice1, dice2=dice_roll()
        print(f"The result of die 1 is {dice1}")
        print(f"The result of die 2 is {dice2}")
        if dice1>dice2:
            print("Die 1 wins")
        elif dice1<dice2:
            print("Die 2 wins")
        else:
            print("It's a tie")
        again=input("Do you want to roll them again. Enter y/Y to roll again: ")


if __name__=="__main__":
    main()