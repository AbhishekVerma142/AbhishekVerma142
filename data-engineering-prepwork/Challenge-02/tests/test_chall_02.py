import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_add_two_numbers():
    assert 3 == chall.add_two_numbers(1, 2), "The function should return the sum of the two numbers."
    assert 4 == chall.add_two_numbers(-1, 5), "The function should handle negative numbers correctly."
