import pyqrcode
import shutil
from barcode import EAN13
from barcode.writer import ImageWriter


def lines():
    terminal_width = shutil.get_terminal_size().columns
    to_print = "_"
    display_terminal = to_print * terminal_width
    print(display_terminal)


def qrcode():
    data_to_encode = input("Enter the data you want to get encoded into QR code: ")
    qr_code = pyqrcode.create(data_to_encode)
    first_image_name = input("Enter image name: ")
    last_image_name = ".png"
    image_name = first_image_name + last_image_name
    qr_code.svg(image_name, scale=8)
    print()
    while True:
        asking_user = input(
            "Do you want to continue generating another image?(Enter Y for 'Yes', N for 'No': "
        )
        if asking_user == "Y" or asking_user == "y":

            lines()
            break
        elif asking_user == "N" or asking_user == "n":

            print()
            print("Thank You for using this program. ")
            print("- Made by VikinG")
            lines()
            quit()
        else:
            print("Invalid Character, enter again. ")
            lines()
            print()


def barcode():
    while True:
        print()
        number = input("Enter 12 digits number you want to get encoded into Bar code: ")
        number_length = len(number)
        if number_length == 12:
            bar_code = EAN13(number, writer=ImageWriter())
            image_name = input("Enter image name: ")
            bar_code.save(image_name)
            print()
            while True:
                asking_user = input(
                    "Do you want to continue generating another image?(Enter Y for 'Yes', N for 'No': "
                )
                if asking_user == "Y" or asking_user == "y":

                    lines()
                    break
                elif asking_user == "N" or asking_user == "n":

                    print()
                    print("Thank You for using this program. ")
                    print("- Made by VikinG ")
                    lines()
                    quit()
                else:
                    print("Invalid Character, enter again. ")
                    lines()
                    print()
            break
        else:
            print("The input must have 12 digits. ")
            lines()
            print()


def exit_program():
    print("Thank You for using this program. ")
    print("- Made by VikinG ")
    print()
    lines()
    quit()


while True:
    print()
    print("This program generates QR codes and Bar codes in PNG format. ")
    print("1. QR code ")
    print("2. Bar code ")
    print("3. Quit ")
    print()
    choice = input("Choose which one to generate: ")
    lines()
    print()
    if choice == "1":
        qrcode()
    elif choice == "2":
        barcode()
    elif choice == "3":
        exit_program()
    else:
        print("Invalid input, please input again. ")
        lines()
