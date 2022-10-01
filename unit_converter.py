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


def celsius_to_fahrenheit():
    C = input("Enter temperature in Celsius: ")
    C = float(C)
    F = C * (9 / 5) + 32
    print("Temperature in Fahrenheit:", F)


def fahrenheit_to_celsius():
    F = input("Enter the temperature in Fahrenheit: ")
    F = float(F)
    C = (F - 32) * (5 / 9)
    print("Temperature in Celsius:", C)


def celsius_to_kelvin():
    C = input("Enter temperature in Celsius: ")
    C = float(C)
    K = C + 273.15
    print("Temperature in Kelvin:", C)


def kelvin_to_celsius():
    K = input("Enter temperature in Kelvin: ")
    K = float(K)
    C = K - 273.15
    print("Temperature in Celsius:", C)


def kelvin_to_fahrenheit():
    K = input("Enter temperature in Kelvin: ")
    K = float(K)
    F = (K - 273.15) * (9 / 5) + 32
    print("Temperature in Fahrenheit:", F)


def fahrenheit_to_kelvin():
    F = input("Enter the temperature in Fahrenheit: ")
    F = float(F)
    K = (F - 32) * (5 / 9) + 273.15
    print("Temperature in Kelvin:", K)


def metre_to_kilometre():
    M = input("Enter the length in metres: ")
    M = float(M)
    KM = M / 1000
    print("Length in Kilometres:", KM)


def kilometre_to_metre():
    KM = input("Enter the area in Kilometres: ")
    KM = float(KM)
    M = KM * 1000
    print("Length in Metres:", M)


def kilometre_to_mile():
    KM = input("Enter the length in Kilometres: ")
    KM = float(KM)
    MI = KM * 0.62137119
    print("Length in Miles:", MI)


def mile_to_kilometre():
    MI = input("Enter the length in Miles: ")
    MI = float(MI)
    KM = MI / 0.62137119
    print("Length in Kilometres:", KM)


def kilometre_to_foot():
    KM = input("Enter the length in Kilometres: ")
    KM = float(KM)
    F = KM * 3280.84
    print("Length in Foot:", F)


def foot_to_kilometre():
    F = input("Enter the length in Foot: ")
    F = float(KM)
    KM = F / 3280.84
    print("Length in Kilometres:", KM)


def squarem_to_squarekm():
    M = input("Enter area in Square Metres: ")
    M = float(M)
    KM = M / 1000000
    print("Area in Square Kilometres:", KM)


def squarekm_to_squarem():
    KM = input("Enter area in Square Kilometres: ")
    KM = float(KM)
    M = KM * 1000000
    print("Area in Square Metres:", M)


def squarekm_to_squaremiles():
    KM = input("Enter area in Square Kilometres: ")
    KM = float(KM)
    MI = KM / 2.59
    print("Area in Square Miles:", MI)


def squaremiles_to_squarekm():
    MI = input("Enter area in Square Miles: ")
    MI = float(MI)
    KM = MI * 2.59
    print("Area in Square Kilometres:", KM)


def squarefoot_to_squarekm():
    F = input("Enter area in Square Foot: ")
    F = float(F)
    KM = F / 10763910.41671
    print("Area in Square Kilometres:", KM)


def squarekm_to_squarefoot():
    KM = input("Enter area in Square Kilometres: ")
    KM = float(KM)
    F = KM * 10763910.41671
    print("Area in Square Foot:", F)


def seconds_to_minutes():
    S = input("Enter time in Seconds: ")
    S = float(S)
    M = S / 60
    print("Time in Minutes:", M)


def minutes_to_seconds():
    M = input("Enter time in Minutes: ")
    M = float(M)
    S = M * 60
    print("Time in Seconds:", S)


def hours_to_minutes():
    H = input("Enter time in Hours: ")
    H = float(H)
    M = H * 60
    print("Time in Minutes:", M)


def minutes_to_hours():
    M = input("Enter time in Minutes: ")
    M = float(M)
    H = M / 60
    print("Time in Hours:", H)


def hours_to_days():
    H = input("Enter time in Hours: ")
    H = float(H)
    D = H / 24
    print("Time in Days:", D)


def days_to_hours():
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
            celsius_to_fahrenheit()
        if choice2 == "2":
            print()
            fahrenheit_to_celsius()
        if choice2 == "3":
            print()
            celsius_to_kelvin()
        if choice2 == "4":
            print()
            kelvin_to_celsius()
        if choice2 == "5":
            print()
            kelvin_to_fahrenheit()
        if choice2 == "6":
            print()
            fahrenheit_to_kelvin()
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
            metre_to_kilometre()
        if choice2 == "2":
            print()
            kilometre_to_metre()
        if choice2 == "3":
            print()
            kilometre_to_mile()
        if choice2 == "4":
            print()
            mile_to_kilometre()
        if choice2 == "5":
            print()
            foot_to_kilometre()
        if choice2 == "6":
            print()
            kilometre_to_foot()
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
            squarem_to_squarekm()
        if choice2 == "2":
            print()
            squarekm_to_squarem()
        if choice2 == "3":
            print()
            squarekm_to_squaremiles()
        if choice2 == "4":
            print()
            squaremiles_to_squarekm()
        if choice2 == "5":
            print()
            squarefoot_to_squarekm()
        if choice2 == "6":
            print()
            squarekm_to_squarefoot()
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
            seconds_to_minutes()
        if choice2 == "2":
            print()
            minutes_to_seconds()
        if choice2 == "3":
            print()
            minutes_to_hours()
        if choice2 == "4":
            print()
            hours_to_minutes()
        if choice2 == "5":
            print()
            days_to_hours()
        if choice2 == "6":
            print()
            hours_to_days()
        if choice2 == "7":
            print()
            break


def close():
    credit1 = "Thank You for using Unit Converter."
    credit2 = "- Made by VikinG"
    print(credit1.center(shutil.get_terminal_size().columns))
    print(credit2.center(shutil.get_terminal_size().columns))
    print()
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
            close()
