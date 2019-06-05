# Create a Tic Tac Toe game. -- Test script --
#Here are the requirements:

    #2 players should be able to play the game (both sitting at the same computer)
    #The board should be printed out every time a player makes a move
    #You should be able to accept input of the player position and then place a symbol on the board



#Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(" ----- ")
    print(f'|{board[1]}|{board[2]}|{board[3]}|')
    print("|-----|")
    print(f'|{board[4]}|{board[5]}|{board[6]}|')
    print("|-----|")
    print(f'|{board[7]}|{board[8]}|{board[9]}|')
    print(" ----- ")

# TEST Step 1: run your function on a test version of the board list, and make adjustments as necessary
test_board = ['#',' ',' ',' ','O','X','O','X','O','X']
display_board(test_board)


# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():
    marker = "A"
    while marker is not "X" or "O":
        marker = (input('Player 1, choose your marker: X or O ')).upper()
        if marker == "X":
            return ('X', 'O')
        else:
            return ('O', 'X')


# TEST Step 2: run the function to make sure it returns the desired output
player_input()


# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker

# TEST Step 3: run the place marker function using test parameters and display the modified board
place_marker(test_board,'$',8)
display_board(test_board)


# Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.

def win_check(board, mark):
    #check rows
    return ((mark == board[1] and mark == board[2] and mark == board[3]) or
    (mark == board[4] and mark == board[5] and mark == board[6]) or
    (mark == board[7] and mark == board[8] and mark == board[9]) or
    #check columns
    (mark == board[1] and mark == board[4] and mark == board[7]) or
    (mark == board[2] and mark == board[5] and mark == board[8]) or
    (mark == board[3] and mark == board[6] and mark == board[9]) or
    #check diagonals
    (mark == board[1] and mark == board[5] and mark == board[9]) or
    (mark == board[3] and mark == board[5] and mark == board[7]))

# TEST Step 4: run the win_check function against our test_board - it should return True

win_check(test_board,'X')


# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

from random import randint

def choose_first():
    first = randint(1,2)
    if first == 1:
        return 'Player 1'
    else:
        return 'Player 2'

# TEST Step 5

choose_first()


#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '

# TEST Step 6

space_check(test_board, 2)


# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for position in range(1,10):
        if space_check(board, position):
            return False
    return True

# TEST Step 7

full_board_check(test_board)


# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Where do you place your marker? 1-9'))
    return position


# TEST Step 8

player_choice(test_board)


# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    answer = 'maybe'
    while answer not in ['y', 'n']:
        answer = str(input('Do you want to play again? y or n?'))
    return answer == 'y'


# TEST Step 9

replay()
