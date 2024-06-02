from typing import List, Any

class Node:
    def __init__(self, value: Any, children: List['Node']):
        self.value = value
        self.children = children

def dfs(root: Node) -> List[Any]:
    """
    Your challenge is to implement the Depth-First Search (DFS) algorithm on a tree.
    The function should return a list of values, representing the order in which nodes were visited in a DFS traversal starting from the root.

    The tree nodes are represented by instances of the Node class, which includes a value and a list of children nodes.
    """
    pass
