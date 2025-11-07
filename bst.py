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

def comes_before(val1: Any, val2: Any) -> bool:
    if type(val1) == str and type(val2) == str:
        return val1 < val2
    elif (type(val1) == float and type(val2) == float) or (type(val1) == int and type(val2) == int):
        return val1 < val2
    else:
         raise ValueError("Input values must be the same type")

def is_empty(tree : BinarySearchTree) -> bool:
    return tree.bt is None
        
def insert(tree: BinarySearchTree, val: Any) -> BinarySearchTree:
    # if is_empty(tree):
    #     raise ValueError("Provided an empty tree")
    # return_tree: BinarySearchTree
    # # if comes_before(val, tree.bt.value):
    # #     return_tree = (val, tree)
    # match tree:
    #     case is_empty(tree):
    return BinarySearchTree(tree.comes_before, insert_helper(tree.comes_before, tree.bt, val))

def insert_helper(comes_before: Callable[[Any, Any], bool], bt: BinTree, val: Any) -> BinTree:
    match bt:
        case None:
            return Node(val, None, None)
        case Node(v, l, r):
            if comes_before(v, val):
                return Node(v, insert_helper(comes_before, l, val), r)
            else:
                return Node(v, l, insert_helper(comes_before, r, val))
                
                

     