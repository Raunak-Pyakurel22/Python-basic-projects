import shutil
from time import sleep


def choices():
    print()
    print("Choose  the Conversion type: ")
    print("1. Temperature")
    print("2. Area")
    print("3. Length")
    print("4. Time")
    print("5. Quit")
    print()


def ctof():
    C = input("Enter temperature in Celsius: ")
    C = float(C)
    F = C * (9 / 5) + 32
    print("Temperature in Fahrenheit:", F)


def ftoc():
    F = input("Enter the temperature in Fahrenheit: ")
    F = float(F)
    C = (F - 32) * (5 / 9)
    print("Temperature in Celsius:", C)


def ctok():
    C = input("Enter temperature in Celsius: ")
    C = float(C)
    K = C + 273.15
    print("Temperature in Kelvin:", C)


def ktoc():
    K = input("Enter temperature in Kelvin: ")
    K = float(K)
    C = K - 273.15
    print("Temperature in Celsius:", C)


def ktof():
    K = input("Enter temperature in Kelvin: ")
    K = float(K)
    F = (K - 273.15) * (9 / 5) + 32
    print("Temperature in Fahrenheit:", F)


def ftok():
    F = input("Enter the temperature in Fahrenheit: ")
    F = float(F)
    K = (F - 32) * (5 / 9) + 273.15
    print("Temperature in Kelvin:", K)


def mtokm():
    M = input("Enter the length in metres: ")
    M = float(M)
    KM = M / 1000
    print("Length in Kilometres:", KM)


def kmtom():
    KM = input("Enter the area in Kilometres: ")
    KM = float(KM)
    M = KM * 1000
    print("Length in Metres:", M)


def kmtomi():
    KM = input("Enter the length in Kilometres: ")
    KM = float(KM)
    MI = KM * 0.62137119
    print("Length in Miles:", MI)


def mitokm():
    MI = input("Enter the length in Miles: ")
    MI = float(MI)
    KM = MI / 0.62137119
    print("Length in Kilometres:", KM)


def kmtof():
    KM = input("Enter the length in Kilometres: ")
    KM = float(KM)
    F = KM * 3280.84
    print("Length in Foot:", F)


def ftokm():
    F = input("Enter the length in Foot: ")
    F = float(KM)
    KM = F / 3280.84
    print("Length in Kilometres:", KM)


def mtosqkm():
    M = input("Enter area in Square Metres: ")
    M = float(M)
    KM = M / 1000000
    print("Area in Square Kilometres:", KM)


def sqkmtom():
    KM = input("Enter area in Square Kilometres: ")
    KM = float(KM)
    M = KM * 1000000
    print("Area in Square Metres:", M)


def sqkmtomi():
    KM = input("Enter area in Square Kilometres: ")
    KM = float(KM)
    MI = KM / 2.59
    print("Area in Square Miles:", MI)


def mitosqkm():
    MI = input("Enter area in Square Miles: ")
    MI = float(MI)
    KM = MI * 2.59
    print("Area in Square Kilometres:", KM)


def ftosqkm():
    F = input("Enter area in Square Foot: ")
    F = float(F)
    KM = F / 10763910.41671
    print("Area in Square Kilometres:", KM)


def sqkmtof():
    KM = input("Enter area in Square Kilometres: ")
    KM = float(KM)
    F = KM * 10763910.41671
    print("Area in Square Foot:", F)


def stom():
    S = input("Enter time in Seconds: ")
    S = float(S)
    M = S / 60
    print("Time in Minutes:", M)


def mtos():
    M = input("Enter time in Minutes: ")
    M = float(M)
    S = M * 60
    print("Time in Seconds:", S)


def htom():
    H = input("Enter time in Hours: ")
    H = float(H)
    M = H * 60
    print("Time in Minutes:", M)


def mtoh():
    M = input("Enter time in Minutes: ")
    M = float(M)
    H = M / 60
    print("Time in Hours:", H)


def htod():
    H = input("Enter time in Hours: ")
    H = float(H)
    D = H / 24
    print("Time in Days:", D)


