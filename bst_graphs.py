import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)
from bst import *
import time

TREES_PER_RUN : int = 10000
def example_graph_creation() -> None:
 # Return log-base-2 of 'x' + 5.
    def f_to_graph( x : float ) -> float:
        return math.log2( x ) + 5.0
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
    y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

def height(bst: BinarySearchTree) -> int:
    def height_bt(bt: BinTree) -> int:
        match bt:
            case None:
                return 0
            case Node(_, l, r):
                return 1 + max(height_bt(l), height_bt(r))
    return height_bt(bst.bt)

def graph_avg_height_vs_n() -> None:
    # def f_to_graph(x: float) -> float:
    #     n = int(x)
    #     heights: List[float] = [height(random_tree(n)) for _ in range(TREES_PER_RUN)]
    #     avg_height: float = sum(heights) / len(heights)
    #     return avg_height

    def f_to_graph(x: float) -> float:
        n = int(x)
        times: List[float] = []
        for _ in range(TREES_PER_RUN):
            tree = random_tree(n)
            new_val = random.random()
            start = time.perf_counter()
            insert(tree, new_val)
            end = time.perf_counter()
            times.append(end - start)
        avg_time = sum(times) / len(times)
        return avg_time
    
    x_coords: List[float] = [float(i) for i in np.linspace(1, n_max, 50)]
    y_coords: List[float] = [f_to_graph(x) for x in x_coords]

    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array type.
    x_numpy: np.ndarray = np.array(x_coords)
    y_numpy: np.ndarray = np.array(y_coords)

    # plt.plot(x_numpy, y_numpy, label='Average Tree Height')
    # plt.xlabel("N (Tree Size)")
    # plt.ylabel("Average Height")
    # plt.title("Average Tree Height vs. N")
    plt.plot(x_numpy, y_numpy, label='Average Insert Time')
    plt.xlabel("N (Tree Size)")
    plt.ylabel("Average Time to Insert (seconds)")
    plt.title("Average Time to Insert vs. N")
    plt.grid(True)
    plt.legend()  # makes the 'label's show up
    plt.show()


#generates BinarySearchTree with n random floats in [0, 1]
def random_tree(n: int) -> BinarySearchTree:
    tree: BinarySearchTree = BinarySearchTree(comes_before_int, None)

    for _ in range(n):
        r_val = random.random()
        tree = insert(tree, r_val)

    return tree

if (__name__ == '__main__'):
    # example_graph_creation()
    n_max = 10

    # while True:
    #     start_time = time.perf_counter()
    #     for _ in range(TREES_PER_RUN):
    #         random_tree(n)       # build a random tree of size n
    #     elapsed = time.perf_counter() - start_time
    #     print(f"n = {n}, total time = {elapsed} seconds")

    #     if 1.5 <= elapsed <= 2.5:
    #         print(f"n_max = {n}")
    #         break

    #     # increase or decrease n depending on speed
    #     if elapsed < 1.5:
    #         n = int(n * 1.5)   # trees are fast → increase n
    #     else:
    #         n = int(n * 0.8)   # trees are slow → decrease n

    graph_avg_height_vs_n()