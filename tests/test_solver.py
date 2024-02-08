# This will work if ran from the root folder ensae-prog24
import sys 
sys.path.append("swap_puzzle/")

import unittest 
from grid import Grid
from solver import Solver

class Test_Solver(unittest.TestCase):
    def tets_solver_grid1(self):
        grid = Grid.grid_from_file("input/grid1.in")
        solution = Solver.get_solution(grid)
        self.assertTrue(grid.is_sorted())
    
    def tets_solver_grid2(self):
        grid = Grid.grid_from_file("input/grid2.in")
        solution = Solver.get_solution(grid)
        self.assertTrue(grid.is_sorted())
    
    def tets_solver_grid3(self):
        grid = Grid.grid_from_file("input/grid3.in")
        solution = Solver.get_solution(grid)
        self.assertTrue(grid.is_sorted())
    
    def tets_solver_grid4(self):
        grid = Grid.grid_from_file("input/grid4.in")
        solution = Solver.get_solution(grid)
        self.assertTrue(grid.is_sorted())

if __name__ == '__main__':
    unittest.main()