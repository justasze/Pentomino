#include "pentomino.h"

static void	*safe_alloc(size_t n)
{
	void	*ret = malloc(n);
	if (ret == NULL)
	{
		dprintf(2, "Error: Couldn't allocate memory\n");
		exit(EXIT_FAILURE);
	}
	return ret;
}

static int get_rotations(t_piece *piece, char c)
{
	switch (c)
	{
		case 'F':
			piece->rotations = (char**)F_ROTATIONS;
			piece->nb_rotations = COUNT_OF(F_ROTATIONS);
			return 1;
		case 'I':
			piece->rotations = (char**)I_ROTATIONS;
			piece->nb_rotations = COUNT_OF(I_ROTATIONS);
			return 1;
		case 'L':
			piece->rotations = (char**)L_ROTATIONS;
			piece->nb_rotations = COUNT_OF(L_ROTATIONS);
			return 1;
		case 'N':
			piece->rotations = (char**)N_ROTATIONS;
			piece->nb_rotations = COUNT_OF(N_ROTATIONS);
			return 1;
		case 'P':
			piece->rotations = (char**)P_ROTATIONS;
			piece->nb_rotations = COUNT_OF(P_ROTATIONS);
			return 1;
		case 'T':
			piece->rotations = (char**)T_ROTATIONS;
			piece->nb_rotations = COUNT_OF(T_ROTATIONS);
			return 1;
		case 'U':
			piece->rotations = (char**)U_ROTATIONS;
			piece->nb_rotations = COUNT_OF(U_ROTATIONS);
			return 1;
		case 'V':
			piece->rotations = (char**)V_ROTATIONS;
			piece->nb_rotations = COUNT_OF(V_ROTATIONS);
			return 1;
		case 'W':
			piece->rotations = (char**)W_ROTATIONS;
			piece->nb_rotations = COUNT_OF(W_ROTATIONS);
			return 1;
		case 'X':
			piece->rotations = (char**)X_ROTATIONS;
			piece->nb_rotations = COUNT_OF(X_ROTATIONS);
			return 1;
		case 'Y':
			piece->rotations = (char**)Y_ROTATIONS;
			piece->nb_rotations = COUNT_OF(Y_ROTATIONS);
			return 1;
		case 'Z':
			piece->rotations = (char**)Z_ROTATIONS;
			piece->nb_rotations = COUNT_OF(Z_ROTATIONS);
			return 1;
		default:
			return 0;
	}
}

static t_piece *get_pieces(size_t nb_pieces, char *av)
{
	t_piece *pieces = safe_alloc(sizeof(t_piece) * nb_pieces);

	for(size_t i = 0; i < nb_pieces; i++)
	{
		if (get_rotations(&pieces[i], av[i]) == 0)
		{
			dprintf(2, "Error: invalid piece found. Valid pieces are FILNPTUVWXYZ.\n");
			free(pieces);
			exit(EXIT_FAILURE);
		}
	}
	return pieces;
}

static char **get_board(size_t nb_pieces)
{
	char **board = safe_alloc(sizeof(char*) * 5);

	for(size_t i = 0; i < 5; i++)
	{
		board[i] = safe_alloc(nb_pieces + 1);
		memset(board[i], '0', nb_pieces);
		board[i][nb_pieces] = '\0';
	}
	return board;
}

static void print_board(char **board)
{
	for (size_t i = 0; i < 5; i++)
		printf("%s\n", board[i]);
}

static int can_be_placed(char **piece, char **board, size_t x, size_t y, size_t board_size)
{
	size_t	part = 0;

	for (size_t i = 0; i < 5; i++)
		for (size_t j = 0; j < 5; j++)
		{
			if (piece[i][j] != '0')
			{
				if (x + i >= 5 || y + j >= board_size
						|| board[x + i][y + j] != '0')
					return 0;
				part++;
				if(part == 5)
					return 1;
			}
		}
	return 1;
}

static void fill_board(char **piece, char **board, size_t x, size_t y, int place)
{
	size_t part = 0;

	for(size_t i = 0; i < 5; i++)
		for (size_t j = 0; j < 5; j++)
		{
			if (piece[i][j] != '0')
			{
				board[x + i][y + j] = place ? piece[i][j] : '0';
				part++;
			}
			if (part == 5)
				return;
		}
}

static int solve(t_piece *pieces, size_t current, char **board, size_t nb_pieces)
{
	char **rotation;

	for(size_t i = 0; i < pieces[current].nb_rotations; i++)
	{
		rotation = &pieces[current].rotations[i * 5];
		for (size_t x = 0; x < 5; x++)
		{
			for (size_t y = 0; y < nb_pieces; y++)
			{
				if (can_be_placed(rotation, board, x, y, nb_pieces))
				{
					fill_board(rotation, board, x, y, 1);
					if (current == nb_pieces - 1)
						return 1;
					else if (solve(pieces, current + 1, board, nb_pieces))
						return 1;
					else
						fill_board(rotation, board, x, y, 0);
				}
			}
		}
	}
	return 0;
}

static void	free_resources(t_piece *pieces, char **board)
{
	for(size_t i = 0; i < 5; i++)
		free(board[i]);
	free(board);
	free(pieces);
}

int main(int ac, char **av)
{
	t_piece *pieces = NULL;
	char	**board = NULL;
	size_t nb_pieces;

	if (ac != 2)
	{
		dprintf(2, "Usage: %s <pieces>\n", av[0]);
		return EXIT_FAILURE;
	}
	nb_pieces = strlen(av[1]);
	pieces = get_pieces(nb_pieces, av[1]);
	board = get_board(nb_pieces);
	if (solve(pieces, 0, board, nb_pieces))
		print_board(board);
	else
		printf("This setup seems impossible...\n");
	free_resources(pieces, board);
	return EXIT_SUCCESS;
}
