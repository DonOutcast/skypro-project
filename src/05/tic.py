class Tic_tac_toe:
    """Class game Tic Tac Toe"""

    def __init__(self, board=" " * 9):
        self.board = [char if char in "XO" else " " for char in board]


    def __repr__(self):
        return ("-" * 9) + "\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n".format(*self.board) + ("-" * 9)


    def play(self):
        print(self)
        move = "X"
        cond = 0
        while cond != 1:
            if self.board.count("X") > self.board.count("O"):
                move = "O"
            else:
                move = 'X'
            try:
                coords = input("Enter cordinations from 1 to 3!: ").split()
                index = (int(coords[0]) - 1) * 3 + int(coords[1]) - 1
                if coords[0] not in "123" or coords[1] not in "123":
                    print("Coordinates should be from 1 to 3!")
                elif self.board[index] != " ":
                    print("This cell is occupied! Choose another one!")
                else:
                    self.board[index] = move
                    print(self)
                    cond = self.check_win(move)
            except ValueError:
                print("You should enter numbers!")


    def check_win(self, move):
        b = self.board
        a = 0
        possible_wins = [b[0] + b[1] + b[2], b[3] + b[4] + b[5], b[6] + b[7] + b[8],
                     b[0] + b[3] + b[6], b[1] + b[4] + b[7], b[2] + b[5] + b[8],
                     b[0] + b[4] + b[8], b[2] + b[4] + b[6]]
        if move * 3 in possible_wins:
            print(move, "wins")
            a = 1
            return a
        elif " " not in b:
            print("Draw")
            a = 1
            return a

if __name__ == "__main__":
    ttt = Tic_tac_toe()
    # ttt.play()
    print(ttt.__str__)
