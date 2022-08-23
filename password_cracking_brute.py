from random import *

inp_pswd = input("Enter your password : ")

password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z',]

guess = ""
while (guess != inp_pswd):
    guess = ""
    for letter in range(len(inp_pswd)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
    print(guess)

print("Your password is : ",guess)