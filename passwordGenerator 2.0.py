import string
import random

password = ''
char = list(string.ascii_letters)
char.extend(list(range(10)))

password_length = int(input("Choose how long you want your password to be (8-16 characters): "))
if not password_length >= 8 or not password_length <= 16:
    print('wrong length')
    quit()

for i in range(password_length + 1):
    ran_num = random.randint(0,61)
    password = password + str(char[ran_num])

print("Here is your randomly generated password: " + password)