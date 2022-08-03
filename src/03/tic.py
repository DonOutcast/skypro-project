user_input = input()

def convert_to_list(stroka: str) -> list:
    """This function coverting your string to list"""
    spisok = []
    spisok_a = ''
    spisok_b = ''
    spisok_c = ''
    spisok_a = user_input[0:3]
    # if user_input[0:1] == 'X' and user_input[1:2] == 'X' and user_input[2:3] == "X":
    #     print("win")
    # elif user_input[0:1] == "X" and user_input[4:5] == "X" and user_input[8:9] == "X":
    #     print("Maan")
    # elif user_input[0:1] == "X" and user_input[3:4] == "X" and user_input[6:7] == "X":
    #     print("EE")
    # elif user_input[]
    spisok_b = user_input[3:6]
    spisok_c = user_input[6:9]
    spisok.append(spisok_a)
    spisok.append(spisok_b)
    spisok.append(spisok_c)
    return spisok


def print_grid(spisok: list) -> None:
    """This function print to console grid """
    print("---------")
    for rows in spisok:
        print("| ", " ".join(words for words in rows), " |")
    print("---------")

def o_wins(spisok: list) -> None:
    if spisok[0][0:1] == 'O' and spisok[0][1:2] == "O" and spisok[0][2:3] == "O":
        print("O wins")
    elif spisok[1][0:1] == 'O' and spisok[1][1:2] == "O" and spisok[1][2:3] == "O":
        print("O wins")
    elif spisok[2][0:1] == 'O' and spisok[2][1:2] == 'O' and spisok[2][2:3] == "O":
        print("O wins")
    elif spisok[0][0:1] == 'O' and spisok[1][1:2] == 'O' and spisok[2][2:3] == 'O':
        print("O wins")
    elif spisok[0][2:3] == 'O' and spisok[1][1:2] == 'O' and spisok[2][0:1] == 'O':
        print("O wins")
    elif spisok[0][0:1] == 'O' and spisok[1][0:1] == 'O' and spisok[2][0:1] == 'O':
        print("O wins")
    elif spisok[0][1:2] == "O" and spisok[1][1:2] == 'O' and spisok[2][1:2] == 'O':
        print("O wins")
    elif spisok[0][2:3] == 'O' and spisok[1][2:3] == 'O' and spisok[2][2:3] == 'O':
        print("O wins")


def x_wins(spisok: list) -> None:
    if spisok[0][0:1] == 'X' and spisok[0][1:2] == "X" and spisok[0][2:3] == "X":
        print("X wins")
    elif spisok[1][0:1] == 'X' and spisok[1][1:2] == "X" and spisok[1][2:3] == "X":
        print("X wins")
    elif spisok[2][0:1] == 'X' and spisok[2][1:2] == 'X' and spisok[2][2:3] == "X":
        print("X wins")
    elif spisok[0][0:1] == 'X' and spisok[1][1:2] == 'X' and spisok[2][2:3] == 'X':
        print("X wins")
    elif spisok[0][2:3] == 'X' and spisok[1][1:2] == 'X' and spisok[2][0:1] == 'X':
        print("X wins")
    elif spisok[0][0:1] == 'X' and spisok[1][0:1] == 'X' and spisok[2][0:1] == 'X':
        print("X wins")
    elif spisok[0][1:2] == "X" and spisok[1][1:2] == 'X' and spisok[2][1:2] == 'X':
        print("X wins")
    elif spisok[0][2:3] == 'X' and spisok[1][2:3] == 'X' and spisok[2][2:3] == 'X':
        print("X wins")

a = convert_to_list(user_input)
x_wins(a)
