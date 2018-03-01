from player import Player # Import Player Class
from random import choice # Import choice Class
import time
def Board_print():
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + places_in_board['7'] + "  |  " + places_in_board['8'] + "  |  " + places_in_board['9'] + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + places_in_board['4'] + "  |  " + places_in_board['5'] + "  |  " + places_in_board['6'] + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + places_in_board['1'] + "  |  " + places_in_board['2'] + "  |  " + places_in_board['3'] + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
def Board_print_with_nums():
	print "Every place in the box represented by a number You Choose choose the number of the place where you want to put your Letter"
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + '7' + "  |  " + '8' + "  |  " + '9' + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + '4' + "  |  " + '5' + "  |  " + '6' + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + '1' + "  |  " + '2' + "  |  " + '3' + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"	
print "Welcome In My Game By Mohamed Marzouk \n====================================="
print "Enter : \n\t[1] To play With Computer\n\t[2] 2 Player"
user_choose = raw_input("Enter your selection here: ")
while user_choose != "1" and user_choose != "2":
	print "Error Input"
	print "Enter : \n\t[1] To play With Computer\n\t[2] 2 Player"
	user_choose = raw_input("Enter your selection here: ")

if user_choose == "1":
	player_name = raw_input("Enter Your Name: ")
	player_letter = raw_input(player_name + " Enter Your Letter: ").replace(' ', '').upper()
	if player_letter == "X":
		computer_letter = "O"
	elif player_letter == "O":
		computer_letter = "X"
	else:
		while player_letter != "X" and player_letter !=  "O":
			print "You Should choose X or O only"
			player_letter = raw_input(player_name + " Enter Your Letter: ").upper()
	player = Player(player_name, player_letter, 0)
	computer = Player("Computer", computer_letter, 0)
	print "Enter : \n\t[1] Easy\n\t[2] Hard"
	game_level = raw_input("Choose the level of the game: ")
	while game_level != "1" and game_level != "2":
		print "Error Input"
		print "Enter : \n\t[1] To play With Computer\n\t[2] 2 Player"
		game_level = raw_input("Enter your selection here: ")
	print "\n\nGame Started"
	Board_print_with_nums()
	header_score = "||       " + player.name + "( " + player.letter + " ): " + str(player.score) + "     ||      " + computer.name + "( " + computer.letter + " ): " + str(computer.score) + "      ||"
	print "=" * len(header_score)
	print header_score
	print "=" * len(header_score)
	continue_game = "y"
	while continue_game == "y":
		places_in_board = {"1":" ", # Bottom Left
						"2": " ", # Bottom Center
						"3": " ", # Bottom Right
						"4": " ", # Center Left
						"5": " ", # Center Center
						"6": " ", # Center Right
						"7": " ", # Top Left
						"8": " ", # Top Center
						"9": " ", # Top Right
						}
		count = 0
		Board_print()
		while True:
			computer_input_list = [x for x in places_in_board.keys() if places_in_board[x] == " "]
			if player.CheckWinner(places_in_board) == "winner":
				print player.name + "! You are The Winner"
				player.score += 1
				header_score = "||       " + player.name + "( " + player.letter + " ): " + str(player.score) + "     ||      " + computer.name + "( " + computer.letter + " ): " + str(computer.score) + "      ||"
				print "=" * len(header_score)
				print header_score
				print "=" * len(header_score)
				break
			elif computer.CheckWinner(places_in_board) == "winner":
				print "The " + computer.name + " is The Winner"
				computer.score += 1
				header_score = "||       " + player.name + "( " + player.letter + " ): " + str(player.score) + "     ||      " + computer.name + "( " + computer.letter + " ): " + str(computer.score) + "      ||"
				print "=" * len(header_score)
				print header_score
				print "=" * len(header_score)
				break
			else:
				if " " not in places_in_board.values():
					print "Draw!"
					header_score = "||       " + player.name + "( " + player.letter + " ): " + str(player.score) + "     ||      " + computer.name + "( " + computer.letter + " ): " + str(computer.score) + "      ||"
					print "=" * len(header_score)
					print header_score
					print "=" * len(header_score)
					break
			player_input = raw_input(player.name + ": ").replace(' ', '')
			while player_input not in places_in_board.keys() or places_in_board[player_input] != " ":
				print "Sorry this place is full or Does not exist"
				player_input = raw_input(player.name + ": ").replace(' ', '')
			places_in_board[player_input] = player.letter
			computer_input_list.remove(player_input)
			Board_print()
			if player.CheckWinner(places_in_board) == "winner":
				print player.name + "! You are The Winner"
				player.score += 1
				header_score = "||       " + player.name + "( " + player.letter + " ): " + str(player.score) + "     ||      " + computer.name + "( " + computer.letter + " ): " + str(computer.score) + "      ||"
				print "=" * len(header_score)
				print header_score
				print "=" * len(header_score)
				break
			elif computer.CheckWinner(places_in_board) == "winner":
				print "The " + computer.name + " is The Winner1"
				computer.score += 1
				header_score = "||       " + player.name + "( " + player.letter + " ): " + str(player.score) + "     ||      " + computer.name + "( " + computer.letter + " ): " + str(computer.score) + "      ||"
				print "=" * len(header_score)
				print header_score
				print "=" * len(header_score)
				break
			else:
				if " " not in places_in_board.values():
					print "Draw!"
					header_score = "||       " + player.name + "( " + player.letter + " ): " + str(player.score) + "     ||      " + computer.name + "( " + computer.letter + " ): " + str(computer.score) + "      ||"
					print "=" * len(header_score)
					print header_score
					print "=" * len(header_score)
					break
			time.sleep(1)
			if game_level == "1":
				computer_input = choice(computer_input_list)
				computer_input_list.remove(computer_input)
			elif game_level == "2":
				while count < 1:
					computer_input = choice(computer_input_list)
					computer_input_list.remove(computer_input)
					count += 1 
				if places_in_board['1'] + places_in_board['2'] == computer.letter * 2 and places_in_board['3'] == " ":
					computer_input = '3'
				elif places_in_board['1'] + places_in_board['3'] == computer.letter * 2 and places_in_board['2'] == " ":
					computer_input = '2'
				elif places_in_board['2'] + places_in_board['3'] == computer.letter * 2 and places_in_board['1'] == " ":
					computer_input = '1'
				elif places_in_board['4'] + places_in_board['5'] == computer.letter * 2 and places_in_board['6'] == " ":
					computer_input = '6'
				elif places_in_board['4'] + places_in_board['6'] == computer.letter * 2 and places_in_board['5'] == " ":
					computer_input = '5'
				elif places_in_board['5'] + places_in_board['6'] == computer.letter * 2 and places_in_board['4'] == " ":
					computer_input = '4'
				elif places_in_board['7'] + places_in_board['8'] == computer.letter * 2 and places_in_board['9'] == " ":
					computer_input = '9'
				elif places_in_board['7'] + places_in_board['9'] == computer.letter * 2 and places_in_board['8'] == " ":
					computer_input = '8'
				elif places_in_board['8'] + places_in_board['9'] == computer.letter * 2 and places_in_board['7'] == " ":
					computer_input = '7'
				elif places_in_board['1'] + places_in_board['4'] == computer.letter * 2 and places_in_board['7'] == " ":
					computer_input = '7'
				elif places_in_board['1'] + places_in_board['7'] == computer.letter * 2 and places_in_board['4'] == " ":
					computer_input = '4'
				elif places_in_board['4'] + places_in_board['7'] == computer.letter * 2 and places_in_board['1'] == " ":
					computer_input = '1'
				elif places_in_board['2'] + places_in_board['5'] == computer.letter * 2 and places_in_board['8'] == " ":
					computer_input = '8'
				elif places_in_board['2'] + places_in_board['8'] == computer.letter * 2 and places_in_board['5'] == " ":
					computer_input = '5'
				elif places_in_board['5'] + places_in_board['8'] == computer.letter * 2 and places_in_board['2'] == " ":
					computer_input = '2'
				elif places_in_board['3'] + places_in_board['6'] == computer.letter * 2 and places_in_board['9'] == " ":
					computer_input = '9'
				elif places_in_board['3'] + places_in_board['9'] == computer.letter * 2 and places_in_board['6'] == " ":
					computer_input = '6'
				elif places_in_board['6'] + places_in_board['9'] == computer.letter * 2 and places_in_board['3'] == " ":
					computer_input = '3'
				elif places_in_board['3'] + places_in_board['5'] == computer.letter * 2 and places_in_board['7'] == " ":
					computer_input = '7'
				elif places_in_board['3'] + places_in_board['7'] == computer.letter * 2 and places_in_board['5'] == " ":
					computer_input = '5'
				elif places_in_board['5'] + places_in_board['7'] == computer.letter * 2 and places_in_board['3'] == " ":
					computer_input = '3'
				elif places_in_board['1'] + places_in_board['5'] == computer.letter * 2 and places_in_board['9'] == " ":
					computer_input = '9'
				elif places_in_board['1'] + places_in_board['9'] == computer.letter * 2 and places_in_board['5'] == " ":
					computer_input = '5'
				elif places_in_board['5'] + places_in_board['9'] == computer.letter * 2 and places_in_board['1'] == " ":
					computer_input = '1'
				elif places_in_board['1'] + places_in_board['2'] == player.letter * 2 and places_in_board['3'] == " ":
					computer_input = '3'
				elif places_in_board['1'] + places_in_board['3'] == player.letter * 2 and places_in_board['2'] == " ":
					computer_input = '2'
				elif places_in_board['2'] + places_in_board['3'] == player.letter * 2 and places_in_board['1'] == " ":
					computer_input = '1'
				elif places_in_board['4'] + places_in_board['5'] == player.letter * 2 and places_in_board['6'] == " ":
					computer_input = '6'
				elif places_in_board['4'] + places_in_board['6'] == player.letter * 2 and places_in_board['5'] == " ":
					computer_input = '5'
				elif places_in_board['5'] + places_in_board['6'] == player.letter * 2 and places_in_board['4'] == " ":
					computer_input = '4'
				elif places_in_board['7'] + places_in_board['8'] == player.letter * 2 and places_in_board['9'] == " ":
					computer_input = '9'
				elif places_in_board['7'] + places_in_board['9'] == player.letter * 2 and places_in_board['8'] == " ":
					computer_input = '8'
				elif places_in_board['8'] + places_in_board['9'] == player.letter * 2 and places_in_board['7'] == " ":
					computer_input = '7'
				elif places_in_board['1'] + places_in_board['4'] == player.letter * 2 and places_in_board['7'] == " ":
					computer_input = '7'
				elif places_in_board['1'] + places_in_board['7'] == player.letter * 2 and places_in_board['4'] == " ":
					computer_input = '4'
				elif places_in_board['4'] + places_in_board['7'] == player.letter * 2 and places_in_board['1'] == " ":
					computer_input = '1'
				elif places_in_board['2'] + places_in_board['5'] == player.letter * 2 and places_in_board['8'] == " ":
					computer_input = '8'
				elif places_in_board['2'] + places_in_board['8'] == player.letter * 2 and places_in_board['5'] == " ":
					computer_input = '5'
				elif places_in_board['5'] + places_in_board['8'] == player.letter * 2 and places_in_board['2'] == " ":
					computer_input = '2'
				elif places_in_board['3'] + places_in_board['6'] == player.letter * 2 and places_in_board['9'] == " ":
					computer_input = '9'
				elif places_in_board['3'] + places_in_board['9'] == player.letter * 2 and places_in_board['6'] == " ":
					computer_input = '6'
				elif places_in_board['6'] + places_in_board['9'] == player.letter * 2 and places_in_board['3'] == " ":
					computer_input = '3'
				elif places_in_board['3'] + places_in_board['5'] == player.letter * 2 and places_in_board['7'] == " ":
					computer_input = '7'
				elif places_in_board['3'] + places_in_board['7'] == player.letter * 2 and places_in_board['5'] == " ":
					computer_input = '5'
				elif places_in_board['5'] + places_in_board['7'] == player.letter * 2 and places_in_board['3'] == " ":
					computer_input = '3'
				elif places_in_board['1'] + places_in_board['5'] == player.letter * 2 and places_in_board['9'] == " ":
					computer_input = '9'
				elif places_in_board['1'] + places_in_board['9'] == player.letter * 2 and places_in_board['5'] == " ":
					computer_input = '5'
				elif places_in_board['5'] + places_in_board['9'] == player.letter * 2 and places_in_board['1'] == " ":
					computer_input = '1'
				else:
					computer_input = choice(computer_input_list)
			places_in_board[computer_input] = computer.letter
			Board_print()
		continue_game = raw_input("Enter y To continue or any letter to Close this Game: ")
