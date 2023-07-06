"""
bulls_and_cows.py: Druhy projekt do Engeto Online Python Akademie
autor: Dominik Beran
email: d.beran27@gmail.com
discord: Despeerado#8409
Program pozdraví užitele a vypíše úvodní text
Program dále vytvoří tajné 4místné číslo (číslice musí být unikátní a nesmí začínat 0)
Hráč hádá číslo. Program jej upozorní, pokud zadá číslo kratší nebo delší než 4 čísla, pokud bude obsahovat duplicity, začínat nulou, příp. obsahovat nečíselné znaky
Program vyhodnotí tip uživatele
Program dále vypíše počet bull/ bulls (pokud uživatel uhodne jak číslo, tak jeho umístění), příp. cows/ cows (pokud uživatel uhodne pouze číslo, ale ne jeho umístění). # Vrácené ohodnocení musí brát ohled na jednotné a množné číslo ve výstupu. Tedy 1 bull a 2 bulls (stejně pro cow/cows).
"""

import random

# nahodne cislo generovane pocitacem

def computer_generator():
    """
    nahodne ctyrciferne cislo, nezacinajici nulou, generovane pocitacem
    """
    random_numbers = random.sample(range(1,10), 4)
    list_numbers = []

    for i in random_numbers:
        list_numbers.append(str(i))

    computer_number = "".join(list_numbers)
    print(computer_number)
    return computer_number

# pro kontrolu, muzu vymazat
# generated_number = computer_generator()

def validation():
    """ validace user inputu"""
    user_input = (input(">>>" + " "))
    if user_input.isdigit():
        # prevedeni user_input do setu kvuli porovnani
        duplications_control = set(user_input)
        # pokud se delky shoduji, program se vykona, jinak vypise chybovou hlasku
        if len(duplications_control) == len(user_input):

            # vyuzivam promennych pro vetsi prehlednost smycek
            digit = user_input
            non_zero_index = user_input[0] != "0"
            length = len(user_input) == 4

            if digit and non_zero_index:
                if length:
                    # print(f">>> {user_input}")
                    return user_input
                else:
                    print("Number must have at least 4 numbers!")
            else:
                print("User input must be a number and cannot start with zero!")
        else:
            print("There are duplications in this number.")
    else:
        print("You can write only numbers.")

    print(50*'-')
    print(user_input)