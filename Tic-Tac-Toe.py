#Tic Tac Toe

#create a 3x3 list of blank spaces
def new_board():
	board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
	return board

#print the current board to the user
def print_board(board):
	print("", board[0][0], "|", board[0][1], "|", board[0][2])
	print("---+---+---")
	print("", board[1][0], "|", board[1][1], "|", board[1][2])
	print("---+---+---")
	print("", board[2][0], "|", board[2][1], "|", board[2][2])
	
#take the user input and return an X or O depending on who's turn it is
def next_turn(turn):
	if (turn % 2) == 0:
		print("X's turn!")
	elif (turn % 2) == 1:
		print("O's turn!")	
	move = input("Enter your move: ")
	print()
	if turn%2 == 0:
		return ("X", move)
	else:
		return ("O", move)
		
#make sure the user input a valid entry and the space is not already taken		
def check_move(move, board):
	if move[1] == 'a1':
		if board[0][0] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	elif move[1] == 'a2':
		if board[0][1] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	elif move[1] == 'a3':
		if board[0][2] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	elif move[1] == 'b1':
		if board[1][0] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	elif move[1] == 'b2':
		if board[1][1] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	elif move[1] == 'b3':
		if board[1][2] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	elif move[1] == 'c1':
		if board[2][0] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	elif move[1] == 'c2':
		if board[2][1] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	elif move[1] == 'c3':
		if board[2][2] == " ":
			return True
		else:
			print("That spot is already taken!")
			print()
			return False
	else:
		print("That is not a valid entry!")
		print()
		return False
		
#takes the current board and the user's move as parameters and updates the board with the new move		
def update_board(board, player_move):
	if player_move[1] == 'a1':
		board[0][0] = player_move[0]
	elif player_move[1] == 'a2':
		board[0][1] = player_move[0]
	elif player_move[1] == 'a3':
		board[0][2] = player_move[0]
	elif player_move[1] == 'b1':
		board[1][0] = player_move[0]
	elif player_move[1] == 'b2':
		board[1][1] = player_move[0]
	elif player_move[1] == 'b3':
		board[1][2] = player_move[0]
	elif player_move[1] == 'c1':
		board[2][0] = player_move[0]
	elif player_move[1] == 'c2':
		board[2][1] = player_move[0]
	elif player_move[1] == 'c3':
		board[2][2] = player_move[0]
	
#checks to see if there is a 'tic tac toe' condition on the board	
def check_win(board):
	if (board[0][0] == board[0][1]) and (board[0][1] == board[0][2]) and (board[0][0] != " "):
		return True
	elif (board[1][0] == board[1][1]) and (board[1][1] == board[1][2]) and (board[1][0] != " "):
		return True
	elif (board[2][0] == board[2][1]) and (board[2][1] == board[2][2]) and (board[2][0] != " "):
		return True
	elif (board[0][0] == board[1][0]) and (board[1][0] == board[2][0]) and (board[0][0] != " "):
		return True
	elif (board[0][1] == board[1][1]) and (board[1][1] == board[2][1]) and (board[0][1] != " "):
		return True
	elif (board[0][2] == board[1][2]) and (board[1][2] == board[2][2]) and (board[0][2] != " "):
		return True
	elif (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[0][0] != " "):
		return True
	elif (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[0][2] != " "):
		return True
	else:
		return False

#Program Initializes
turn = 0 #initialize the number of turns taken
win = False #initialize win condition
board = new_board() #create the new tic tac toe board

print('Welcome to Tic Tac Toe!')
print("Enter a1 - c3 to choose a space (a1 = top left corner)")
print()

print_board(board)

#Main loop
while (win == False) and turn < 9: #loop runs while no one has won and the board isn't full
	print()
	while True:
		player = (turn % 2) + 1 #keeps track of who's turn it is (player 1 or 2)
		player_move = next_turn(turn)
		if check_move(player_move, board) == True: #loop that runs until user enters a valid move
			break
	update_board(board, player_move)
	print_board(board)
	win = check_win(board)
	turn += 1 #update what turn number it is
	
if win == True: #check to see if someone won, or if it was a cat's game
	print()
	print(f'Player {player} wins! Game over!')
else:
	print()
	print("Cat's game! Game Over!")
	
