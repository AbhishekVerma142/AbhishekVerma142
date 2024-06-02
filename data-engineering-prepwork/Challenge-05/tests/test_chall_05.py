import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_is_palindrome():
    assert True == chall.is_palindrome("Able was I ere I saw Elba"), "The function should return True for palindromes."
    assert False == chall.is_palindrome("Hello, world!"), "The function should return False for non-palindromes."
    assert True == chall.is_palindrome("A man, a plan, a canal: Panama"), "The function should correctly handle punctuation and whitespace."
    assert True == chall.is_palindrome(""), "An empty string is considered a palindrome."
