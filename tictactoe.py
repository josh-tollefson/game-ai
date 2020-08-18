import numpy as np
import random

class TicTacToe():

	def __init__(self, player1, player2):

		self.board = np.zeros((3,3))
		self.turn = 0
		self.players = [player1, player2]
		self.markers = [1, 2]
		self.cur_player = self.players[0]

	def get_board(self):

		return self.board

	def get_state(self):

		return ' '.join(map(str, self.board.flatten()))

	def get_player_turn(self):

		return self.players[self.turn]

	def get_possible_moves(self):

		x_ind, y_ind = np.where(self.board == 0)

		move_list = [(x, y) for x, y in zip(x_ind, y_ind)]

		return move_list 

	def is_valid_move(self, move):

		if move in self.get_possible_moves():
			return True
		else:
			print('Invalid move, try again')
		return False

	def play_turn(self, move):
		"""
		INPUTS: move, tuple containing row and col of move
		"""

		if self.is_valid_move(move):
			self.board[move[0], move[1]] = self.markers[self.turn]
			if self.turn == 0:
				self.turn = 1
				self.cur_player = self.players[self.turn]
			elif self.turn == 1:
				self.turn = 0
				self.cur_player = self.players[self.turn]


	def is_win(self):

		win_1 = np.array([1.,1.,1.])
		win_2 = np.array([2.,2.,2.])

		for i in range(3):
			if (self.board[:,i] == win_1).all() or (self.board[:,i] == win_2).all():
				return True
		for i in range(3):
			if (self.board[i,:] == win_1).all() or (self.board[i,:] == win_2).all():
				return True

		diag = np.array([self.board[0][0], self.board[1][1], self.board[2][2]])
		off_diag = np.array([self.board[2][0], self.board[1][1], self.board[0][2]])

		if (diag == win_1).all() or (diag == win_2).all():
			return True
		if (off_diag == win_1).all() or (off_diag == win_2).all():
			return True

		return False

	def is_over(self):
		if len(self.get_possible_moves()) == 0:
			return True
		return False

	def play_game(self):

		#print('INITIALIZE DA GAME\n')
		while(not self.is_win() and not self.is_over()):
			if self.cur_player.type == 'human':
				print(self.get_board())
			before = self.get_state()
			possible_moves = self.get_possible_moves()
			move_tuple = self.cur_player.pick_move(possible_moves, before)
			self.play_turn(move_tuple)
			after = self.get_state()

			if self.is_win():
				self.cur_player.update_q(before, move_tuple, after, 10) # Game over - give all the rewards
				#self.cur_player.update_q(losing_state, losing_move, winning_state, -10) # Game over - give all the rewards

			elif self.is_over():
				self.cur_player.update_q(before, move_tuple, after, -1) # Game is tie - no reward

			else:
				self.cur_player.update_q(before, move_tuple, after, 0) # Game still going - move is neutral
				losing_state = before
				losing_move = move_tuple
				winning_state = after

class Player():

	def __init__(self, name):

		self.name = name

	def pick_move(self):

		raise NotImplementedError 		

class Human(Player):

	def __init__(self, name):
		super().__init__(name)
		self.type = 'human'

	def pick_move(self, possible_moves, state):

		print("\nPlayer " + str(self.name) + ", write the row then col (e.g., '1 1')")
		move = input()
		move_tuple = (int(move.split(' ')[0]), int(move.split(' ')[1]))

		return move_tuple

	def update_q(self, state, move, new_state, r, lam=0.9):

		return

class Dumb_AI(Player):

	def __init__(self, name):
		super().__init__(name)

	def pick_move(self, possible_moves, state):
		nmoves = len(possible_moves)
		move = possible_moves[random.randrange(nmoves)]
		return move


class Smart_AI(Player):

	def __init__(self, name, game_dict={}, threshold=0.5):
		super().__init__(name)

		self.game_dict = game_dict
		self.type = 'ai'
		self.threshold = threshold

	def pick_move(self, possible_moves, state):

		if self.game_dict == {} or self.game_dict[state] == {}:
			nmoves = len(possible_moves)
			move = possible_moves[random.randrange(nmoves)]	
			return move

		else:
			best_move = max(self.game_dict[state], key=self.game_dict[state].get)
			if random.random() <self.threshold:
				move = best_move
			else:
				nmoves = len(possible_moves)
				move = possible_moves[random.randrange(nmoves)]			
			return move

	def update_q(self, state, move, new_state, r, lam=0.9):

		if state not in self.game_dict.keys():
			self.game_dict[state] = {}	
			
		if new_state not in self.game_dict.keys():
			self.game_dict[new_state] = {}		

		if self.game_dict[new_state] == {}:

			self.game_dict[state][move] = r

		else:
			self.game_dict[state][move] = r - lam * max([self.game_dict[new_state][x] for x in self.game_dict[new_state]])

	def dump_q(self, outfile='./q_table_tictactoe.pickle'):
		import pickle

		with open(outfile, 'wb') as f:
			pickle.dump(self.game_dict, f)


import pickle
ai_dict = pickle.load( open('./q_table_tictactoe.pickle', 'rb') )

p1 = Smart_AI('Josh', game_dict=ai_dict)

# for i in range(30000):
#  	t = TicTacToe(p1, p1)
#  	t.play_game()

# p1.dump_q()

#ai_dict = p1.game_dict

p1 = Smart_AI('Josh', game_dict=ai_dict, threshold=1.0)
p2 = Human('Hallacy')

t = TicTacToe(p2, p1)
t.play_game()
print(t.get_board())

