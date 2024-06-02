import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_find_max_in_list():
    assert 5 == chall.find_max_in_list([1, 2, 3, 4, 5]), "The function should return the maximum number in the list."
    assert -1 == chall.find_max_in_list([-1, -2, -3, -4, -5]), "The function should handle negative numbers correctly."
    assert None is chall.find_max_in_list([]), "The function should return None for an empty list."