elif user_choose == "2":
	first_player_name = raw_input("Enter First Player Name: ")
	second_player_name = raw_input("Enter Second Player Name: ")
	print "Choose X or O only"
	first_player_letter = raw_input(first_player_name + " Enter Your Letter: ").replace(' ', '')
	first_player_letter = first_player_letter.upper()
	if first_player_letter == "X":
		second_player_letter = "O"
	elif first_player_letter == "O":
		second_player_letter = "X"
	else:
		while first_player_letter != "X" and first_player_letter !=  "O":
			print "You Should choose X or O only"
			first_player_letter = raw_input(first_player_name + " Enter Your Letter: ").upper()
	first_player = Player(first_player_name, first_player_letter, 0)
	second_player = Player(second_player_name, second_player_letter, 0)
	header_score = "||       " + first_player.name + "( " + first_player.letter + " ): " + str(first_player.score) + "     ||      " + second_player.name + "( " + second_player.letter + " ): " + str(second_player.score) + "      ||"
	print "=" * len(header_score)
	print header_score
	print "=" * len(header_score)
	Board_print_with_nums()
	print "\n\nGame Started"
	continue_game = "y"
	while continue_game == "y":
		places_in_board = {"1":" ", # Bottom Left
						"2": " ", # Bottom Center
						"3": " ", # Bottom Right
						"4": " ", # Center Left
						"5": " ", # Center Center
						"6": " ", # Center Right
						"7": " ", # Top Left
						"8": " ", # Top Center
						"9": " ", # Top Right
						}
		Board_print()
		while True:
			if first_player.CheckWinner(places_in_board) == "winner":
				print first_player.name + "! You are The Winner"
				first_player.score += 1
				header_score = "||       " + first_player.name + "( " + first_player.letter + " ): " + str(first_player.score) + "     ||      " + second_player.name + "( " + second_player.letter + " ): " + str(second_player.score) + "      ||"
				print "=" * len(header_score)
				print header_score
				print "=" * len(header_score)
				break
			elif second_player.CheckWinner(places_in_board) == "winner":
				print "The " + second_player.name + " is The Winner"
				second_player.score += 1
				header_score = "||       " + first_player.name + "( " + first_player.letter + " ): " + str(first_player.score) + "     ||      " + second_player.name + "( " + second_player.letter + " ): " + str(second_player.score) + "      ||"
				print "=" * len(header_score)
				print header_score
				print "=" * len(header_score)
				break
			else:
				if " " not in places_in_board.values():
					print "Draw!"
					header_score = "||       " + first_player.name + "( " + first_player.letter + " ): " + str(first_player.score) + "     ||      " + second_player.name + "( " + second_player.letter + " ): " + str(second_player.score) + "      ||"
					print "=" * len(header_score)
					print header_score
					print "=" * len(header_score)
					break
			first_player_input = raw_input(first_player.name + ": ").replace(' ', '')
			while first_player_input not in places_in_board.keys() or places_in_board[first_player_input] != " ":
				print "Sorry this place is full or Does not exist"
				first_player_input = raw_input(first_player.name + ": ").replace(' ', '')
			places_in_board[first_player_input] = first_player.letter
			Board_print()
			if first_player.CheckWinner(places_in_board) == "winner":
				print first_player.name + "! You are The Winner"
				first_player.score += 1
				header_score = "||       " + first_player.name + "( " + first_player.letter + " ): " + str(first_player.score) + "     ||      " + second_player.name + "( " + second_player.letter + " ): " + str(second_player.score) + "      ||"
				print "=" * len(header_score)
				print header_score
				print "=" * len(header_score)
				break
			elif second_player.CheckWinner(places_in_board) == "winner":
				print "The " + second_player.name + " is The Winner"
				second_player.score += 1
				header_score = "||       " + first_player.name + "( " + first_player.letter + " ): " + str(first_player.score) + "     ||      " + second_player.name + "( " + second_player.letter + " ): " + str(second_player.score) + "      ||"
				print "=" * len(header_score)
				print header_score
				print "=" * len(header_score)
				break
			else:
				if " " not in places_in_board.values():
					print "Draw!"
					header_score = "||       " + first_player.name + "( " + first_player.letter + " ): " + str(first_player.score) + "     ||      " + second_player.name + "( " + second_player.letter + " ): " + str(second_player.score) + "      ||"
					print "=" * len(header_score)
					print header_score
					print "=" * len(header_score)
					break
			second_player_input = raw_input(second_player.name + ": ").replace(' ', '')
			while second_player_input not in places_in_board.keys() or places_in_board[second_player_input] != " ":
				print "Sorry this place is full or Does not exist"
				second_player_input = raw_input(second_player.name + ": ").replace(' ', '')
			places_in_board[second_player_input] = second_player.letter
			Board_print()
		continue_game = raw_input("Enter y To continue or any letter to Close this Game: ")




