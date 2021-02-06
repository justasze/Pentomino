NAME = pentomino

FLAGS = -Wall -Wextra -Werror -Weverything -Ofast

SRC = pentomino.c

OBJS_NAME = $(SRC:.c=.o)

OBJS_PATH = objs/

OBJS = $(addprefix $(OBJS_PATH), $(OBJS_NAME))

all: $(OBJS_PATH) $(NAME)

$(NAME): $(OBJS)
	clang $(FLAGS) -o $(NAME) $(OBJS) 

$(OBJS_PATH):
	mkdir -p $(OBJS_PATH)

$(OBJS_PATH)%.o: $(SRCS_PATH)%.c
	clang $(FLAGS) -o $@ -c $< $(INCLUDES_PATH)

clean:
	rm -rf $(OBJS_PATH)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: clean fclean re
