import random

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []


YELLOW = "\033[1;33m"
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

print(YELLOW)
print("""

██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░
""")
print("""
                    ░██████╗░███████╗███╗░░██╗
                    ██╔════╝░██╔════╝████╗░██║
                    ██║░░██╗░█████╗░░██╔██╗██║
                    ██║░░╚██╗██╔══╝░░██║╚████║
                    ╚██████╔╝███████╗██║░╚███║
                    ░╚═════╝░╚══════╝╚═╝░░╚══╝
""")

print(RED)
print("Lengh of password ? (default 64)")

length = input("Answer : ")
if length == '':
    length = 64
else:
    length = int(length)

#randomly select ascii character classes and individual characters

while count < length:
    rand = random.randint (0,3)
    if rand == 0:
        lower += 1
        lower_letter = int(random.randint (97,123))
        password.append(lower_letter)
    elif rand == 1:
        upper += 1
        upper_letter = random.randint (65,91)
        password.append(upper_letter)
    elif rand == 2:
        number += 1
        number_char = random.randint (48,58)
        password.append(number_char)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            symbol_gen = random.randint (33,48)
            password.append(symbol_gen)
        elif r == 1:
            symbol_gen = random.randint (91,97)
            password.append(symbol_gen)
        elif r == 2:
            symbol_gen = random.randint (123,126)
            password.append(symbol_gen)
    count += 1

password_end = "".join([chr(i) for i in password])

print(YELLOW)
print ("Random password of length %s is: \n" % length)
print(GREEN)
print('******')
print(password_end)
print('******')
print(BLUE)
print ("\nIt contains",lower,"lowercase,",upper,"uppercase,",number,"numbers and",symbol,"symbol characters")
input('Push a button to exit...')