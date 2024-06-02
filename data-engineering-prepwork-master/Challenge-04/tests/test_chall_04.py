import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_count_elements():
    assert {1: 3, 2: 2, 3: 1} == chall.count_elements([1, 1, 1, 2, 2, 3]), "The function should return the correct counts of each number."
    assert {5: 1, 7: 2, 9: 3} == chall.count_elements([5, 7, 7, 9, 9, 9]), "The function should handle different sets of numbers correctly."
    assert {} == chall.count_elements([]), "The function should return an empty dictionary for an empty list."
