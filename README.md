# Conway's Game of Life
- Specifics and requirement: diamond2016
- Elaborated by: gemini-cli

## 1. Project Overview

This project aims to create a Python application to simulate and visualize Conway's Game of Life. The application will display the evolution of cell generations on a grid based on the rules of the game.

## 2. Key Technologies

- **Language:** Python
- **UI Library (Turtle):**
- **Core Logic:** Standard Python libraries


## 3. Project Structure

- `main.py`: The main entry point of the application.
- `gen.py `: Contains the core logic for the Game of Life simulation (e.g., calculating the next generation).
- `config.py`: Allows to load initial configuration of cells (load from external file the) and manage other configuration 
- `cell.py`: contains single cell clas to display
- `README.md`: Project documentation.
- `requirements.txt`: Project dependencies.

## 4. Development Workflow

main.py 
- creates screen with Screen of Turtle;
- creates grid: bidimensiona listi of cells, all of class Cell(Turtle); 
- calls config.py (load_initial_pattern): reads from external file initial pattern (see pattern.txt): 1 live, 0 dead. 
  computes m and n of grid based on number rows and dimension of columns in file
- use Cell functions to visualize grid

loop
    - computes new generation (Generation())
    - updates cell state (Cell())
    - displays cells
    - display info on generation on topo screen (gen nr., lives, deads)

- listen key ESC or mouse click to exit from LOOP

cell.py
class cell (Turtle)
contains the attribute state (1/0), and also row and col which are the row and column number of the cell in grid (the list of the main)
it is an object with shape "circle", color "black", default size 20 pixels
- defines a function display(width, Height) that receives the dimensions of the screen and calculates the coordinates on the screen to display the cell through its internal attributes
self.row and self.col
- the function display() uses self.hideturtle() if self.state = 0 or self.showturtle if self.state = 1

gen.py
This class exposes the next_gen(grid) function which:
- calculates the behavior of all grid cells according to the four rules of game-of-life:
Any live cell with fewer than two adjacent live cells dies, as if by isolation;
Any live cell with two or three adjacent live cells survives to the next generation;
Any live cell with more than three adjacent live cells dies, as if by overpopulation;
Any dead cell with exactly three adjacent live cells becomes a live cell, as if by reproduction.
- keeps internally in a list, for each generation: the number of living and dead cells, the generation number (progressive from 1), the configuration state of each generation (bit mask of all rows and columns of the grid)
- provides a function: gen_info() for the data to be presented by main on the screen: generation number, the number of living and dead cells



config.py
exposes the service to load the initial pattern
if the file does not exist a default file, to be created: pattern.txt (glider)
contains the time parameters (default 1 second), maximum number of generations (default 1000), screen background color (default white), cell color (default black) that the main will use in its cycle

### Setup

1.  Clone the repository.

### Running the Application

bash
python main.py initial_pattern.txt (if file not exists will use: pattern.txt)
