# unit tests for Project 1 (Degree distributions for graphs), by k., 09/03/2014

import unittest
from project1 import EX_GRAPH0, EX_GRAPH1, EX_GRAPH2
from project1 import compute_in_degrees
from project1 import in_degree_distribution


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.GRAPH3 = {0: set([1, 2, 3, 4]),
                       1: set([0, 2, 3, 4]),
                       2: set([0, 1, 3, 4]),
                       3: set([0, 1, 2, 4]),
                       4: set([0, 1, 2, 3])}
        self.GRAPH4 = {'dog': set(['cat']),
                       'cat': set(['dog']),
                       'monkey': set(['banana']),
                       'banana': set([])}
        self.GRAPH5 = {1: set([2, 4, 6, 8]),
                       2: set([1, 3, 5, 7]),
                       3: set([4, 6, 8]),
                       4: set([3, 5, 7]),
                       5: set([6, 8]),
                       6: set([5, 7]),
                       7: set([8]),
                       8: set([7])}
        self.GRAPH6 = {1: set([2, 5]),
                       2: set([1, 7]),
                       3: set([4, 6, 9]),
                       4: set([6]),
                       5: set([2, 7]),
                       6: set([4, 9]),
                       7: set([1, 5]),
                       9: set([3, 4])}
        self.GRAPH7 = {0: set([1, 2, 3, 4]), 
                       1: set([0, 2, 3, 4]), 
                       2: set([0, 1, 3, 4]), 
                       3: set([0, 1, 2, 4]), 
                       4: set([0, 1, 2, 3]), 
                       5: set([2, 3, 4]), 
                       6: set([0, 1, 4]), 
                       7: set([0, 1, 2, 3]), 
                       8: set([0, 1, 4, 7]), 
                       9: set([2, 4]), 
                      10: set([1, 2, 4]), 
                      11: set([1, 3, 4, 7]), 
                      12: set([0, 2, 3]), 
                      13: set([0, 2, 4, 10]), 
                      14: set([0, 2, 3, 4, 13])}
    def test_degrees(self):
        self.assertEqual(in_degree_distribution(EX_GRAPH0), {0: 1, 1: 2})
        self.assertEqual(in_degree_distribution(EX_GRAPH1), {1: 5, 2: 2})
        self.assertEqual(in_degree_distribution(EX_GRAPH2), {0: 2, 1: 1, 2: 3, 3: 4})
        self.assertEqual(in_degree_distribution(self.GRAPH3), {4: 5})
        self.assertEqual(in_degree_distribution(self.GRAPH4), {0: 1, 1: 3})
        self.assertEqual(in_degree_distribution(self.GRAPH5), {1: 2, 2: 2, 3: 2, 4: 2})
        self.assertEqual(in_degree_distribution(self.GRAPH6), {1: 1, 2: 6, 3: 1})
        self.assertEqual(in_degree_distribution(self.GRAPH7), {0: 7, 1: 2, 2: 1, 9: 2, 10: 1, 11: 1, 12: 1})


              
# let's run it in IDLE
if __name__ == '__main__':
    unittest.main(exit=False)
