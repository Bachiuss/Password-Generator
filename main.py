# Password Generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my empire! I am gonna generate your password")

inp_letters = int(input("How many letters would you like to have?\n"))
inp_numbers = int(input("How many numbers?\n"))
inp_symbols = int(input("How many symbols?\n"))

password_list = []

for i in range(1, inp_letters + 1):
    password_list.append(random.choice(letters))
for j in range(1, inp_numbers + 1):
    password_list.append((random.choice(numbers)))
for k in range(1, inp_symbols + 1):
    password_list.append((random.choice(symbols)))
# print(password_list)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(password)

