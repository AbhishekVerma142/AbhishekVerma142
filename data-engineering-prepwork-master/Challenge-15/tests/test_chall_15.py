import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_tower_of_hanoi():
    assert chall.tower_of_hanoi(3, 'A', 'C', 'B') == [
        (1, 'A', 'C'),
        (2, 'A', 'B'),
        (1, 'C', 'B'),
        (3, 'A', 'C'),
        (1, 'B', 'A'),
        (2, 'B', 'C'),
        (1, 'A', 'C')
    ]

    assert chall.tower_of_hanoi(4, 'A', 'C', 'B') == [
        (1, 'A', 'B'),
        (2, 'A', 'C'),
        (1, 'B', 'C'),
        (3, 'A', 'B'),
        (1, 'C', 'A'),
        (2, 'C', 'B'),
        (1, 'A', 'B'),
        (4, 'A', 'C'),
        (1, 'B', 'C'),
        (2, 'B', 'A'),
        (1, 'C', 'A'),
        (3, 'B', 'C'),
        (1, 'A', 'B'),
        (2, 'A', 'C'),
        (1, 'B', 'C')
    ]
