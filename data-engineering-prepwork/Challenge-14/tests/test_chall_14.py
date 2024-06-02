import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_dfs():
    leaf1 = chall.Node(4, [])
    leaf2 = chall.Node(5, [])
    leaf3 = chall.Node(6, [])
    internal1 = chall.Node(2, [leaf1, leaf2])
    internal2 = chall.Node(3, [leaf3])
    root = chall.Node(1, [internal1, internal2])

    assert [1, 2, 4, 5, 3, 6] == chall.dfs(root), "The function should return the correct list of values."
