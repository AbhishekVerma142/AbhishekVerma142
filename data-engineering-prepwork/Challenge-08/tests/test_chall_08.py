import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_remove_duplicates():
    assert [1, 2, 3] == chall.remove_duplicates([1, 1, 2, 2, 3, 3]), "The function should remove duplicate elements."
    assert [1, 2, 3, -1, 0] == chall.remove_duplicates([1, 2, 3, -1, 0]), "The function should handle lists without duplicates correctly."
    assert [] == chall.remove_duplicates([]), "The function should return an empty list when given an empty list."
