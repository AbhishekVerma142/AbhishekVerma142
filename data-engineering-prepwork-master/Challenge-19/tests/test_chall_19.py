import sys
from pathlib import Path


current_script_path = Path(__file__).resolve()
module_path = current_script_path.parent.parent / 'chall.py'
sys.path.append(str(module_path.parent))

import chall

def test_bst():
    bst = chall.BST()

    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    assert bst.search(10) == True, "The BST should contain the value 10."
    assert bst.search(5) == True, "The BST should contain the value 5."
    assert bst.search(15) == True, "The BST should contain the value 15."
    assert bst.search(3) == True, "The BST should contain the value 3."
    assert bst.search(7) == True, "The BST should contain the value 7."
    assert bst.search(12) == True, "The BST should contain the value 12."
    assert bst.search(18) == True, "The BST should contain the value 18."

    assert bst.root.value == 10, "The root should have the value 10."
    assert bst.root.left.value == 5, "The left child of root should have the value 5."
    assert bst.root.right.value == 15, "The right child of root should have the value 15."
    assert bst.root.left.left.value == 3, "The left-left grandchild of root should have the value 3."
    assert bst.root.left.right.value == 7, "The left-right grandchild of root should have the value 7."
    assert bst.root.right.left.value == 12, "The right-left grandchild of root should have the value 12."
    assert bst.root.right.right.value == 18, "The right-right grandchild of root should have the value 18."

    assert bst.search(2) == False, "The BST should not contain the value 2."
    assert bst.search(20) == False, "The BST should not contain the value 20."

    bst.delete(5)
    assert bst.search(5) == False, "The BST should not contain the value 5 after it has been deleted."
    assert type(bst.root) == chall.Node, "Root should be a Node type"
    assert bst.root.left.value == 7, "The left child of root should be updated to 7 after deleting 5."
