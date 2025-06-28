import copy

class Generation:
    """
    Manages the state and evolution of the Game of Life generations.
    """
    def __init__(self):
        """
        Initializes the generation manager.
        """
        self.generation_number = 0
        self.live_cells_count = 0
        self.dead_cells_count = 0
        self.history = []

    def next_gen(self, grid):
        """
        Calculates the next generation of the grid based on the rules of the game.

        Args:
            grid (list[list[int]]): The current state of the grid.

        Returns:
            list[list[int]]: The grid representing the next generation.
        """
        if not grid or not grid[0]:
            return []

        rows = len(grid)
        cols = len(grid[0])
        # Create a new grid for the next generation, initialized to all dead
        new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                live_neighbors = self._count_live_neighbors(grid, r, c)
                current_state = grid[r][c]

                # Apply the rules of the Game of Life
                if current_state == 1:  # Cell is alive
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[r][c] = 0  # Dies
                    else:
                        new_grid[r][c] = 1  # Survives
                else:  # Cell is dead
                    if live_neighbors == 3:
                        new_grid[r][c] = 1  # Becomes alive

        # Update statistics for the new generation
        self.generation_number += 1
        self._update_stats(new_grid)
        self.history.append(copy.deepcopy(new_grid))

        return new_grid

    def _count_live_neighbors(self, grid, r, c):
        """Counts the live neighbors for a given cell."""
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        # Iterate over the 8 neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # Skip the cell itself

                neighbor_r, neighbor_c = r + i, c + j

                # Check boundaries
                if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols:
                    count += grid[neighbor_r][neighbor_c]
        return count

    def _update_stats(self, grid):
        """Updates the count of live and dead cells."""
        if not grid or not grid[0]:
            self.live_cells_count = 0
            self.dead_cells_count = 0
            return
            
        rows = len(grid)
        cols = len(grid[0])
        live_count = sum(row.count(1) for row in grid)
        self.live_cells_count = live_count
        self.dead_cells_count = rows * cols - live_count

    def gen_info(self):
        """
        Returns statistics for the current generation.

        Returns:
            tuple: (generation_number, live_cells_count, dead_cells_count)
        """
        return (self.generation_number, self.live_cells_count, self.dead_cells_count)
