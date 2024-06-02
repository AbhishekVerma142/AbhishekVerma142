import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_solve_n_queens():
    solutions = chall.solve_n_queens(4)
    expected_solutions = [
        ['.Q..', '...Q', 'Q...', '..Q.'],
        ['..Q.', 'Q...', '...Q', '.Q..']
    ]

    assert set(tuple(sol) for sol in solutions) == set(tuple(sol) for sol in expected_solutions)

    solutions = chall.solve_n_queens(1)
    assert solutions == [['Q']]

    assert chall.solve_n_queens(2) == []
    assert chall.solve_n_queens(3) == []

    solutions = chall.solve_n_queens(8)
    assert len(solutions) == 92

    solutions = chall.solve_n_queens(11)
    assert len(solutions) == 2680
