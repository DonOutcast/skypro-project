user_input = input()
array = [char if char in "XO" else "_" for char in user_input]


def print_grid(stroka: str) -> None:
    """This is function print your answer in grid game."""
    print("-" * 9 + "\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n".format(*stroka) + "-" * 9)



def o_wins(spisok: list) -> None:
    """This is function print how win and some rules in the game."""
    possible_wins = [spisok[0] + spisok[1] + spisok[2], spisok[3] + spisok[4] + spisok[5], spisok[6] + spisok[7] + spisok[8],
                     spisok[0] + spisok[3] + spisok[6], spisok[1] + spisok[4] + spisok[7], spisok[2] + spisok[5] + spisok[8],
                     spisok[0] + spisok[4] + spisok[8], spisok[2] + spisok[4] + spisok[6]]
    if 'X' * 3 in possible_wins and 'O' * 3 not in possible_wins:
        print("X wins")
    elif 'O' * 3 in possible_wins and 'X' * 3 not in possible_wins:
        print("O wins")
    elif "_" not in array:
        print("Draw")
    elif '_' in array and 'X' * 3 not in possible_wins and 'O' * 3 not in possible_wins and array.count("X") == array.count("O"):
        print("Game not finished")
    else:
        print("Impossible")
        
print_grid(array)
o_wins(array)
