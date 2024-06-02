import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_car():
    car = chall.Car("Toyota")

    assert car.get_wheels() == 4, "A car should always have 4 wheels."
    assert car.get_name() == "Toyota", "The car's brand should be Toyota."
    assert car.car_info() == {'brand': 'Toyota', 'wheels': 4}, "The car_info method should return a dictionary with keys 'brand' and 'wheels'."
