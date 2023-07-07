"""
bulls_and_cows.py: Druhy projekt do Engeto Online Python Akademie
autor: Dominik Beran
email: d.beran27@gmail.com
discord: Despeerado#8409
"""

import random

# nahodne cislo generovane pocitacem

def computer_generator():
    """
    nahodne ctyrciferne cislo, nezacinajici nulou, generovane pocitacem
    """
    random_numbers = random.sample(range(1,10), 4)

    list_numbers = [str(i) for i in random_numbers]

    computer_number = "".join(list_numbers)
    # print(computer_number)
    return computer_number

def validation():
    """ user input validation"""
    while True:
        user_input = (input(">>>" + " "))
        if user_input.isdigit():
            # converting user_input to a set for comparison
            duplications_control = set(user_input)
            # if the lengths match, the program will execute; otherwise, it will display an error  message
            if len(duplications_control) == len(user_input):
                # I am using variables for better loop readability
                digit = user_input
                non_zero_index = user_input[0] != "0"
                length = len(user_input) == 4

                if digit and non_zero_index:
                    if length:

                        return user_input
                    else:
                        print("Number must have 4 numbers!")
                else:
                    print("User input must be a number and cannot start with zero!")
            else:
                print("There are duplications in this number.")
        else:
            print("You can write only numbers.")