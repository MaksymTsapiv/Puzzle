"""puzzle"""


def horizontal_check(board: list):
    """
    Horizontal check
    >>> horizontal_check(['*  *', '**12'])
    True
    >>> horizontal_check(['****', '**11'])
    False
    """
    for line in board:
        for digit in line:
            if digit != '*' and digit != ' ' and line.count(digit) > 1 or digit == '0':
                return False
    return True


def column_check(board: list):
    """
    Column check
    >>> column_check([' ***', ' *23', '*45*'])
    True
    >>> column_check(['1***', '1*2 ', '**5 '])
    False
    """
    result = [[None] * len(board) for _ in range(len(board[0]))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            result[j][i] = board[i][j]
    for k in range(len(result)):
        result[k] = "".join(result[k])
    return horizontal_check(result)



def color_check(board: list):
    """
    Check color
    """
    col_board = []
    for i in range(5):
        col_board.append(one_color(board, i, 4 - i))
    return horizontal_check(col_board)
    


def one_color(board, i, j):
    """
    Returns one color
    """
    color = []
    for k in range(5):
        color.append(board[i + k][j])
    for l in range(4):
        color.append(board[i + 4][j + l + 1])
    return color
    


def validate_board(board: list):
    """
    Validate board
    """
    return horizontal_check(board) and column_check(board) and color_check(board)



if __name__ == '__main__':
    board = [
    "**** ****",
    "***1 ****",
    "**  3****",
    "* 4 1****",
    "     9 5 ",
    " 6  83  *",
    "3   1  **",
    "  8  2***",
    "  2  ****"
    ]
    # print(horizontal_check(['***1***','***238 **','**2***',]))
    # print(column_check(['1***56',' ***23','*** **','  8** ','******','******']))
    # print(column_check(board))
    # print(color_check(board))
    # print(one_color(board, 0, 4))
    # print(color_check(board))
    print(validate_board(board))
    # import doctest
    # doctest.testmod()
