import pyqrcode
from barcode import EAN13
from barcode.writer import ImageWriter

again = True
while again == True:
    print()
    print("This program generates QR codes and Bar codes in PNG format. ")
    print("1. QR code ")
    print("2. Bar code ")
    print("3. Quit ")
    print()
    choice = input("Choose which one to generate: ")
    print(
        "________________________________________________________________________________________________________________"
    )
    print()
    if choice == "1":
        data_to_encode = input("Enter the data you want to get encoded into QR code: ")
        qr_code = pyqrcode.create(data_to_encode)
        first_image_name = input("Enter image name: ")
        last_image_name = ".png"
        image_name = first_image_name + last_image_name
        qr_code.svg(image_name, scale=8)
        print()
        while again == True:
            asking_user = input(
                "Do you want to continue generating another image?(Enter Y for 'Yes', N for 'No': "
            )
            if asking_user == "Y" or asking_user == "y":
                again = True
                print(
                    "________________________________________________________________________________________________________________"
                )
                break
            elif asking_user == "N" or asking_user == "n":
                again = False
                print()
                print("Thank You for using this program. ")
                print("- Made by VikinG")
                print(
                    "________________________________________________________________________________________________________________"
                )
                quit()
            else:
                print("Invalid Character, enter again. ")
                print(
                    "________________________________________________________________________________________________________________"
                )
                print()
    elif choice == "2":
        while again == True:
            print()
            number = input(
                "Enter 12 digits number you want to get encoded into Bar code: "
            )
            number_length = len(number)
            if number_length == 12:
                bar_code = EAN13(number, writer=ImageWriter())
                image_name = input("Enter image name: ")
                bar_code.save(image_name)
                print()
                while again == True:
                    asking_user = input(
                        "Do you want to continue generating another image?(Enter Y for 'Yes', N for 'No': "
                    )
                    if asking_user == "Y" or asking_user == "y":
                        again = True
                        print(
                            "________________________________________________________________________________________________________________"
                        )
                        break
                    elif asking_user == "N" or asking_user == "n":
                        again = False
                        print()
                        print("Thank You for using this program. ")
                        print("- Made by VikinG ")
                        print(
                            "________________________________________________________________________________________________________________"
                        )
                        quit()
                    else:
                        print("Invalid Character, enter again. ")
                        print(
                            "________________________________________________________________________________________________________________"
                        )
                        print()
            else:
                print("The input must have 12 digits. ")
                print(
                    "________________________________________________________________________________________________________________"
                )
                print()
            break

    elif choice == "3":
        print("Thank You for using this program. ")
        print("- Made by VikinG ")
        print()
        print(
            "________________________________________________________________________________________________________________"
        )
        quit()
    else:
        print("Invalid input, please input again. ")
        print(
            "________________________________________________________________________________________________________________"
        )
