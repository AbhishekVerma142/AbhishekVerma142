import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_find_pairs_with_sum():
    assert [(1, 2), (0, 3)] == chall.find_pairs_with_sum([1, 2, 3, 0], 3), "The function should return all pairs with the sum equal to the target."
    assert [(1, 4), (2, 3)] == chall.find_pairs_with_sum([1, 4, 2, 3], 5), "The function should handle different sets of numbers correctly."
    assert [] == chall.find_pairs_with_sum([1, 2, 3, 4], 10), "The function should return an empty list if no pairs sum to the target."
    assert [] == chall.find_pairs_with_sum([], 0), "The function should return an empty list when given an empty list."
