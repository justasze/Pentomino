import numpy

"""
Here, I write the first rotation of each piece (and their
mirror in needed), and generate the whole set with numpy.
"""

F_PIECE = [numpy.array([['0','F','F'],['F','F','0'],['0','F','0']]),
	numpy.array([['F','F','0'],['0','F','F'],['0','F','0']])]

I_PIECE = [numpy.array([['I','I','I','I','I'], ['0','0','0','0','0']])]
I_PIECE.append(numpy.rot90(I_PIECE[0]))

L_PIECE = [numpy.array([['L','L','L','L'], ['L','0','0','0']]),
	numpy.array([['L','L','L','L'], ['0','0','0','L']])]

N_PIECE = [numpy.array([['N','N','N','0'],['0','0','N','N']]),
	numpy.array([['0','0','N','N'], ['N','N','N','0']])]

P_PIECE = [numpy.array([['0','P','P'],['P','P','P']]),
	numpy.array([['P','P','0'],['P','P','P']])]

T_PIECE = [numpy.array([['T','0','0'],['T','T','T'],['T','0','0']])]

U_PIECE = [numpy.array([['U','0','U'],['U','U','U']])]

V_PIECE = [numpy.array([['V','0','0'],['V','0','0'],['V','V','V']])]

W_PIECE = [numpy.array([['0','W','W'],['W','W','0'], ['W','0','0']])]

X_PIECE = [numpy.array([['0','X','0'],['X','X','X'],['0','X','0']])]

Y_PIECE = [numpy.array([['0','Y','0','0'],['Y','Y','Y','Y']]),
	numpy.array([['0','0','Y','0'],['Y','Y','Y','Y']])]

Z_PIECE = [numpy.array([['Z','Z','0'],['0','Z','0'],['0','Z','Z']]),
	numpy.array([['0','Z','Z'],['0','Z','0'],['Z','Z','0']])]
Z_PIECE.append(numpy.rot90(Z_PIECE[0]))
Z_PIECE.append(numpy.rot90(Z_PIECE[1]))

for i in range(1, 4):
	F_PIECE.append(numpy.rot90(F_PIECE[0], i))
	F_PIECE.append(numpy.rot90(F_PIECE[1], i))
	L_PIECE.append(numpy.rot90(L_PIECE[0], i))
	L_PIECE.append(numpy.rot90(L_PIECE[1], i))
	N_PIECE.append(numpy.rot90(N_PIECE[0], i))
	N_PIECE.append(numpy.rot90(N_PIECE[1], i))
	P_PIECE.append(numpy.rot90(P_PIECE[0], i))
	P_PIECE.append(numpy.rot90(P_PIECE[1], i))
	T_PIECE.append(numpy.rot90(T_PIECE[0], i))
	U_PIECE.append(numpy.rot90(U_PIECE[0], i))
	V_PIECE.append(numpy.rot90(V_PIECE[0], i))
	W_PIECE.append(numpy.rot90(W_PIECE[0], i))
	Y_PIECE.append(numpy.rot90(Y_PIECE[0], i))
	Y_PIECE.append(numpy.rot90(Y_PIECE[1], i))

PIECES = {
	'F': F_PIECE,
	'I': I_PIECE,
	'L': L_PIECE,
	'N': N_PIECE,
	'P': P_PIECE,
	'T': T_PIECE,
	'U': U_PIECE,
	'V': V_PIECE,
	'W': W_PIECE,
	'X': X_PIECE,
	'Y': Y_PIECE,
	'Z': Z_PIECE
}
