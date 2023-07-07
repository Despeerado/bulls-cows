
from validation import *
 
def matches(user_input, computer_number):

	user_list = list(user_input)
	computer_list = list(computer_number)

	bulls = 0
	cows = 0

	for i in range(4):
		if computer_list[i] == user_list[i]:
			bulls +=1
		elif user_list[i] in computer_list:
			cows +=1	
			
	return bulls, cows

def switch_suffix(bulls, cows):
	bull_suffix = 0
	cow_suffix = 0

	if bulls == 1:
		bull_suffix = "bull"
	else:
		bull_suffix = "bulls"

	if cows == 1:
		cow_suffix = "cow"
	else:
		cow_suffix = "cows"
	
	print(str(bulls) + ' ' + bull_suffix + ',' + ' ' + str(cows) + ' ' + cow_suffix)
	
def game():
	""" start the game"""
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

		user_input = validation()

		bulls, cows = matches(user_input, computer_number)

		switch_suffix(bulls, cows)

		condition_iteration +=1

		if condition_iteration <= 4:
			rating = "amazing!"
		elif condition_iteration < 10:
			rating = "average."
		else:
			rating = "not great, not terrible."

		if bulls == 4:
			condition = False
			print(f"Correct, you've guessed the right number {condition_iteration} guesses!")
			print(50*'-')
			print(f"it is {rating}")

if __name__ == "__main__":
	game()