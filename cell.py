from turtle import Turtle
from config import CELL_COLOR, CELL_SIZE

class Cell(Turtle):
    """
    Represents a single cell in the Game of Life grid.
    It's a Turtle object that can be shown (alive) or hidden (dead).
    """
    def __init__(self, row, col, state=0):
        """
        Initializes a Cell object.

        Args:
            row (int): The row index of the cell in the grid.
            col (int): The column index of the cell in the grid.
            state (int): The initial state of the cell (0 for dead, 1 for alive).
        """
        super().__init__()
        self.row = row
        self.col = col
        self.state = state
        
        self.shape("square")
        self.color(CELL_COLOR)
        self.penup()  # Don't draw lines when moving
        self.speed(0)  # Fastest drawing speed
        self.shapesize(stretch_wid=CELL_SIZE / 20, stretch_len=CELL_SIZE / 20)

    def display(self, grid_width, grid_height):
        """
        Calculates the cell's position on the screen and displays it.
        The cell is positioned relative to the center of the grid.

        Args:
            grid_width (int): The total width of the grid (number of columns).
            grid_height (int): The total height of the grid (number of rows).
        """
        # Calculate the top-left corner of the grid to center it
        start_x = - (grid_width / 2) * CELL_SIZE
        start_y = (grid_height / 2) * CELL_SIZE

        # Calculate the specific coordinates for this cell
        x = start_x + self.col * CELL_SIZE + CELL_SIZE / 2
        y = start_y - self.row * CELL_SIZE - CELL_SIZE / 2
        
        self.goto(x, y)
        
        if self.state == 1:
            self.showturtle()
        else:
            self.hideturtle()

    def set_state(self, new_state):
        """
        Updates the state of the cell.

        Args:
            new_state (int): The new state (0 or 1).
        """
        self.state = new_state
