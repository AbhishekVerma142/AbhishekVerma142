class MagicMeta(type):
    """
    Your challenge is to implement a metaclass that adds some magic behavior to its subclasses.
    The metaclass should override the `__new__` method to modify the creation of new classes as follows:
    - The metaclass should automatically add a class attribute named `magic` to the subclass with the value "Abracadabra!".
    - The metaclass should also check if the subclass has a method named `spell` and if not, add a default implementation of `spell` that returns "Casting a spell!".

    Example usage:
    >>> class Wizard(metaclass=MagicMeta):
    ...     pass
    ...
    >>> Wizard.magic
    'Abracadabra!'
    >>> Wizard.spell()
    'Casting a spell!'
    """
    pass
