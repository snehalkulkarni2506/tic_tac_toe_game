board=["-","-","-",
       "-","-","-",
       "-","-","-"]
current_player="X"
continue_game=True
winner=0
choice=""
def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


#Assigning position on board
def handle_turn():
    global current_player
    position=int(input("Choose Random Position between 0 to 8"))
    board[position]=current_player


#Next player turn
def swap_player():
    global current_player
    if current_player=="X":
        current_player="O"
    else:
        current_player="X"


def check_winner():
    global winner
    row=check_rows()
    column=check_cols()
    daigonal=check_daig()

    if row:
        winner=row
    elif column:
        winner=column
    elif daigonal:
        winner=daigonal


#Checking Winner in Rows
def check_rows():
    global continue_game
    row1=board[0] == board[1] == board[2] != "-" # checking if all element in row1 is same
    row2=board[3] == board[4] == board[5] != "-" # checking if all element in row2 is same
    row3=board[6] == board[7] == board[8] != "-" # checking if all element in row3 is same

    if row1 or row2 or row3:
        continue_game=False

    if row1:
        return board[0]     #if element in row1 is same than it will return any value between 0,1,2
    elif row2:
        return board[3]     #if element in row2 is same than it will return any value between 3,4,5
    elif row3:
        return board[6]     #if element in row1 is same than it will return any value between 6,7,8


#Checking Winner in Column
def check_cols():
    global continue_game
    col1=board[0] == board[3] == board[6] != "-" # checking if all element in col1 is same i.e X or O
    col2=board[1] == board[4] == board[7] != "-" # checking if all element in col2 is same i.e X or O
    col3=board[2] == board[5] == board[8] != "-" # checking if all element in col3 is same i.e X or O

    if col1 or col2 or col3:
        continue_game=False

    if col1:
        return board[0]     #if element in col1 is same than it will return any value between 0,3,6
    elif col2:
        return board[4]     #if element in col2 is same than it will return any value between 1,4,7
    elif col3:
        return board[8]     #if element in col3 is same than it will return any value between 2,5,8


#Checking Winner at Daigonals
def check_daig():
    global continue_game
    daig1=board[0] == board[4] == board[8] != "-" # checking if all element in daigonal1 is same i.e X or O
    daig2=board[2] == board[4] == board[6] != "-" # checking if all element in daigonal2 is same i.e X or O

    if daig1 or daig2:
        continue_game=False

    if daig1:
        return board[0]     #if element in col1 is same than it will return any value between 0,4,8
    elif daig2:
        return board[4]     #if element in col2 is same than it will return any value between 2,4,6



#Checking whether match is tie or not
def check_tie():
    global continue_game
    if "-" not in board:
        continue_game=False
        display_board()
        print("Match is tie")


#Displaying the winner
def win():
    if winner=="X":
        display_board()
        print("X is Winner")
    elif winner=="O":
        display_board()
        print("O is Winner")

def play():
    while continue_game:
        display_board()
        handle_turn()
        swap_player()
        check_winner()
        check_tie()
        win()


play()
