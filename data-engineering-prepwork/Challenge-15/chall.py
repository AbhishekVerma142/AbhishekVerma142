from typing import List, Tuple

def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str) -> List[Tuple[int, str, str]]:
    """
    Your challenge is to implement the Tower of Hanoi puzzle using recursion.
    The Tower of Hanoi is a mathematical puzzle where you have three pegs and a number of disks of different sizes.
    The objective is to move the entire stack of disks from the source peg to the destination peg, obeying the following rules:
    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack.
    3. No disk may be placed on top of a smaller disk.

    The function should return a list of moves required to solve the Tower of Hanoi puzzle.
    Each move is represented as a tuple (disk_number, source_peg, destination_peg).

    Example:
    tower_of_hanoi(3, 'A', 'C', 'B') should return [(1, 'A', 'C'), (2, 'A', 'B'), (1, 'C', 'B'), (3, 'A', 'C'), (1, 'B', 'A'), (2, 'B', 'C'), (1, 'A', 'C')]
    """

    pass
