import numpy as np
import random

class TicTacToe():

	def __init__(self, player1, player2):

		self.board = np.zeros((3,3))
		self.turn = 0
		self.players = [player1, player2]
		self.markers = [1, 2]
		self.cur_player = self.players[0]

	def return_board(self):

		return self.board

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

		win_1 = np.array([1,1,1])
		win_2 = np.array([2,2,2])

		for i in range(3):
			if (self.board[:,i] == win_1).all() or (self.board[:,i] == win_2).all():
				return True
		for i in range(3):
			if (self.board[i,:] == win_1).all() or (self.board[:,i] == win_2).all():
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

		print('INITIALIZE DA GAME\n')
		while(not self.is_win() and not self.is_over()):
			print(self.return_board())
			possible_moves = self.get_possible_moves()
			move_tuple = self.cur_player.pick_move(possible_moves, self.return_board())
			self.play_turn(move_tuple)

		print('Game Over!')
		print(self.return_board())

class Player():

	def __init__(self, name):

		self.name = name

	def pick_move(self):

		raise NotImplementedError 		

class Human(Player):

	def __init__(self, name):
		super().__init__(name)

	def pick_move(self, possible_moves, state):

		print("\nPlayer " + str(self.name) + ", write the row then col (e.g., '1 1')")
		move = input()
		move_tuple = (int(move.split(' ')[0]), int(move.split(' ')[1]))

		return move_tuple

class Dumb_AI(Player):

	def __init__(self, name):
		super().__init__(name)

	def pick_move(self, possible_moves, state):
		nmoves = len(possible_moves)
		move = possible_moves[random.randrange(nmoves)]
		return move


p1 = Dumb_AI('Josh')
p2 = Dumb_AI('Hallacy')

for i in range(100):
	t = TicTacToe(p1, p2)
	t.play_game()



# print(t.return_board())
# t.play_turn((1,2))
# print(t.is_win())
# print(t.return_board())
# t.play_turn((1,1))
# print(t.is_win())
# print(t.return_board())
# t.play_turn((0,1))
# print(t.is_win())
# print(t.return_board())
# t.play_turn((2,0))
# print(t.is_win())
# print(t.return_board())
# t.play_turn((0,0))
# print(t.is_win())
# print(t.return_board())
# t.play_turn((0,2))
# print(t.is_win())
# print(t.return_board())
# t.play_turn((1,0))
# print(t.is_win())
# print(t.return_board())
# t.play_turn((2,1))
# print(t.is_win())
# print(t.return_board())
# t.play_turn((2,2))
# print(t.is_win())
# print(t.return_board())
