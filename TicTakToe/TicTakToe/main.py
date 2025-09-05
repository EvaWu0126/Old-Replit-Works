from colorama import Fore, Back, Style

def isWinner(board, symbol):
    #horizontally
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == symbol:
        return True
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == symbol:
        return True
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == symbol:
        return True

    #vertically
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == symbol:
        return True
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == symbol:
        return True
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == symbol:
        return True

    #diagonal
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == symbol:
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == symbol:
        return True


def tic_tac_toe():
    board= [
        [0, 0, 0],
        [0, 0, 0],
        [0 ,0 ,0]
    ]
    symbol = -1    # "-1" is for x
    turn = 0
    winner = ""    # no current winner
    print_board(board)

    while winner == "" and turn < 9:

        # set the symbol to -1 for x or 1 for 0
        if turn % 2 == 0:
            symbol = -1
        else:
            symbol = 1

        row, col = get_move(board, symbol)
        # put the symbol into row & col on the board, you can set the top left corner to -1 by doing board[0][0] = -1
        if symbol == -1:
            board[row][col] = -1
        elif symbol == 1:
            board[row][col] = 1

        if isWinner(board, symbol):
            # TODO: if there's a winner,set it to be "x" or "o" based on the current symbol
            if symbol == -1:
                winner = "X"
            elif symbol == 1:
                winner = "O"

        # print out the board
        print_board(board)

        # advance the turn by 1
        turn = turn + 1

    # TODO: after the loop, print if there was a winner, or if there was a draw. Say who won if there was a winner
    if isWinner(board, symbol) != True:
        print("Draw!")
    else:
        print(winner + " won! ")



# hint is to do the error checking in here. you have the board state passed in so you can check what they type
# for row and col and make them do it again before returning values that are ok
def get_move(board,symbol):
    if symbol == -1:
        print(Fore.RED + "It is X's turn." +Style.RESET_ALL,)
    elif symbol == 1:
        print(Fore.BLUE + "It is O's turn." +Style.RESET_ALL)
    row = int(input("Please enter the row: "))
    col = int(input("Please enter the col: "))
    while board[row][col] != 0:
        print("This is invalid placement. Please redo.")
        row = int(input("Please enter the row: "))
        col = int(input("Please enter the col: "))


    return (row, col)


def print_board(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                print(" ", end = "")
            elif board[row][col] == -1:
                print(Fore.RED + "X" +Style.RESET_ALL, end = "")
            elif board[row][col] == 1:
                print(Fore.BLUE + "O" +Style.RESET_ALL, end = "")

            if col != 2:
                print("|", end="")
        if row != 2:
            print("\n-----")
    print()


tic_tac_toe()