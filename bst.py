import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

BinTree: TypeAlias = Union["Node", None]
@dataclass
class Node:
    value: Any 
    left: BinTree
    right: BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any,Any],bool]
    bt: BinTree

@dataclass(frozen=True)
class Point2:
    x: int
    y: int

# def comes_before(val1: Any, val2: Any) -> bool:
#     if type(val1) == str and type(val2) == str:
#         return val1 < val2
#     elif (type(val1) == float and type(val2) == float) or (type(val1) == int and type(val2) == int):
#         return val1 < val2
#     else:
#          raise ValueError("Input values must be the same type")
# returns whether val1 is less than val2
def comes_before_int(val1: int, val2: int) -> bool:
    return val1 < val2
    
#return whether val1 comes before val2 alphabetically
def comes_before_str(str1: str, str2: str) -> bool:
        return str1 < str2

#returns the distance between the origin and the point
def euclidean_distance(point: Point2) -> float:
    return ((point.x)**2 +(point.y)**2) ** (1/2)

# returns true if the binary tree in the BST is empty
def is_empty(tree : BinarySearchTree) -> bool:
    if not tree:
        return True
    return tree.bt is None
# adds a value into a BST
def insert(tree: BinarySearchTree, val: Any) -> BinarySearchTree:
    # if is_empty(tree):
    #     raise ValueError("Provided an empty tree")
    # return_tree: BinarySearchTree
    # # if comes_before(val, tree.bt.value):
    # #     return_tree = (val, tree)
    # match tree:
    #     case is_empty(tree):
    return BinarySearchTree(tree.comes_before, insert_helper(tree.comes_before, tree.bt, val))
# helper function for insert to actually insert value to appropriate tree spot
def insert_helper(comes_before: Callable[[Any, Any], bool], bt: BinTree, val: Any) -> BinTree:
    match bt:
        case None:
            return Node(val, None, None)
        case Node(v, l, r):
            if comes_before(v, val):
                return Node(v, insert_helper(comes_before, l, val), r)
            else:
                return Node(v, l, insert_helper(comes_before, r, val))

def lookup(tree: BinarySearchTree, val: Any) -> bool:
    return lookup_helper(tree.comes_before, tree.bt, val)
    

def lookup_helper(comes_before: Callable[[Any, Any], bool], bt: BinTree, val:Any) -> bool:
    match bt:
        case None:
            raise ValueError("tree is empty, val not present")
        case Node(v, l, r):
            if (v == val):
                return True
            else:
                if comes_before(val, v):
                    return lookup_helper(comes_before(val, l.value), l, val)
                else:
                    return lookup_helper(comes_before(val, r.value), r, val)
                return False
    
#removes val from the tree if it is present and reorders it so it remains a proper BST 
def delete(tree: BinarySearchTree, val: Any) -> None:
    pass

                
class Tests(unittest.TestCase):
    def test_is_empty(self):
        t1 : BinarySearchTree = BinarySearchTree(comes_before_int, Node(4, Node(2, Node(1, None, None), Node(3, None, None)), Node(8,None, None)))
        t2: BinarySearchTree = BinarySearchTree(comes_before_str, None)
        self.assertFalse(is_empty(t1))
        self.assertTrue(is_empty(t2))

        
    
if (__name__ == '__main__'):
    unittest.main()