import random
import shutil

# just the end of game not much imp here
def credits():
    credit1 = "Thank You for playing Number game."
    credit2 = "- Made by VikinG"
    print(credit1.center(shutil.get_terminal_size().columns))
    print(credit2.center(shutil.get_terminal_size().columns))
    print()
    quit()


# just the intro of game not much imp here
def instructions():
    print()
    welcome_message1 = "- Welcome to Number game -"
    print(welcome_message1.center(shutil.get_terminal_size().columns))
    print()
    print("Before you start, Remember:")
    print(
        "1. One must first provide the computer with the lower and upper bounds of numbers."
    )
    print("2. As the game advances, hints will be provided.")
    print(
        "3. The number of tries will be determined by the digits between the lower and upper ranges of the number."
    )
    print("   Upto 10 digits - 3tries max")
    print("   Upto 20 digits - 6tries max")
    print("   Upto 30 digits - 9tries max")
    print("   Upto 40 digits - 12tries max")
    print("   More than 40 digits - 15tries max")
    print("   Thank You, Enjoy the Game!")
    print()


# the main logic of game
def main_game():
    print()
    random_number = random.randint(lower_limit, upper_limit)
    if random_number > 0:
        print("Hint : It is a positive number.")
    else:
        print("Hint : It is a negative number.")
    print(
        "________________________________________________________________________________________________________________"
    )
    print()
    loop = 3
    print("You will have 3 chances to get hint here.")
    while loop > 0:
        loop = loop - 1
        second_hint = int(
            input(
                "Enter a number to know if the number to be guessed is divisible by it: "
            )
        )
        if random_number % second_hint == 0:
            print("Hint: It is completely divisible by", second_hint)
            break
        else:
            print("Hint: It is not completely divisible by", second_hint)
            print()
    print(
        "________________________________________________________________________________________________________________"
    )
    number_digits = upper_limit - lower_limit
    if number_digits < 10 & number_digits > 0:
        attemp = 3
    elif number_digits < 20 & number_digits >= 10:
        attemp = 4
    elif number_digits < 30 & number_digits >= 20:
        attemp = 6
    elif number_digits < 40 & number_digits >= 30:
        attemp = 8
    else:
        attemp = 10
    print("You will have", attemp, "tries")
    while attemp > 0:
        attemp = attemp - 1
        print()
        guess = int(input("Enter your guess: "))
        if guess > random_number:
            print("Hint: The number is smaller than your guess.")
        elif guess < random_number:
            print("Hint: The number is larger than your guess.")
        else:
            print("Congratulations, you guessed the number.")
            print()
            print(
                "________________________________________________________________________________________________________________"
            )
            print()
            credits()


# just felt like making a func here,lol
def compare_lower_upper():
    if lower_limit >= upper_limit:
        print("Lower limit cannot be larger than or equal to upper limit.")
        print()
        print("Please enter the values again.")
        print(
            "________________________________________________________________________________________________________________"
        )
        print()
        return "False"
    else:
        main_game()


# main program starts here
instructions()
user_name = input("Please do enter your name: ")
start_game = input("Press any key to start the game: ")
while True:
    lower_limit = input("Enter lower limit of Number: ")
    upper_limit = input("Enter upper limit of Number: ")
    print()
    try:
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)
        compare_lower_upper()
        print()
        quit()
    except ValueError:
        print("Upper and Lower limits can only accept numbers.")
        print(
            "________________________________________________________________________________________________________________"
        )
        print()
