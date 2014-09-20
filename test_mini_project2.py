# unit tests for Project 2 (Connected components and graph resilience), by k., 09/20/2014

import unittest
from project2 import bfs_visited
from project2 import cc_visited
from project2 import largest_cc_size
from project2 import compute_resilience


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.GRAPH1 = {0: set([1]),
                       1: set([2, 0, 3]),
                       2: set([3, 1]),
                       3: set([1, 2, 4, 5]),
                       4: set([3]),
                       5: set([3]),
                       6: set([7, 8]),
                       7: set([8, 6]),
                       8: set([6, 7]),
                       9: set([])}
        self.GRAPH2 = {0:set([]),
                       1:set([2,3,4]),
                       2:set([1,3]),
                       3:set([1,2]),
                       4:set([1]),
                       5:set([6]),
                       6:set([5]),
                       7:set([])}
    def test_visited(self):
        self.assertEqual(set(range(6)), bfs_visited(self.GRAPH1, 0))
        self.assertEqual(set(range(1)), bfs_visited(self.GRAPH2, 0))
        self.assertEqual(set(range(1, 5)), bfs_visited(self.GRAPH2, 1))
        self.assertEqual(set(range(5, 7)), bfs_visited(self.GRAPH2, 5))
        self.assertEqual(set(range(7, 8)), bfs_visited(self.GRAPH2, 7))
        self.assertEqual(set([9]), bfs_visited(self.GRAPH1, 9))
        self.assertEqual(set(range(6,9)), bfs_visited(self.GRAPH1, 8))
    def test_cc_visited(self):
        self.assertEqual(([set([0, 1, 2, 3, 4, 5]), set([8, 6, 7]), set([9])]),
                         cc_visited(self.GRAPH1))
        self.assertEqual(([set([0]), set([1, 2, 3, 4]), set([5, 6]), set([7])]),
                         cc_visited(self.GRAPH2))
    def test_largest(self):
        self.assertEqual(largest_cc_size(self.GRAPH1), 6)
        self.assertEqual(largest_cc_size(self.GRAPH2), 4)
    def test_resilience(self):
        self.assertEqual(compute_resilience(self.GRAPH1, range(10)),
                         [6, 5, 4, 3, 3, 3, 3, 2, 1, 1, 0])
        self.assertEqual(compute_resilience(self.GRAPH2, [1,4,5]),
                         [4, 2, 2, 2])
        
              
# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
