# This will work if ran from the root folder ensae-prog24
import sys 
import ast
sys.path.append("swap_puzzle/")

import unittest 
from graph import Graph

class Test_Solver(unittest.TestCase):
    def test_graph1_bfs(self):
        self.bfs_for_file("input/graph1.in", "input/graph1.path.out")

    def test_graph2_bfs(self):
        self.bfs_for_file("input/graph2.in", "input/graph2.path.out")
    
    def bfs_for_file(self, input, out):
        g = Graph.graph_from_file(input)
        with open (out) as f:
            lines = f.readlines()
            for line in lines:
                splited = line.split()
                src = ast.literal_eval(splited[0])
                dst = ast.literal_eval(splited[1])
                length = ast.literal_eval(splited[2])
                if len(splited) > 3:
                    joined = ''.join(splited[3:])
                    path = ast.literal_eval(joined)
                    self.assertEqual(g.bfs(src, dst), path)
                else:
                    self.assertEqual(g.bfs(src, dst), None)
        

if __name__ == '__main__':
    unittest.main()