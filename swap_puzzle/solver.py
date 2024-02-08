from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """

    @staticmethod
    def get_naive_solution(grid: Grid) -> list:
        """
        Solves the grid and returns the sequence of swaps at the format complexité O((n*m)^2)
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 

        Parameters:
        -----------
        grid: Grid
            The grid to solve.

        Returns:
        --------
        list
            A list of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """

        retour = []
        while not grid.is_sorted():
            # on commence par chercher les coordonnées du minimum pas a ca place
            minimum = grid.state[-1][-1]
            i_min = grid.m-1
            j_min = grid.n-1
            for i in range(grid.m):
                for j in range(grid.n):
                    if grid.state[i][j] < minimum and grid.state[i][j] != i*grid.n+j+1:
                        minimum = grid.state[i][j]
                        i_min = i
                        j_min = j

            ligne_visee = (minimum-1)//grid.n
            colonne_visee = (minimum-1)%grid.n
            if i_min != ligne_visee: # si on es pas sur la bonne ligne
                if i_min > ligne_visee: # si on es trop bas
                    grid.swap((i_min, j_min), (i_min-1, j_min))
                    retour.append(((i_min, j_min), (i_min-1, j_min)))
                else: # sinon on es trop haut
                    grid.swap((i_min, j_min), (i_min+1, j_min))
                    retour.append(((i_min, j_min), (i_min+1, j_min)))
            else: # sinon on est sur le bonne ligne
                if j_min > colonne_visee: # il faut aller a gauche
                    grid.swap((i_min, j_min), (i_min, j_min-1))
                    retour.append(((i_min, j_min), (i_min, j_min-1)))
                else: # sinon il faut aller a droite
                    grid.swap((i_min, j_min), (i_min, j_min+1))
                    retour.append(((i_min, j_min), (i_min, j_min+1)))
        return retour
    
    @staticmethod
    def get_bfs_solution(grid: Grid) -> list:
        """
        Solves the grid and returns the sequence of swaps at the format complexité O(n*m)
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 

        Parameters:
        -----------
        grid: Grid
            The grid to solve.

        Returns:
        --------
        list
            A list of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        graph = grid.generate_all_possible_grid()
        src = grid.to_hashable()
        dst = Grid(grid.m, grid.n).to_hashable()
        path = graph.bfs(src, dst)
        solution = Solver.path_to_swaps(path)
        grid.swap_seq(solution)
        return solution 


    @staticmethod
    def path_to_swaps(path: list) -> list:
        """
        Transforms a path from the bfs method to a sequence of swaps. 

        Parameters:
        -----------
        path: list
            A list of nodes from the bfs method.

        Returns:
        --------
        list
            A list of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        solution = []
        for i in range(1, len(path)): # pour chaque element du chemin en partant du deuxieme
            for line in range(len(path[i])): # pour chaque ligne
                for column in range(len(path[i][0])): # pour chaque colonne
                    if path[i][line][column] != path[i-1][line][column]: # si la case a changé
                        # on cherche la case qui a changé
                        for dest_line in range(len(path[i])): # pour chaque ligne
                            for dest_column in range(len(path[i][0])): # pour chaque colonne
                                if path[i][line][column] == path[i-1][dest_line][dest_column]: # on a trouvé la case qui a changé
                                    if not ((dest_line, dest_column), (line, column)) in solution: # si le swap n'est pas déjà dans la solution
                                        solution.append(((line, column), (dest_line, dest_column))) # on sauvegarde le swap
        return solution