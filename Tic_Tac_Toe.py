#-----------TicTacToe-----------

board = ["_", "_", "_",
         "_", "_", "_", 
         "_", "_", "_"]

game_still_going = True

winner = None

current_player = "X"

def display_board():
    print(board[0]+"|" +board[1]+"|"+ board[2]+"|")
    print(board[3]+"|" +board[4]+"|"+ board[5]+"|")
    print(board[6]+"|" +board[7]+"|" +board[8]+"|")

def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_gameover()

        flip_player()
    if winner == "X" or winner == "O":
        print(winner +" won!")
    else:
        print("Game Tied")


def handle_turn(player):
    print(current_player +"'s turn")
    position = input("Choose a number between 1 and 9: ")
    valid = False

    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a number between 1 and 9: ")
        
        position = int(position) - 1
        if board[position]=="_":
            valid = True
        else:
            print("You cannot overwrite")

    board[position] = player
    display_board()
        
    
def check_if_gameover():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_rows():
    global game_still_going
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"
    if row1 or row2 or row3:
        game_still_going = False
       
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    

def check_columns():
    global game_still_going
    column1 = board[0] == board[3] == board[6] != "_"
    column2 = board[1] == board[4] == board[7] != "_"
    column3 = board[2] == board[5] == board[8] != "_"
    if column1 or column2 or column3:
        game_still_going = False
       
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    


def check_diagonals():
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != "_"
    diagonal2 = board[2] == board[4] == board[6] != "_"

    if diagonal1 or diagonal2:
        game_still_going = False
       
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    

play_game()