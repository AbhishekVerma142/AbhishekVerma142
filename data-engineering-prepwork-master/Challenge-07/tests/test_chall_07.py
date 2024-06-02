import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_is_leap_year():
    assert True == chall.is_leap_year(2000), "The function should return True for leap years."
    assert False == chall.is_leap_year(1900), "The function should return False for non-leap years."
    assert False == chall.is_leap_year(2001), "The function should return False for non-leap years."
