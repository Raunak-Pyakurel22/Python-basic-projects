import shutil
from time import sleep


def count(value):
    if value == 1:
        print()
        timer_start_message = "The Countdown starts now"
        print(timer_start_message.center(shutil.get_terminal_size().columns))
        print()
        print()
    else:
        print()
        timer_finished_message = " The Countdown has Ended! "
        print(timer_finished_message.center(shutil.get_terminal_size().columns))
        print()


def timer(num):
    border1 = "┌──────────────────────────────┐"
    print(border1.center(shutil.get_terminal_size().columns))
    count(1)
    if num > 0:
        while num >= 0:
            center_in_console = shutil.get_terminal_size().columns
            mins, secs = divmod(num, 60)
            for_screen = "{:02d}:{:02d}".format(mins, secs)
            # new_print = print(for_screen, end="\r")
            print(for_screen.center(center_in_console), end="\r")
            num = num - 1
            sleep(1)
        print()
    else:
        if_zero = "00:00"
        print(if_zero.center(shutil.get_terminal_size().columns))
    print()
    count(0)
    border2 = "└──────────────────────────────┘"
    print(border2.center(shutil.get_terminal_size().columns))
    print()
    credit1 = "Thank You for using Timer."
    credit2 = "- Made by Raunak Pyakurel"
    print(credit1.center(shutil.get_terminal_size().columns))
    print(credit2.center(shutil.get_terminal_size().columns))
    print()


print()
all_hash = "#######################################"
some_hash = "###                                 ###"
message_hash = "###     Countdown Timer Program     ###"
print(all_hash.center(shutil.get_terminal_size().columns))
print(message_hash.center(shutil.get_terminal_size().columns))
print(all_hash.center(shutil.get_terminal_size().columns))
print()

num = int(input("Enter time in seconds: "))
call_function = timer(num)
