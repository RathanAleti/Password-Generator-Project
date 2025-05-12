import random
# Declaring the letters named list and storing the words which are require for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#Declaring the numbers named list and storing the numbers which are require for the password
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#Declaring the symbols named list and storing the symbols which are require for the password
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome the user to my Password Generator
print("Welcome to the PyPassword Generator!")
# Asking the users for input,How many letters they want in their password
numbers_of_letters = int(input("How many letters would you like in your password?\n"))
#asking users for input, How many symbols they want in their password
number_of_symbols = int(input(f"How many symbols would you like?\n"))
#asking users for input,How many numbers they want in their password
number_of_numbers = int(input(f"How many numbers would you like?\n"))

password = []
# used for loop and used range to get track of number of letters the user want 
for a in range (0, numbers_of_letters):
    #used random choice for pick different letter for the password and used .append function to add each of the letter
    password.append(random.choice(letters))
for a in range (0,number_of_symbols):
   password.append(random.choice(numbers))
for a in range (0,number_of_numbers):
    password.append(random.choice(symbols))
print(password)
#Used random shuffle
random.shuffle(password)
print(password)

passkey = " "
for a in password:
    passkey += a

print(f"Your password is: {passkey}")
    

