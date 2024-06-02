class Animal:
    """
    This is a base class for animals.
    It includes an initializer that sets the animal's name and a method for getting the animal's name.
    """

    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        """
        This method returns the name of the animal.
        """
        return self._name

class Dog(Animal):
    """
    Your challenge is to implement a Dog class that inherits from the Animal class.
    The Dog class should include the following methods:

    - bark(self) -> str: A method that returns a string representing the dog's bark.

    Remember, since Dog is a subclass of Animal, it should be initialized with a name.
    """
    pass
