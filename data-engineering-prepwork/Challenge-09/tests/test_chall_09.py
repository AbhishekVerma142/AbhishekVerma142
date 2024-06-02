import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_reverse_words():
    assert "world! Hello," == chall.reverse_words("Hello, world!"), "The function should reverse the order of words, but not the words themselves or the punctuation attached to them."
    assert "dog. lazy the over jumped fox quick The" == chall.reverse_words("The quick fox jumped over the lazy dog."), "The function should handle longer sentences correctly."
    assert "" == chall.reverse_words(""), "The function should return an empty string when given an empty string."
