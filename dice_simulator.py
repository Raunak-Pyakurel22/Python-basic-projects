import random
import shutil


def dice():
    num = ["1", " 2", "3", "4", "5", "6"]
    n = int(random.choice(num))
    if n == 1:
        print("- RESULTS -")
        print("┌─────────┐")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("└─────────┘")
    if n == 2:
        print("- RESULTS -")
        print("┌─────────┐")
        print("|         |")
        print("| O     O |")
        print("|         |")
        print("└─────────┘")

    if n == 3:
        print("- RESULTS -")
        print("┌─────────┐")
        print("| O       |")
        print("|    O    |")
        print("|       O |")
        print("└─────────┘")
    if n == 4:
        print("- RESULTS -")
        print("┌─────────┐")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("└─────────┘")
    if n == 5:
        print("- RESULTS -")
        print("┌─────────┐")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("└─────────┘")
    if n == 6:
        print("- RESULTS -")
        print("┌─────────┐")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("└─────────┘")


while True:
    # printing the program name(simple method)

    # print("#######################################")
    # print("#######################################")
    # print("###                                 ###")
    # print("###  Hello, This is Dice Simulator  ###")
    # print("###                                 ###")
    # print("#######################################")
    # print("#######################################")

    # printing the program name(complex method)
    # used shutil library to center the printing in the console
    # center(shutil.get_terminal_size().columns takes column width and then centers the text

    a = "#######################################"
    b = "###                                 ###"
    c = "###  Hello, This is Dice Simulator  ###"
    # print(a.center(shutil.get_terminal_size().columns))
    print(a.center(shutil.get_terminal_size().columns))
    # print(b.center(shutil.get_terminal_size().columns))
    print(c.center(shutil.get_terminal_size().columns))
    # print(b.center(shutil.get_terminal_size().columns))
    print(a.center(shutil.get_terminal_size().columns))
    # print(a.center(shutil.get_terminal_size().columns))

    print("1. Shuffle the Dice")
    print("2. Exit")
    a = input("Enter your choice: ")
    print()
    if a == "1":
        dice()
        print()
    elif a == "2":
        print()
        print("Thank You for using Dice Simulator.")
        print("- Made by Raunak Pyakurel")
        quit()
    else:
        print("Please enter the valid number")
        print()
