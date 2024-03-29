"""
This is the grid module. It contains the Grid class and its associated methods.
"""

from matplotlib import pyplot as plt
from itertools import permutations
from graph import Graph

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

  
        
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
   
    def is_sorted(self):
        L = []
        for i in range(self.m):
            L = L + self.state[i]
        for k in range(len(L)-1):
            if L[k] > L[k+1]:
                return False
        return True

    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        if cell1[0] == cell2[0]:
            if cell1[1] == cell2[1] or cell1[1] == cell2[1]+1 or cell1[1] == cell2[1]-1:
                self.state[cell1[0]][cell1[1]], self.state[cell2[0]][cell2[1]] = self.state[cell2[0]][cell2[1]], self.state[cell1[0]][cell1[1]]
        elif cell1[1] == cell2[1]:
            if cell1[0] == cell2[0] or cell1[0] == cell2[0]+1 or cell1[0] == cell2[0]-1:
                self.state[cell1[0]][cell1[1]], self.state[cell2[0]][cell2[1]] = self.state[cell2[0]][cell2[1]], self.state[cell1[0]][cell1[1]]
        else:
            raise Exception(f"Cells {cell1} and {cell2} are not adjacent and cannot be swapped.")


        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
       
    def swap_seq(self, cell_pair_list):
        for k in range(len(cell_pair_list)):
            self.swap(cell_pair_list[k][0], cell_pair_list[k][1])


    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid

    def display(self):
        """
        Displays the grid using matplotlib
        """
        _, ax = plt.subplots()
        ax.matshow(self.state, cmap='viridis')
        for i in range(self.m):
            for j in range(self.n):
                ax.text(j, i, str(self.state[i][j]), va='center', ha='center')
        plt.show()

    def to_hashable(self):
        """
        Returns a hashable representation of the grid. 
        """
        return tuple([tuple(line) for line in self.state])

    @staticmethod
    def from_hashable(hashable_state: tuple):
        """
        Convert a hashable grid state (tuple of tuples) to a list of lists.
        """
        content = [list(row) for row in hashable_state]
        m = len(content)
        n = len(content[0])
        return Grid(m, n, content)
    
    def generate_all_possible_grid(self) -> Graph:
        """
        Generates all possible grids that can be obtained from the current grid.
        """
        # generate all possible grids with content 1,2,3,4,5,6,7,8,...
        grids = []
        items = list(range(1, self.m*self.n+1))
        for p in permutations(items):
            grids.append(Grid(self.m, self.n, [list(p[i*self.n:(i+1)*self.n]) for i in range(self.m)]))
        
        # create a graph with all the possible grids
        graph = Graph([grid.to_hashable() for grid in grids])

        # add edges between the grids that can be obtained from each other by a single swap
        for i in range(len(grids)): # pour toute les grilles
            for line in range(self.m): # pour toute les lignes
                for column in range(self.n): # pour toute les colonnes
                    for line_add, column_add in [(0, 1), (1, 0), (-1, 0), (0, -1)]: # pour toute les operation possible
                        if 0 <= line+line_add < self.m and 0 <= column+column_add < self.n: # si la case est dans la grille
                            hashable = grids[i].to_hashable()
                            grids[i].swap((line, column), (line+line_add, column+column_add))
                            graph.add_edge(hashable, grids[i].to_hashable())
        return graph
    
    def generate_neighbours(self) -> list:
        """
        Generates the neighbours of the grid. 
        """
        result = []
        for line in range(self.m):
            for column in range(self.n):
                for line_add, column_add in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if 0 <= line+line_add < self.m and 0 <= column+column_add < self.n:
                        new_grid = Grid(self.m, self.n, [list(row) for row in self.state])
                        new_grid.swap((line, column), (line+line_add, column+column_add))
                        new_grid_hashable = new_grid.to_hashable()
                        if new_grid_hashable not in result:
                            result.append(new_grid_hashable)
        return result