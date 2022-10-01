import shutil
from time import sleep


def timer(num):
    print("The Countdown has started: ")
    while num >= 0:
        print(num)
        num = num - 1
        sleep(1)
    z = "The Countdown has finished!"
    print()
    print(z.center(shutil.get_terminal_size().columns))
    print()


print()
a = "#######################################"
b = "###                                 ###"
c = "###         Countdown Timer         ###"
print(a.center(shutil.get_terminal_size().columns))
print(c.center(shutil.get_terminal_size().columns))
print(a.center(shutil.get_terminal_size().columns))
print()

num = int(input("Enter time in seconds: "))
x = timer(num)
