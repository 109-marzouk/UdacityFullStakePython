class Player:
	def __init__(self, name, letter, score):
		self.name = name
		self.letter = letter
		self.score = score
	def CheckWinner(self, my_dict):
		if my_dict['1'] + my_dict['2'] + my_dict['3'] == self.letter * 3:
			return "winner"
		elif my_dict['4'] + my_dict['5'] + my_dict['6'] == self.letter * 3:
			return "winner"
		elif my_dict['7'] + my_dict['8'] + my_dict['9'] == self.letter * 3:
			return "winner"
		elif my_dict['7'] + my_dict['4'] + my_dict['1'] == self.letter * 3:
			return "winner"
		elif my_dict['8'] + my_dict['5'] + my_dict['2'] == self.letter * 3:
			return "winner"
		elif my_dict['9'] + my_dict['6'] + my_dict['3'] == self.letter * 3:
			return "winner"
		elif my_dict['7'] + my_dict['5'] + my_dict['3'] == self.letter * 3:
			return "winner"
		elif my_dict['9'] + my_dict['5'] + my_dict['1'] == self.letter * 3:
			return "winner"
		return "not winner"

