class Monad:
    """
    This is a generic monad it is a simple representation of a monad.
    Try to understand how it works and the then try and implement the Optional monad below!
    - `unit`: Takes a value and wraps it in the Monad.
    - `bind`: Takes a function that operates on the value inside the Monad and returns a new Monad.
    - `get_value`: Returns the value inside the Monad.

    Example usage:
    >>> m = Monad.unit(5)
    >>> m.get_value()
    5

    >>> def add_one(x):
    ...     return Monad.unit(x + 1)
    ...
    >>> m.bind(add_one).get_value()
    6
    """

    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return func(self.value)

    def get_value(self):
        return self.value

    @staticmethod
    def unit(value):
        return Monad(value)

class Optional:
    """
    An Optional monad that represents a value which might be present or absent.

    The Optional monad is used to handle cases where a value might not be present,
    without resorting to the explicit use of None or null. It promotes explicit
    handling of such cases, leading to safer code. This class provides methods to
    wrap a value, transform it, and retrieve it.

    Methods:
    - `unit`: Accepts a value and wraps it in the Optional monad. If the value is None,
              it denotes absence.
    - `bind`: Accepts a function that operates on the wrapped value, returning a new
              Optional. If the contained value is absent (None), it returns an absent
              Optional without invoking the function.
    - `get_value`: Returns the contained value or raises an exception if the value is absent.

    Example usage:
    >>> m = Optional.unit(5)
    >>> m.get_value()
    5

    >>> def add_one(x):
    ...     return Optional.unit(x + 1)
    ...
    >>> m.bind(add_one).get_value()
    6

    >>> n = Optional.unit(None)
    >>> n.bind(add_one).get_value()
    Raises ValueError: No value present in Optional.
    """
    pass
