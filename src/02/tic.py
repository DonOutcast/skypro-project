user_input = input()


def convert_to_list(stroka: str) -> list:
    """This function coverting your string to list"""
    spisok = []
    spisok.append(user_input[0:3])
    spisok.append(user_input[3:6])
    spisok.append(user_input[6:9])
    return spisok


def print_grid(spisok: list) -> None:
    """This function print to console grid """
    print("---------")
    for rows in spisok:
        print("| ", " ".join(words for words in rows), " |")
    print("---------")


print_grid(convert_to_list(user_input))

