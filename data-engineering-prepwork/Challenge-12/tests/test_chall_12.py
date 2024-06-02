import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_dog():
    dog = chall.Dog("Fido")

    assert dog.get_name() == "Fido", "The dog's name should be Fido."
    assert dog.bark() == "Woof!", "The dog should bark 'Woof!'"
