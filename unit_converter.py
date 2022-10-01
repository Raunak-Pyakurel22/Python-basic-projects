import shutil
from time import sleep


def choices():
    print()
    print("# Choose the Conversion type: ")
    print("1.  Temperature")
    print("2.  Area")
    print("3.  Length")
    print("4.  Time")
    print("5.  Mass")
    print("6.  Volume")
    print("7.  Data")
    print("8.  Quit")
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
    print("Number of Days:", D)


def days_to_hours():
    D = input("Enter number of Days: ")
    D = float(D)
    H = D * 24
    print("Time in Minutes:", H)


def days_to_weeks():
    D = input("Enter number of Days: ")
    D = float(D)
    W = D / 7
    print("Number of Weeks:", W)


def weeks_to_days():
    W = input("Enter number of Weeks: ")
    W = float(W)
    D = W * 7
    print("Number of Days:", D)


def weeks_to_years():
    W = input("Enter number of Weeks: ")
    W = float(W)
    Y = W / 52
    print("Number of Years:", Y)


def years_to_weeks():
    Y = input("Enter number of Weeks: ")
    Y = float(Y)
    W = Y * 52
    print("Number of Years:", W)


def kilogram_to_pound():
    KG = input("Enter mass in Kilogram: ")
    KG = float(KG)
    P = KG * 2.20462262185
    print("Mass in Pounds:", P)


def pound_to_kilogram():
    P = input("Enter mass in Pound ")
    P = float(P)
    KG = P / 2.20462262185
    print("Mass in Kilogram:", KG)


def kilogram_to_gram():
    KG = input("Enter mass in Kilogram: ")
    KG = float(KG)
    G = KG * 1000
    print("Mass in Gram:", G)


def gram_to_kilogram():
    G = input("Enter mass in Gram: ")
    G = float(G)
    KG = G / 1000
    print("Mass in Kilogram:", KG)


def kilogram_to_ton():
    KG = input("Enter mass in Kilogram: ")
    KG = float(KG)
    T = KG / 1000
    print("Mass in Ton:", T)


def ton_to_kilogram():
    T = input("Enter mass in Ton: ")
    T = float(T)
    KG = T * 1000
    print("Mass in Kilogram:", KG)


def litre_to_cmetre():
    L = input("Enter volume in litre: ")
    L = float(L)
    CM = L / 1000
    print("Volume in Cubic Metre:", CM)


def cmetre_to_litre():
    CM = input("Enter volume in Cubic Metre: ")
    CM = float(CM)
    L = CM * 1000
    print("Volume in Litre:", L)


def litre_to_UKgal():
    L = input("Enter volume in Litre: ")
    L = float(L)
    UKG = L * 0.2199692483
    print("Volume in UK gallon:", UKG)


def UKgal_to_litre():
    UKG = input("Enter Volume in UK gallon: ")
    UKG = float(UKG)
    L = UKG / 0.2199692483
    print("Volume in Litre:", L)


def litre_to_USgal():
    L = input("Enter volume in Litre: ")
    L = float(L)
    USG = L * 0.2641720524
    print("Volume in US Gallon:", USG)


def USgal_to_litre():
    USG = input("Enter volume in US Gallon: ")
    USG = float(USG)
    L = USG / 0.2641720524
    print("Volume in Litre:", L)


def bit_to_byte():
    BIT = input("Enter data size in Bit: ")
    BIT = float(BIT)
    BYTE = BIT / 8
    print("Data size in Byte:", BYTE)


def byte_to_bit():
    BYTE = input("Enter data size in Byte: ")
    BYTE = float(BYTE)
    BIT = BYTE * 8
    print("Data size in Bit:", BIT)


def byte_to_kbyte():
    BYTE = input("Enter data size in Byte: ")
    BYTE = float(BYTE)
    KBYTE = BYTE / 1024
    print("Data size in Kilobyte:", KBYTE)


def kbyte_to_byte():
    KBYTE = input("Enter data size in Kilobyte: ")
    KBYTE = float(KBYTE)
    BYTE = KBYTE * 1024
    print("Data size in Byte:", BYTE)


def kbyte_to_mbyte():
    KBYTE = input("Enter data size in Kilobyte: ")
    KBYTE = float(KBYTE)
    MBYTE = KBYTE / 1024
    print("Data size in Megabyte:", MBYTE)


def mbyte_to_kbyte():
    MBYTE = input("Enter data size in Megabyte: ")
    MBYTE = float(MBYTE)
    KBYTE = MBYTE * 1024
    print("Data size in Kilobyte:", KBYTE)


def mbyte_to_gbyte():
    MBYTE = input("Enter data size in Megabyte: ")
    MBYTE = float(MBYTE)
    GBYTE = MBYTE / 1024
    print("Data size in Gigabyte:", GBYTE)


