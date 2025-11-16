import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *

class BSTTests(unittest.TestCase):

    def test_is_empty(self):
        t1 : BinarySearchTree = BinarySearchTree(comes_before_int, Node(4, Node(2, Node(1, None, None), Node(3, None, None)), Node(8,None, None)))
        t2 : BinarySearchTree = BinarySearchTree(comes_before_str, None)
        self.assertFalse(is_empty(t1))
        self.assertTrue(is_empty(t2))
    
    def test_insert_amd_lookup(self):
        tree = BinarySearchTree(comes_before_int, None)
        values = [10, 5, 15, 3, 7]

        for n in values:
            tree = insert(tree, n)
        
        self.assertFalse(lookup(tree, 9900))

    def test_delete(self):
        tree = BinarySearchTree(comes_before_int, None)
        for n in [10, 20, 30 , 500]:
            tree = insert(tree, n)

        self.assertTrue(lookup(tree, 10))
        tree = delete(tree, 10)
        self.assertFalse(lookup(tree, 10))

if (__name__ == '__main__'):
    unittest.main()