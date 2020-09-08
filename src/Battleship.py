from random import randint

#Generating the game board (5 x 5 grid)
board = [] 
for x in range(5):
    board.append(["O"] * 5)

#Printing the board
def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)

#Random row for battleship
def random_row(board):
    return randint(0, len(board) - 1)

#Random column for battleship
def random_col(board):
    return randint(0, len(board[0]) - 1)

#Assigning coordinates for the ship
ship_row = random_row(board)
ship_col = random_col(board)

#Printing battleship location for testing purposes
print (ship_row)
print (ship_col)

#Getting player guesses and letting them know what turn they're on. 4 guesses are allowed
for turn in range(4):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    #Checks if player's guess matches the ship location
    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): #Guess not on grid
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"): #Repeated guess
            print ("You guessed that one already.")
        else: #Valid incorrect guess
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            
        #Incrementing turn 
        turn +1
        print_board(board)
        if turn == 3:
            print ("Game Over")

