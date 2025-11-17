import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *

class BSTTests(unittest.TestCase):
    def test_comes_before_int(self):
        self.assertTrue(comes_before_int(1, 2))
        self.assertFalse(comes_before_int(5, 3))
        self.assertFalse(comes_before_int(4, 4))

    def test_comes_before_str(self):
        self.assertTrue(comes_before_str("apple", "banana"))
        self.assertFalse(comes_before_str("zebra", "ant"))
        self.assertFalse(comes_before_str("same", "same"))

    def test_comes_before_point(self):
        p1 = Point2(3, 4)  
        p2 = Point2(6, 8)   
        p3 = Point2(0, 0)   
        self.assertTrue(comes_before_point(p3, p1))  
        self.assertTrue(comes_before_point(p1, p2))   
        self.assertFalse(comes_before_point(p2, p1))  
        self.assertFalse(comes_before_point(p1, p1))
    
    def test_point_distance_precision(self):
        p1 = Point2(1, 1)
        p2 = Point2(1, 1)
        self.assertFalse(comes_before_point(p1, p2))

    def test_is_empty(self):
        t1 : BinarySearchTree = BinarySearchTree(comes_before_int, Node(4, Node(2, Node(1, None, None), Node(3, None, None)), Node(8,None, None)))
        t2 : BinarySearchTree = BinarySearchTree(comes_before_str, None)
        self.assertFalse(is_empty(t1))
        self.assertTrue(is_empty(t2))
    
    def test_insert_and_lookup_int(self):
        tree = BinarySearchTree(comes_before_int, None)
        values = [10, 5, 15, 3, 7]
        for n in values:
            tree = insert(tree, n)
        self.assertFalse(lookup(tree, 9900))

    def test_delete_int(self):
        tree = BinarySearchTree(comes_before_int, None)
        for n in [10, 20, 30 , 500]:
            tree = insert(tree, n)
        self.assertTrue(lookup(tree, 10))
        tree = delete(tree, 10)
        self.assertFalse(lookup(tree, 10))

    def test_insert_lookup_str(self):
        t = BinarySearchTree(comes_before_str, None)
        words = ["mango", "apple", "zebra"]
        for w in words:
            t = insert(t, w)
        self.assertTrue(lookup(t, "apple"))
        self.assertFalse(lookup(t,"pear"))

    def test_delete_str(self):
        # t = BinarySearchTree(comes_before_str, None)
        
        # for w in ["m", "a", "z"]:
        #     t = insert(t, w)
        #     self.assertTrue(lookup(t, "a"))

        t = BinarySearchTree(
        comes_before_str,
        Node("m", Node("a", None, None), Node("z", None, None))
    )
        self.assertTrue(lookup(t, "a"))

        t = delete(t, "a")
        self.assertFalse(lookup(t, "a"))

if __name__ == "__main__":
    unittest.main()