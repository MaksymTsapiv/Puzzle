"""puzzle"""


def horizontal_check(board: list):
    """
    """
    for line in board:
        for digit in line:
            if digit != '*' and digit != ' ' and line.count(digit) > 1 or digit == '0':
                return False
    return True


def column_check(board: list):
    """
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
    """
    pass




def validate_board(board: list):
    """

    """
    pass



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
    # import doctest
    # doctest.testmod()
