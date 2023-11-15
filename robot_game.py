import random
import time

board_x_size = 10
board_y_size = 7
game = [[0] * board_x_size for i in range(board_y_size)]
position = [0, 0] # robot position
final_position = [board_y_size - 1, board_x_size - 1]
count_of_mines = 15

random_y = [random.randint(0, board_y_size - 1) for _ in range(count_of_mines)]
random_x = [random.randint(0, board_x_size - 1) for _ in range(count_of_mines)]

for i in range(count_of_mines):
	# don't add mine on the final position
	if final_position == [random_y[i], random_x[i]]:
		continue
	else:
		# add mine
		game[random_y[i]][random_x[i]] = 1

# manual add one mine
# game[0][0] = 1 <- mine!!!!

def show_game():
	board = []
	for y in range(board_y_size):
		board.append("\r\n")
		for x in range(board_x_size):
			if final_position == [y, x]:
				# FINAL POSITION
				board.append("_F_|")
			elif game[y][x] == 0:
				if position == [y, x]:
					# robot only
					board.append("_R_|")
				else:
					# no mine, no robot
					board.append("___|")
			else:
				if position == [y, x]:
					# robot is dead
					board.append("_X_|")
				else:
					# mine
					board.append("_M_|")
	print("".join(board))

def main():
	aval_action = ['r', 'l', 'u', 'd']
	act_to_coordinate = {'r' : (0, 1), 'l' : (0, -1), 'u' : (-1, 0), 'd' : (1, 0)}
	while True:
		show_game()
		if game[position[0]][position[1]] == 1:
			print("Game over")
			return
		if final_position == position:
			print("Game finished. You won")
			return

		#break
		action = input('Введи ход (r, l, u, d)')
		if action not in aval_action:
			print('ты писька')
			continue
		coor = act_to_coordinate[action]
		position[0] += coor[0]
		position[1] += coor[1]

		# show user action
		# apply action
		# check if we collide with mine


if __name__ == "__main__":
	main()
