# Create a Tic Tac Toe game.
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


# Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while loops to continually ask until you get a correct answer.

def player_input():
    marker = "A"
    while marker is not "X" or "O":
        marker = (input('Player 1, choose your marker: X or O ')).upper()
        if marker == "X":
            return ('X', 'O')
        else:
            return ('O', 'X')



# Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker


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


# Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.

from random import randint

def choose_first():
    first = randint(1,2)
    if first == 1:
        return 'Player 1'
    else:
        return 'Player 2'


#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    return board[position] == ' '


# Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for position in range(1,10):
        if space_check(board, position):
            return False
    return True


# Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Where do you place your marker? 1-9'))
    return position


# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    answer = 'maybe'
    while answer not in ['y', 'n']:
        answer = str(input('Do you want to play again? y or n?'))
    return answer == 'y'


# Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!

print('Welcome to Tic Tac Toe!')

while True:
    #set up the board to 10 empty strings
    play_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    #tuple containing marker player1,player2 X,O or O,X
    player1_marker, player2_marker = player_input()

    # string 'Player 1' or 'Player 2'
    turn = choose_first()
    print(turn + ' will play first')

    #check if players are ready
    ready = input('are you ready to play? y or n?')
    if ready == 'y':
        game_on = True
    else:
        game_on = False

    # establish who starts
    if turn == 'Player 1':
        play = 1
    else:
        play = 2


    # while loop for the game
    while game_on:
        display_board(play_board)

        # check if win
        if win_check(play_board,'X'):
            print('X has won')
            break
        if win_check(play_board,'O'):
            print('O has won')
            break
        # check if board full
        if full_board_check(play_board):
            print("It's a tie!")
            break

        # if no win and board not full, play.
        else:

            # for first turn, play is etablished as 1 if player 1 starts or as 2 for player 2
            if play % 2 != 0:
                #player 1 turn
                print("player 1's turn")
                position = player_choice(play_board)
                place_marker(play_board, player1_marker,position)
                # add 1 to play so it becomes even
                play += 1

            elif play % 2 == 0:
                #player 2 turn
                print("player 2's turn")
                position = player_choice(play_board)
                place_marker(play_board,player2_marker,position)
                # add 1 to play so it becomes odd
                play += 1


    #once while loop for the game breaks, ask to play again.
    if not replay():
        break
