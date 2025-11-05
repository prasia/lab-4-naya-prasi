import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

BinTree: TypeAlias = Union["Node", None]
@dataclass
class Node:
    element: Any
    value: Any

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any,Any],bool]
    bt: BinTree

