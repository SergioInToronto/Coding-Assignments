# 7 wide x 6 high
# 2 player
# terminal is fine


import copy


token_at_position = [
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
    [None, None, None, None, None, None],
]


def draw_board():
    draw_columns = []
    for column_index, column in enumerate(token_at_position):
        draw_column = copy.deepcopy(column)
        while len(draw_column) < 7:
            draw_column.append('_')
        draw_columns.append(draw_column)


    # TODO: more pretty!
    for current_column in range(6, -1, -1):
        for column in draw_columns:
            print(column[current_column] and column[current_column][0] or '_', end='')
        print('')


def insert(colour, column):
    if all(token_at_position[column]):
        # TODO: ask for another column instead of failing
        raise RuntimeError('This column is full!')

    for index, value in enumerate(token_at_position[column]):
        if value is None:
            token_at_position[column][index] = colour
            return


def check_win(column_of_new_token):
    # Check columns
    column = token_at_position[column_of_new_token]
    winner = _check_column(column)
    if winner:
        return winner

    # Check rows
    height = len(_tokens_in_column(token_at_position[column_of_new_token])) - 1
    row = [column[height] and column[height][0] for column in token_at_position]
    winner = _check_row(row)
    if winner:
        return winner

    # Check diagonal
    # diagonal-up-left

    # diagonal-up-right
    token_colours = []
    # row, column
    coor = (column_of_new_token, height)
    new_coor = coor
    # while True:
    #     new_coor = (coor[0] + 1, coor[1] + 1)
    #     new_coor




def _check_4_in_a_row(token_colours):
    if len(token_colours) < 4:
        return

    # # Silly solution
    # str_tokens = ''.join(token_colours)
    # if 'redredredred' in str_tokens:
    #     return "red"
    # if 'blueblueblueblue' in str_tokens:
    #     return "blue"


    current_colour = token_colours[0]
    count = 1
    for token in token_colours:
        if count >= 4:
            return current_colour
        if current_colour == token:
            count += 1
        else:
            current_colour = token
            count = 1

    if count >= 4:
        return current_colour



def _check_column(column):
    current_colour = None
    current_count = 0
    for token_colour in column:
        if current_colour and current_colour == token_colour:
            current_count += 1
        else:
            current_colour = token_colour
            current_count = 1

    if current_colour and current_count >= 4:
        return current_colour




def _check_row(row):
    current_colour = None
    current_count = 0
    for index, token_colour in enumerate(row):
        if current_count >= 4:
            return current_colour
        if current_colour == token_colour:
            current_count += 1
        else:
            current_colour = token_colour
            current_count = 1

    if current_colour and current_count >= 4:
        return current_colour


def _tokens_in_column(column):
    return [x for x in column if x]


def run():
    print("Let's play Connect Four!")
    print("Player 1 is red, player 2 is blue")
    print("Player 1's turn")

    current_player_colour = "red"
    winner = None

    for turn_number in range(42):
        draw_board()
        position = input(f"{current_player_colour}'s turn. Enter a column (0-5): ")
        column = int(position)
        insert(current_player_colour, column)

        winner = check_win(column)
        if winner:
            break

        current_player_colour = current_player_colour == "red" and "blue" or "red"



    if turn_number == 42:
        raise RuntimeError("Something awful happened")

    if winner:
        print(f"{winner} WINS!! 🎉🎉🎉")
    else:
        print("Draw game!")



if __name__ == '__main__':
    run()
    # TODO: ask to play again?
