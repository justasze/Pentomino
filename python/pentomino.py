#!/bin/python

import sys
from typing import List
from pieces import PIECES

def get_pieces() -> List:
	"""
	PIECES is a dict associating to each piece the list of its permutations.
	"""
	pieces = []

	if len(sys.argv) != 2:
		print("Usage: {} <pieces>".format(sys.argv[0]), file=sys.stderr)
		exit(1)

	for c in sys.argv[1]:
		piece = PIECES.get(c)
		if piece is None:
			print("Error: invalid piece found. Valid pieces are FILNPTUVWXYZ.", file=sys.stderr)
			exit(1)
		pieces.append(piece)
	return pieces

def print_board(board) -> None:
	for y in board:
		for x in y:
			print(x, end='')
		print('')

def can_be_placed(piece, board, y, x) -> bool:
	try:
		for i in range(len(piece)):
			for j in range(len(piece[i])):
				if piece[i][j] != '0' and board[y + i][x + j] != '0':
					return False
	except IndexError:
		return False
	return True

def fill_board(piece, board, y, x, place) -> None:
	"""
	This function both places and removes pieces.
	"""
	for i in range(len(piece)):
		for j in range(len(piece[i])):
			if piece[i][j] != '0':
				board[y + i][x + j] = piece[i][j] if place else '0'

def solve(pieces, current, board) -> bool:
	"""
	This is a simple backtracking. For loops are slow in python, but I think
	this is the simplest implementation.
	Each piece is placed wherever possible, and calls for the next one.
	If all pieces are placed, this is good. Else, pieces are removed and
	another position / piece rotation is tried.
	"""
	rotations = pieces[current]
	for piece in rotations:
		for y in range(len(board)):
			for x in range(len(board[y])):
				if can_be_placed(piece, board, y, x):
					fill_board(piece, board, y, x, True)
					if current == len(pieces) - 1:
						return True
					elif solve(pieces, current + 1, board) is True:
						return True
					else:
						fill_board(piece, board, y, x, False)
	return False

def main() -> None:
	"""
	The pentomino setup is a grid of size 5xN with n the number of pieces.
	"""
	pieces = get_pieces()
	board = [['0' for i in range(len(sys.argv[1]))] for i in range(5)]

	if solve(pieces, 0, board) is True:
		print_board(board)
	else:
		print('This setup seems impossible...')

if __name__ == "__main__":
	main()
