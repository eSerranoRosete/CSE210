def main():

    def has_winner(player):
        if (board[0] == player and board[1] == player and board[2] == player):
            return True
        elif (board[3] == player and board[4] == player and board[5] == player):
            return True
        elif (board[6] == player and board[7] == player and board[8] == player):
            return True
        elif (board[0] == player and board[3] == player and board[6] == player):
            return True
        elif (board[2] == player and board[4] == player and board[7] == player):
            return True
        elif (board[3] == player and board[5] == player and board[8] == player):
            return True
        elif (board[0] == player and board[4] == player and board[8] == player):
            return True
        elif (board[2] == player and board[4] == player and board[6] == player):
            return True
        else: 
            return False

    board = []

    for i in range(10):
        board.append(i)

    board.pop(0)

    def draw_board():
        print()
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("-----------")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("-----------")
        print(f"{board[6]} | {board[7]} | {board[8]}")
        print()

    player = "x"
    game_end = False

    draw_board()

    while not game_end:

        prompt = input(f"It's player's {player} turn: ")
        board[int(prompt) - 1] = player

        draw_board()

        if has_winner(player):
            print(f"Player {player} has won the game! :)")
            game_end = True
        else: 
            if (player == "x"):
                player = "o"
            else:
                player = "x"


if __name__ == "__main__":
    main()