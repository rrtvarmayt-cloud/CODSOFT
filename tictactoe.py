board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):

    win_conditions = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == player and \
           board[condition[1]] == player and \
           board[condition[2]] == player:
            return True

    return False

def check_draw():
    return " " not in board

def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if check_draw():
        return 0

    if is_maximizing:

        best_score = -100

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                if score > best_score:
                    best_score = score

        return best_score

    else:

        best_score = 100

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                if score < best_score:
                    best_score = score

        return best_score

def ai_move():

    best_score = -100
    best_move = 0

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

print("Welcome to Tic-Tac-Toe AI!")

while True:

    print_board()

    position = int(input("Choose position (1-9): "))

    if position < 1 or position > 9:
        print("Invalid position!")
        continue

    if board[position - 1] != " ":
        print("Position already taken!")
        continue

    board[position - 1] = "X"

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if check_draw():
        print_board()
        print("It's a draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break

    if check_draw():
        print_board()
        print("It's a draw!")
        break