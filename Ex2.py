

def is_win(board):
    #looking for all the possible win lines to see if the line spots is the same sign and not '?'

    for row in range(3):
        #horizontal
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '?':
            return True, board[row][0]

    for col in range(3):
        #vertical
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '?':
            return True, board[0][col]

    #diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '?':
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '?':
        return True, board[0][2]

    #no win
    return False, None

def play_turn(turn, row, col, board):
    #changing the '?' sign to X if the turn number is odd and O if even
    sign = "X" if turn % 2 != 0 else "O"
    board[row][col] = sign
    return

def is_free(user, free_places):
    #checks for a '?' in the player choice location
    if user in free_places:
        free_places.remove(user)
        return True
    else:
        return False

def print_board(board):
    #printing every row in a 3X3 matricx
    for i in range(3):
        print(f" {board[i][0]} {board[i][1]} {board[i][2]} ")

def location(choice):
    #set location of the board
    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    return mapping[choice]

def game():
    board = [['?', '?', '?'], ['?', '?', '?'], ['?', '?', '?']]
    free_places = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("******** Tik-Tak-Tok Game ********")
    turn = 1

    while turn <= 9:

        print_board(board)
        print("Free Places is: " , *free_places)

        while True:
            try:
                user_play = int(input("Choose a place: "))
                if is_free(user_play, free_places):
                    break
                else:
                    print("Invalid Input Try Again!")
                    print("Free Places is: ", *free_places)
            except ValueError:
                print("Please enter a valid number between 1 and 9!")

        row, col = location(user_play)
        play_turn(turn, row, col, board)

        if turn >= 5:
            #win check since the 5th turn (the first winning spot)
            win, sign = is_win(board)
            if win:
                #we found a win for one of the players
                print_board(board)
                if sign == "X":
                    player = 'First'
                else:
                    player = 'Second'
                print(f"{player} player Win")
                break
        if turn == 9:
            #is we got here the bord is full and no win was detected
            print("Tie")
            break
        turn += 1
    return



if __name__ == "__main__":
    while True:
        play = input("Wanna play Tik-Tak-Tok? (Y/N): ").strip().lower()

        if play == 'y':
            game()
        elif play == 'n':
            print('Bye')
            break
        else:
            print("Invalid input try again")

