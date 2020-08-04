import numpy as np

class TicTacToe():

	def __init__(self):

		self.board = np.zeros((3,3))
		self.cur_player = 1

	def return_board(self):

		return self.board

	def get_player_turn(self):

		return self.cur_player

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
			self.board[move[0], move[1]] = self.cur_player
			if self.cur_player == 1:
				self.cur_player = 2
			elif self.cur_player == 2:
				self.cur_player = 1

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
		if self.get_possible_moves() is None:
			return True
		return False

	def interface(self):

		print('INITIALIZE DA GAME\n')
		while(not self.is_win() or self.is_over()):
			print(self.return_board())
			print("\nPlayer " + str(self.cur_player) + ", write the row then col (e.g., '1 1')")
			move = input()
			move_tuple = (int(move.split(' ')[0]), int(move.split(' ')[1]))
			self.play_turn(move_tuple)

		print('Game Over!')


t = TicTacToe()
t.interface()

#print(t.return_board())
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
