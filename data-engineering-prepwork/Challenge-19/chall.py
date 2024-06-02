class Node:
    """
    This is a Node class that is the building block for the Binary Search Tree.
    Each node contains a value, a pointer to the left child, and a pointer to the right child.
    """

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BST:
    """
    Your challenge is to implement a Binary Search Tree (BST) class. The BST class should have the following methods:

    - __init__(self): A constructor that initializes an empty BST.

    - insert(self, value: int) -> None: A method that takes an integer value, creates a new Node, and inserts it into the BST at the correct position.

    - search(self, value: int) -> bool: A method that takes a value and returns True if the value is in the BST and False otherwise.

    - delete(self, value: int) -> None: A method that deletes a node with a given value from the BST. If the value is not in the BST, it should not modify the BST.
    """
    def __init__(self):
        self.root = None