def dtoh():
    D = input("Enter time in Days: ")
    D = float(D)
    H = D * 24
    print("Time in Minutes:", H)


def temperature():
    while True:
        print()
        print("Choose from the following: ")
        print("1. °C to °F")
        print("2. °F to °C")
        print("3. °C to  K")
        print("4.  K to °C")
        print("5.  K to °F")
        print("6. °F to  K")
        print("7. Back")
        print()
        choice2 = input("Enter the choice: ")
        sleep(0.25)
        if choice2 == "1":
            print()
            ctof()
        if choice2 == "2":
            print()
            ftoc()
        if choice2 == "3":
            print()
            ctok()
        if choice2 == "4":
            print()
            ktoc()
        if choice2 == "5":
            print()
            ktof()
        if choice2 == "6":
            print()
            ftok()
        if choice2 == "7":
            print()
            break


def length():
    while True:
        print()
        print("Choose from the following: ")
        print("1. m to km")
        print("2. km to m")
        print("3. km to miles")
        print("4. miles to km")
        print("5. foot to km")
        print("6. km to  foot")
        print("7. Back")
        print()
        choice2 = input("Enter the choice: ")
        sleep(0.25)
        if choice2 == "1":
            print()
            mtokm()
        if choice2 == "2":
            print()
            kmtom()
        if choice2 == "3":
            print()
            kmtomi()
        if choice2 == "4":
            print()
            mitokm()
        if choice2 == "5":
            print()
            ftokm()
        if choice2 == "6":
            print()
            kmtof()
        if choice2 == "7":
            print()
            break


def area():
    while True:
        print()
        print("Choose from the following: ")
        print("1. sq.m to sq.km")
        print("2. sq.km to sq.m")
        print("3. sq.m to sq.miles")
        print("4. sq.miles to sq.km")
        print("5. sq.foot to sq.km")
        print("6. sq.km to sq.foot")
        print("7. Back")
        print()
        choice2 = input("Enter the choice: ")
        sleep(0.25)
        if choice2 == "1":
            print()
            mtosqkm()
        if choice2 == "2":
            print()
            sqkmtom()
        if choice2 == "3":
            print()
            sqkmtomi()
        if choice2 == "4":
            print()
            mitosqkm()
        if choice2 == "5":
            print()
            ftosqkm()
        if choice2 == "6":
            print()
            sqkmtof()
        if choice2 == "7":
            print()
            break


def time():
    while True:
        print()
        print("Choose from the following: ")
        print("1. Seconds to Minutes")
        print("2. Minutes to Seconds")
        print("3. Minutes to Hours")
        print("4. Hours to Minutes")
        print("5. Days to Hours")
        print("6. Hours to Days")
        print("7. Back")
        print()
        choice2 = input("Enter the choice: ")
        sleep(0.25)
        if choice2 == "1":
            print()
            stom()
        if choice2 == "2":
            print()
            mtos()
        if choice2 == "3":
            print()
            mtoh()
        if choice2 == "4":
            print()
            htom()
        if choice2 == "5":
            print()
            dtoh()
        if choice2 == "6":
            print()
            htod()
        if choice2 == "7":
            print()
            break


def close():
    quit()


print()
a = "#######################################"
b = "###                                 ###"
c = "###          Unit Converter         ###"
print(a.center(shutil.get_terminal_size().columns))
print(c.center(shutil.get_terminal_size().columns))
print(a.center(shutil.get_terminal_size().columns))
print("Hello, this is Unit Converter,")
continue_program = input("Press enter to continue: ")
print()
sleep(0.25)
if continue_program == "":
    while True:
        choices()
        choice1 = input("Enter your choice: ")
        print()
        sleep(0.25)
        if choice1 == "1":
            temperature()
        if choice1 == "2":
            area()
        if choice1 == "3":
            length()
        if choice1 == "4":
            time()
        if choice1 == "5":
            print()
            credit1 = "Thank You for using Unit Converter."
            credit2 = "- Made by Raunak Pyakurel"
            print(credit1.center(shutil.get_terminal_size().columns))
            print(credit2.center(shutil.get_terminal_size().columns))
            print()
            close()
