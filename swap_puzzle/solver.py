from grid import Grid

class Solver(): 
    """
    A solver class, to be implemented.
    """

    @staticmethod
    def get_solution(grid: Grid) -> list:
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