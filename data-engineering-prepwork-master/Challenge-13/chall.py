class Vehicle:
    """
    This is a base class for Vehicles.
    It includes an initializer that sets the vehicle's number of wheels.
    """

    def __init__(self, wheels: int):
        self._wheels = wheels

    def get_wheels(self) -> int:
        """
        This method returns the number of wheels of the vehicle.
        """
        return self._wheels


class Brand:
    """
    This is a base class for Brands.
    It includes an initializer that sets the brand's name.
    """

    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        """
        This method returns the name of the brand.
        """
        return self._name


class Car(Vehicle, Brand):
    """
    Your challenge is to implement a Car class that inherits from both the Vehicle and Brand classes.
    A Car is a Vehicle that always has 4 wheels, and it also has a brand name.
    The Car class should also include the following method:

    - car_info(self) -> dict: A method that returns a dictionary with keys 'brand' and 'wheels', containing the car's brand name and number of wheels, respectively.

    Remember, since Car is a subclass of Vehicle and Brand, it should use the Vehicle and Brand classes' __init__ methods.
    """
    pass
