import sys
from pathlib import Path
import pytest


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_optional():
    opt = chall.Optional.unit(5)
    assert opt.get_value() == 5

    opt_none = chall.Optional.unit(None)
    with pytest.raises(ValueError):
        opt_none.get_value()

    opt = chall.Optional.unit(5)

    def add_one(x):
        return chall.Optional.unit(x + 1)

    opt1 = opt.bind(add_one)
    assert opt1.get_value() == 6
    assert isinstance(opt1, chall.Optional)

    opt_none = chall.Optional.unit(None)
    opt_none_result = opt_none.bind(add_one)
    with pytest.raises(ValueError):
        opt_none_result.get_value()

    opt = chall.Optional.unit(42)
    assert opt.is_present()

    opt_none = chall.Optional.unit(None)
    assert not opt_none.is_present()
