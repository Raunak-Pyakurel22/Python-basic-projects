import random
import shutil


def rps():
    list = ["R", "P", "S"]
    os_choice = random.choice(list)
    if os_choice == "R":
        if user_choice == "R":
            print()
            print("User chose: Rock")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("Tie!")
        if user_choice == "P":
            print()
            print("User chose: Paper")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("You Win!")
        if user_choice == "S":
            print()
            print("User chose: Scissors")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("Rock beat Scissors, I Win!")
    if os_choice == "P":
        if user_choice == "R":
            print()
            print("User chose: Rock")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("Paper beat Rock, I Win!")
        if user_choice == "P":
            print()
            print("User chose: Paper")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("Tie!")
        if user_choice == "S":
            print()
            print("User chose: Scissors")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("You Win!")
    if os_choice == "S":
        if user_choice == "R":
            print()
            print("User chose: Rock")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("You Win!")
        if user_choice == "P":
            print()
            print("User chose: Paper")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("Scissors beat Paper, I Win!")
        if user_choice == "S":
            print()
            print("User chose: Scissors")
            if os_choice == "R":
                print("Computer chose: Rock")
            elif os_choice == "P":
                print("Computer chose: Paper")
            else:
                print("Computer chose: Scissors")
            print("Tie!")


while True:
    a = "#######################################"
    b = "###                                 ###"
    c = "###  Rock, Paper and Scissors Game  ###"
    print(a.center(shutil.get_terminal_size().columns))
    print(c.center(shutil.get_terminal_size().columns))
    print(a.center(shutil.get_terminal_size().columns))
    print("Choose from the following: ")
    print("R. Rock")
    print("P. Paper")
    print("S. Scissors")
    print("Q. Quit")
    print()
    user_choice = input("Enter your choice: ")
    user_choice = user_choice.upper()
    if user_choice == "R" or user_choice == "P" or user_choice == "S":
        rps()
        print()
    elif user_choice == "Q":
        print()
        credit1 = "Thank You for playing Rock, Paper and Scissors game."
        credit2 = "- Made by Raunak Pyakurel"
        print(credit1.center(shutil.get_terminal_size().columns))
        print(credit2.center(shutil.get_terminal_size().columns))
        print()
        quit()
    else:
        print()
        print("Error! Please enter the valid character!")
        print()
