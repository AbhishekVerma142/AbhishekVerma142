import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_multiply_all_elements():
    assert 120 == chall.multiply_all_elements([1, 2, 3, 4, 5]), "The function should return the product of all elements in the list."
    assert -24 == chall.multiply_all_elements([-1, 2, 3, 4]), "The function should handle negative numbers correctly."
    assert 1 == chall.multiply_all_elements([]), "The function should return 1 for an empty list."
