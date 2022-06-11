import random

print ("Welcome to ROCK PAPER SCISSORS by Henry")

# defining game options
game_options = ["P", "R", "S"]

while True:

	# taking input from player
	player_choice = input(f'Please pick an option between "R", "P" or "S" ').upper()

	# computer randomly selecting an option
	comp_choice = random.choice(game_options)
	
	# checking if players choice is valid
	while True:
		if player_choice  not in game_options:
			player_choice = input(f'Please select a valid option "R", "P" or "S" ').upper()
		else:
			break

	# displaying players choice if its valid
	options_dict = {"P":"Paper", "R":"Rock", "S":"Scissors"}
	print (f'Player ({options_dict[player_choice]}) : CPU ({options_dict[comp_choice]})')

	# defining game conditions
	if player_choice == comp_choice:
		print(f'Its a tie, you picked same option as Computer')

	elif (comp_choice == "R" and player_choice == "S"):
		print(f'Rock beats Scissors \n'
			'Computer is the winner')
		break

	elif (comp_choice == "P" and player_choice == "R"):
		print(f'Paper beats Rock \n'
			'Computer is the winner')
		break

	elif (comp_choice == "S" and player_choice == "P"):
		print(f'Scissors beats Paper \n'
			'Computer is the winner')
		break

	elif (comp_choice == "S" and player_choice == "R"):
		print(f'Rock beats Scissors \n'
			'Player is the winner')
		break

	elif (comp_choice == "R" and player_choice == "P"):
		print(f'Paper beats Rock \n'
			'Player is the winner')
		break

	elif (comp_choice == "P" and player_choice == "S"):
		print(f'Scissors beats Paper \n'
			'Computer is the winner')
		break