from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    """
    Solve the N-Queens puzzle and return all distinct solutions.

    The N-Queens puzzle involves placing N chess queens on an N x N chessboard such that
    no two queens threaten each other. This means that no two queens can be in the same
    row, the same column, or along the same diagonal.

    Parameters:
    - n (int): The size of the chessboard (i.e., number of queens).

    Returns:
    - List[List[str]]: A list of solutions, where each solution is represented as a list of strings.
                       Each string in the inner list represents a row on the chessboard.
                       A queen is denoted by 'Q' and an empty space by '.'.

    Example:
    --------
    For n = 4, the function might return:
    [
     ['.Q..',  // Queen at (1,2)
      '...Q',  // Queen at (2,4)
      'Q...',  // Queen at (3,1)
      '..Q.']  // Queen at (4,3)
    ]

    Note: The order of solutions and the order of rows inside each solution may vary.

    We will only test up to n = 11. Beware doing a very high number is possible but will
    require a hyper optimized solution!
    """
