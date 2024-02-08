# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver

class Test_Solver(unittest.TestCase):
    def test_solver_grid1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        solution = Solver.get_naive_solution(grid)
        self.assertTrue(grid.is_sorted())
    
    def test_solver_grid2(self):
        grid = Grid.grid_from_file("input/grid2.in")
        solution = Solver.get_naive_solution(grid)
        self.assertTrue(grid.is_sorted())
    
    def test_solver_grid3(self):
        grid = Grid.grid_from_file("input/grid3.in")
        solution = Solver.get_naive_solution(grid)
        self.assertTrue(grid.is_sorted())
    
    def test_solver_grid4(self):
        grid = Grid.grid_from_file("input/grid4.in")
        solution = Solver.get_naive_solution(grid)
        self.assertTrue(grid.is_sorted())

    def test_solver_bfs(self):
        grid = Grid.grid_from_file("input/grid2.in")
        solution = Solver.get_bfs_solution(grid)
        self.assertTrue(grid.is_sorted())

    def test_solver_bfs_optimized(self):
        grid = Grid.grid_from_file("input/grid2.in")
        solution = Solver.get_bfs_optimized_solution(grid)
        self.assertTrue(grid.is_sorted())

if __name__ == '__main__':
    unittest.main()