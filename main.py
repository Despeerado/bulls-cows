""" definice samotne hry"""

from validation import *


def matches(user_input, computer_number):
	user_set = set(user_input)
	computer_set = set(computer_number)

	a = len(user_set.intersection(computer_set))
	# print(f"Typ:{type(a)}")
	# print(f"Length:{a}")
	# spravna cisla na spatnem miste pomoci setu

	intersectioned_numbers = 0

	for i in range(a):
		if a >=1:
			intersectioned_numbers +=1 
	
	# print(intersectioned_numbers)
	cows = intersectioned_numbers
	# print(f"Cows:{cows}")
	# print(f"pocet pruniku je{intersectioned_numbers}")
	# pokud je user input spravny, pokracuje dalsi cast.
	user_list = list(user_input)
	computer_list = list(computer_number)

	list_matches = 0

	for i in range(len(user_list)):
			if user_list[i] == computer_list[i]:
				list_matches += 1
	# print(user_list)
	# print(computer_list)
	# print(list_matches)
	bulls = list_matches  # spravne cislo na spravnem umisteni
	# print(f"Bulls:{bulls}")
	
	return bulls, cows

def switch_case(bulls, cows):
	if bulls == 0 and cows == 0:
		print(f"{bulls} Bulls, {cows} cows")
	elif bulls == 0 and cows == 1:
		print(f"{bulls} Bulls, {cows} cow")
	elif bulls == 1 and cows == 0:
		print(f"{bulls} Bull, {cows} cows")
	elif bulls == 1 and cows == 1:
		print(f"{bulls} Bull, {cows} cow")
	# uz cisla
	elif bulls == 0 and cows >=2:
		print(f"{bulls} Bulls, {cows} cows")
	elif bulls >=2 and cows == 0:
		print(f"{bulls} Bulls, {cows} cows")
	elif bulls >=2 and cows >=2:
		print(f"{bulls} Bulls, {cows} cows")
	else:
		print("zapomnel jsi na dalsi variantu")

def game():
	""" spusti hru"""
	print("Hi there!")
	print(50*'-')
	print("I've generated a random four digit number for you. Let's play a bulls and cows game.")
	computer_number = computer_generator()

	# print(generated_number)
	print(50*'-')
	print("Enter a number: ")
	print(50*'-')

	condition_iteration = 0
	
	condition = True
	
	while condition:
		# probiha validace
		user_input = validation()
		bulls, cows = matches(user_input, computer_number)
		switch_case(bulls, cows)
		# print(bulls)
		# print(cows)
		condition_iteration +=1

		if condition_iteration <= 4:
			rating = "amazing!"
		elif condition_iteration < 10:
			rating = "average."
		else:
			rating = "Not great, not terrible."

		if bulls == 4:
			condition = False
			print(f"Correct, you've guessed the right number {condition_iteration} guesses!")
			print(50*'-')
			print(f"it is {rating}")

if __name__ == "__main__":
	game()