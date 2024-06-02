import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_metaclass_magic():
    class Wizard(metaclass=chall.MagicMeta):
        def spell(cls):
            return "Casting a powerful spell!"

    assert Wizard.magic == 'Abracadabra!'
    assert Wizard.spell() == 'Casting a powerful spell!'

    class Sorcerer(metaclass=chall.MagicMeta):
        pass

    assert Sorcerer.magic == 'Abracadabra!'
    assert Sorcerer.spell() == 'Casting a spell!'
