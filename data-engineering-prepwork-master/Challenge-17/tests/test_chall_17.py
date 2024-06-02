import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import sqlite3
import chall

def test_create_table(tmp_path):
    db_file = tmp_path / "test.db"

    conn = sqlite3.connect(str(db_file))
    conn.execute("DROP TABLE IF EXISTS employees")
    conn.close()

    chall.create_table(db_file)

    conn = sqlite3.connect(str(db_file))
    cursor = conn.execute("PRAGMA table_info(employees)")
    columns = cursor.fetchall()
    conn.close()

    expected_columns = [
        (0, 'id', 'INTEGER', 0, None, 1),
        (1, 'name', 'TEXT', 0, None, 0),
        (2, 'age', 'INTEGER', 0, None, 0),
        (3, 'salary', 'REAL', 0, None, 0)
    ]

    assert columns == expected_columns
