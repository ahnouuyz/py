import random as rd

class Tictactoe:
	def __init__(self):
		self.state = [[0 for _ in range(3)] for _ in range(3)]
		self.positions = set((r, c) for r in range(3) for c in range(3))

	def __repr__(self):
		sll = [[' XO'[val] for val in row] for row in self.state]
		hline = '  ---|---|---'
		render = '   1   2   3 \n'
		render += '   a   b   c \n'
		for i, row in enumerate(sll):
			line = f'{i + 1}' + '  ' + ' | '.join([val for val in row])
			render += line + '\n' + hline + '\n' if i < 2 else line + '\n'
		return render

	def __str__(self):
		return self.__repr__()

	def show_positions(self):
		lst = ['abc'[c] + '123'[r] for r, c in self.positions]
		return ' '.join(sorted(lst))

	def input_position(self):
		print(self.__repr__())
		print(f'Available positions: {self.show_positions()}')
		usr_input = input('("q" to quit) Input a "a1"-"c3" or "row,col": ')
		if usr_input[0].lower() == 'q':
			return 'quit'
		elif usr_input[0].lower() in 'abc' and usr_input[1] in '123':
			r = '123'.index(usr_input[1])
			c = 'abc'.index(usr_input[0].lower())
			if (r, c) in self.positions:
				return r, c
		else:
			delimiters = ',;:-_/.*~|\t '
			mask = [delimiter in usr_input for delimiter in delimiters]
			if any(mask):
				delimiter = delimiters[mask.index(True)]
				lst = usr_input.split(delimiter)[:2]
				lst = list(map(str.strip, lst))
				if all(val in '123' for val in lst):
					r, c = tuple(map(int, lst))
					r, c = r - 1, c - 1
					if (r, c) in self.positions:
						return r, c

	def update_state(self, player, pos):
		r, c = pos
		self.state[r][c] = player
		self.positions -= {pos}

	def find_winner(self):
		rows = self.state
		cols = list(zip(*rows))
		diag1 = [[rows[i][i] for i in range(3)]]
		diag2 = [[rows[2 - i][i] for i in range(3)]]
		trips = rows + cols + diag1 + diag2
		for trip in trips:
			if 0 in trip:
				continue
			elif all(val == 1 for val in trip):
				return 1
			elif all(val == 2 for val in trip):
				return 2

	def run_2_players(self):
		while len(self.positions) > 0:
			move = 10 - len(self.positions)
			player = (2, 1)[move % 2]
			print(f'\nRound {move}: It is Player {player}\'s turn:')

			pos = self.input_position()
			if pos == 'quit':
				break
			elif pos in self.positions:
				self.update_state(player, pos)
				winner = self.find_winner()
				if winner:
					break
			else:
				print('\nInvalid move! Please try again...')

		print(self.__repr__())
		if pos == 'quit':
			print('Game terminated.')
		elif winner:
			print(f'Game over! Player {winner} won!')
		else:
			print('Game over! It\'s a draw!')

	def defend8(self, player):
		other = (0, 2, 1)[player]
		rows = self.state
		cols = list(zip(*rows))
		for r in range(len(rows)):
			mask = [val == other for val in rows[r]]
			if sum(mask) > 1 and 0 in rows[r]:
				c = mask.index(False)
				return r, c
		for c in range(len(cols)):
			mask = [val == other for val in cols[c]]
			if sum(mask) > 1 and 0 in cols[c]:
				r = mask.index(False)
				return r, c
		mask = [rows[i][i] == other for i in range(3)]
		if sum(mask) > 1 and 0 in [rows[i][i] for i in range(3)]:
			r = mask.index(False)
			return r, r
		mask = [rows[2 - i][i] == other for i in range(3)]
		if sum(mask) > 1 and 0 in [rows[2 - i][i] for i in range(3)]:
			c = mask.index(False)
			return 2 - c, c
		return False

	def easy_mode(self):
		if (1, 1) in self.positions:
			return 1, 1
		else:
			return rd.sample(self.positions, 1)[0]

	def med_mode(self, player):
		if (1, 1) in self.positions:
			return 1, 1
		else:
			pos = self.defend8(player)
			if pos:
				return pos
			else:
				return rd.sample(self.positions, 1)[0]
		
	def run_1_player(self):
		while len(self.positions) > 0:
			move = 10 - len(self.positions)
			player = (2, 1)[move % 2]

			if player == 2:
				pos = self.med_mode(player)
			else:
				print(f'\nRound {move}: It is your turn:')
				pos = self.input_position()

			if pos == 'quit':
				break
			elif pos:
				self.update_state(player, pos)
				if player == 2:
					print('Computer chose:', pos)
				winner = self.find_winner()
				if winner:
					break
			else:
				print('\nInvalid move! Please try again...')

		print(self.__repr__())
		if pos == 'quit':
			print('Game terminated.')
		elif winner:
			print(f'Game over! Player {winner} won!')
		else:
			print('Game over! It\'s a draw!')

if __name__ == '__main__':
	game = Tictactoe()
	print('Select mode: \n1:  1-player\n2:  2-players')
	mode = int(input('Mode: ')[0])
	if mode == 1:
		game.run_1_player()
	elif mode == 2:
		game.run_2_players()
	else:
		print('Exiting...')