def gbyte_to_mbyte():
    GBYTE = input("Enter data size in Gigabyte: ")
    GBYTE = float(GBYTE)
    MBYTE = GBYTE * 1024
    print("Data size in Megabyte:", MBYTE)


def gbyte_to_tbyte():
    GBYTE = input("Enter data size in Gigabyte: ")
    GBYTE = float(GBYTE)
    TBYTE = GBYTE / 1024
    print("Data size in Terabyte:", TBYTE)


def tbyte_to_gbyte():
    TBYTE = input("Enter data size in Terabyte: ")
    TBYTE = float(TBYTE)
    GBYTE = TBYTE * 1024
    print("Data size in Gigabyte:", GBYTE)


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
        elif choice2 == "3":
            print()
            celsius_to_kelvin()
        elif choice2 == "4":
            print()
            kelvin_to_celsius()
        elif choice2 == "5":
            print()
            kelvin_to_fahrenheit()
        elif choice2 == "6":
            print()
            fahrenheit_to_kelvin()
        elif choice2 == "7":
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
        print("1.  Seconds to Minutes")
        print("2.  Minutes to Seconds")
        print("3.  Minutes to Hours")
        print("4.  Hours to Minutes")
        print("5.  Days to Hours")
        print("6.  Hours to Days")
        print("7.  Days to Weeks")
        print("8.  Weeks to Days")
        print("9.  Years to Weeks")
        print("10. Weeks to Years")
        print("11. Back")
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
            days_to_weeks()
        if choice2 == "8":
            print()
            weeks_to_days()
        if choice2 == "9":
            print()
            years_to_weeks()
        if choice2 == "10":
            print()
            weeks_to_years()
        if choice2 == "11":
            print()
            break


def mass():
    while True:
        print()
        print("Choose from the following: ")
        print("1. Kilogram to Pound")
        print("2. Pound to Kilogram")
        print("3. Kilogram to Gram")
        print("4. Gram to Kilogram")
        print("5. Kilogram to Ton")
        print("6. Ton to Kilogram")
        print("7. Back")
        print()
        choice2 = input("Enter the choice: ")
        sleep(0.25)
        if choice2 == "1":
            print()
            kilogram_to_pound()
        if choice2 == "2":
            print()
            pound_to_kilogram()
        if choice2 == "3":
            print()
            kilogram_to_gram()
        if choice2 == "4":
            print()
            gram_to_kilogram()
        if choice2 == "5":
            print()
            kilogram_to_ton()
        if choice2 == "6":
            print()
            ton_to_kilogram()
        if choice2 == "7":
            print()
            break


def volume():
    while True:
        print()
        print("Choose from the following: ")
        print("1. Litre to Cubic Metre")
        print("2. Cubic Metre to Litre")
        print("3. Litre to UK Gallon")
        print("4. UK Gallon to Litre")
        print("5. Litre to US Gallon")
        print("6. US Gallon to Litre")
        print("7. Back")
        print()
        choice2 = input("Enter the choice: ")
        sleep(0.25)
        if choice2 == "1":
            print()
            litre_to_cmetre()
        if choice2 == "2":
            print()
            cmetre_to_litre()
        if choice2 == "3":
            print()
            litre_to_UKgal()
        if choice2 == "4":
            print()
            UKgal_to_litre()
        if choice2 == "5":
            print()
            litre_to_USgal()
        if choice2 == "6":
            print()
            USgal_to_litre()
        if choice2 == "7":
            print()
            break


def data():
    while True:
        print()
        print("Choose from the following: ")
        print("1. Bit to Byte")
        print("2. Byte to Bit")
        print("3. Byte to Kilobyte")
        print("4. Kilobyte to Byte")
        print("5. Kilobyte to Megabyte")
        print("6. Megabyte to Kilobyte")
        print("7. Megabyte to Gigabyte")
        print("8. Gigabyte to Megabyte")
        print("9. Gigabyte to Terabyte")
        print("10. Terabyte to Gigabyte")
        print("11. Back")
        print()
        choice2 = input("Enter the choice: ")
        sleep(0.25)
        if choice2 == "1":
            print()
            bit_to_byte()
        if choice2 == "2":
            print()
            byte_to_bit()
        if choice2 == "3":
            print()
            byte_to_kbyte()
        if choice2 == "4":
            print()
            kbyte_to_byte()
        if choice2 == "5":
            print()
            kbyte_to_mbyte()
        if choice2 == "6":
            print()
            mbyte_to_kbyte()
        if choice2 == "7":
            print()
            mbyte_to_gbyte()
        if choice2 == "8":
            print()
            gbyte_to_mbyte()
        if choice2 == "9":
            print()
            gbyte_to_tbyte()
        if choice2 == "10":
            print()
            tbyte_to_gbyte()
        if choice2 == "11":
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
print()
print("Hello, This is Unit Converter.")
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
            mass()
        if choice1 == "6":
            print()
            volume()
        if choice1 == "7":
            print()
            data()
        if choice1 == "8":
            print()
            close()
