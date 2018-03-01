# -*- coding: utf-8 -*-
# By Mohamed Marzouk
# facebook.com/MohamedMarzouk23
# I used the dictionaries in this game more about data type dictionaries
# https://www.tutorialspoint.com/python/python_dictionary.htm
def GameStatus(my_dict):
	if my_dict['1'] + my_dict['2'] + my_dict['3'] == "XXX":
		return "X is The Winner"
	elif my_dict['4'] + my_dict['5'] + my_dict['6'] == "XXX":
		return "X is The Winner"
	elif my_dict['7'] + my_dict['8'] + my_dict['9'] == "XXX":
		return "X is The Winner"
	elif my_dict['7'] + my_dict['4'] + my_dict['1'] == "XXX":
		return "X is The Winner"
	elif my_dict['8'] + my_dict['5'] + my_dict['2'] == "XXX":
		return "X is The Winner"
	elif my_dict['9'] + my_dict['6'] + my_dict['3'] == "XXX":
		return "X is The Winner"
	elif my_dict['7'] + my_dict['5'] + my_dict['3'] == "XXX":
		return "X is The Winner"
	elif my_dict['9'] + my_dict['5'] + my_dict['1'] == "XXX":
		return "X is The Winner"
	elif my_dict['1'] + my_dict['2'] + my_dict['3'] == "OOO":
		return "O is The Winner"
	elif my_dict['4'] + my_dict['5'] + my_dict['6'] == "OOO":
		return "O is The Winner"
	elif my_dict['7'] + my_dict['8'] + my_dict['9'] == "OOO":
		return "O is The Winner"
	elif my_dict['7'] + my_dict['4'] + my_dict['1'] == "OOO":
		return "O is The Winner"
	elif my_dict['8'] + my_dict['5'] + my_dict['2'] == "OOO":
		return "O is The Winner"
	elif my_dict['9'] + my_dict['6'] + my_dict['3'] == "OOO":
		return "O is The Winner"
	elif my_dict['7'] + my_dict['5'] + my_dict['3'] == "OOO":
		return "O is The Winner"
	elif my_dict['9'] + my_dict['5'] + my_dict['1'] == "OOO":
		return "O is The Winner"
	else:
		if " " in my_dict.values():
			return "continue"
		else:
			return "draw"
def Board_print():
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + places_in_board['7'] + "  |  " + places_in_board['8'] + "  |  " + places_in_board['9'] + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + places_in_board['4'] + "  |  " + places_in_board['5'] + "  |  " + places_in_board['6'] + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
	print "|  " + places_in_board['1'] + "  |  " + places_in_board['2'] + "  |  " + places_in_board['3'] + "  |  "
	print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
print "Welcome In My Game By Mohamed Marzouk \n====================================="
first_player_name = raw_input("Enter First Player Name: ").upper()
second_player_name = raw_input("Enter Second Player Name: ").upper()
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
first_player_score = 0
second_player_score = 0
header_score = "||       " + first_player_name + "( " + first_player_letter + " ): " + str(first_player_score) + "     ||      " + second_player_name + "( " + second_player_letter + " ): " + str(second_player_score) + "      ||"
print "=" * len(header_score)
print header_score
print "=" * len(header_score)
print "Every place in the box represented by a number You Choose choose the number of the place where you want to put your Letter"
print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
print "|  " + '7' + "  |  " + '8' + "  |  " + '9' + "  |  "
print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
print "|  " + '4' + "  |  " + '5' + "  |  " + '6' + "  |  "
print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"
print "|  " + '1' + "  |  " + '2' + "  |  " + '3' + "  |  "
print "*" + "-" * 5 + "*" + "-" * 5 + "*" + "-" * 5 + "*"

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
		if "Winner" in GameStatus(places_in_board):
			print GameStatus(places_in_board)
			if "X" in GameStatus(places_in_board) and first_player_letter == "X":
				first_player_score += 1
			elif "O" in GameStatus(places_in_board) and first_player_letter == "O":
				first_player_score += 1
			elif "X" in GameStatus(places_in_board) and second_player_letter == "X":
				second_player_score += 1
			elif "O" in GameStatus(places_in_board) and second_player_letter == "O":
				second_player_score += 1
			header_score = "||       " + first_player_name + "( " + first_player_letter + " ): " + str(first_player_score) + "     ||      " + second_player_name + "( " + second_player_letter + " ): " + str(second_player_score) + "      ||"
			print "=" * len(header_score)
			print header_score
			print "=" * len(header_score)
			break
		elif GameStatus(places_in_board) == "draw":
			print "Draw!"
			break
		first_player = raw_input(first_player_name + ": ").replace(' ', '')
		while first_player not in places_in_board.keys() or places_in_board[first_player] != " ":
			print "Sorry this place is full or Does not exist"
			first_player = raw_input(first_player_name + ": ").replace(' ', '')
		places_in_board[first_player] = first_player_letter
		Board_print()
		if "Winner" in GameStatus(places_in_board):
			print GameStatus(places_in_board)
			if "X" in GameStatus(places_in_board) and first_player_letter == "X":
				first_player_score += 1
			elif "O" in GameStatus(places_in_board) and first_player_letter == "O":
				first_player_score += 1
			elif "X" in GameStatus(places_in_board) and second_player_letter == "X":
				second_player_score += 1
			elif "O" in GameStatus(places_in_board) and second_player_letter == "O":
				second_player_score += 1
			header_score = "||       " + first_player_name + "( " + first_player_letter + " ): " + str(first_player_score) + "     ||      " + second_player_name + "( " + second_player_letter + " ): " + str(second_player_score) + "      ||"
			print "=" * len(header_score)
			print header_score
			print "=" * len(header_score)
			break
		elif GameStatus(places_in_board) == "draw":
			print "Draw!"
			break
		second_player = raw_input(second_player_name + ": ").replace(' ', '')
		while second_player not in places_in_board.keys() or places_in_board[second_player] != " ":
			print "Sorry this place is full or Does not exist"
			second_player = raw_input(second_player_name + ": ").replace(' ', '')
		places_in_board[second_player] = second_player_letter
		Board_print()
	continue_game = raw_input("Enter y To continue or any letter to Close this Game: ")




