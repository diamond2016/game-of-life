# diamond2016 game-of-life

import turtle
import sys
from cell import Cell
from gen import Generation
import config

def main():
    """Main function to run the Game of Life simulation."""
    # --- 1. Setup --- 
    # Check for custom pattern file from command-line arguments
    pattern_file = sys.argv[1] if len(sys.argv) > 1 else None

    # Load the initial grid pattern
    initial_grid = config.load_initial_pattern(pattern_file)
    if initial_grid is None:
        return # Exit if the pattern file could not be loaded

    grid_height = len(initial_grid)
    grid_width = len(initial_grid[0])

    # Setup the screen
    screen = turtle.Screen()
    screen.title("Conway's Game of Life")
    screen.bgcolor(config.SCREEN_BG_COLOR)
    # Set screen size based on grid dimensions, with some padding
    screen.setup(width=grid_width * config.CELL_SIZE + 40, 
                 height=grid_height * config.CELL_SIZE + 80)
    screen.tracer(0)  # Turn off automatic screen updates

    # --- 2. Create Grid of Cells ---
    grid_of_cells = []
    for r in range(grid_height):
        row_list = []
        for c in range(grid_width):
            state = initial_grid[r][c]
            cell = Cell(row=r, col=c, state=state)
            row_list.append(cell)
        grid_of_cells.append(row_list)

    # --- 3. Initial Display ---
    for r in range(grid_height):
        for c in range(grid_width):
            grid_of_cells[r][c].display(grid_width, grid_height)
    screen.update()

    # --- 4. Setup Generation Manager and Status Writer ---
    gen_manager = Generation()
    gen_manager._update_stats(initial_grid) # Initialize stats for gen 0

    status_writer = turtle.Turtle()
    status_writer.hideturtle()
    status_writer.penup()
    status_writer.goto(-grid_width * config.CELL_SIZE / 2, grid_height * config.CELL_SIZE / 2 + 20)

    def update_status():
        """Writes the current generation status on the screen."""
        gen_num, live, dead = gen_manager.gen_info()
        status_writer.clear()
        status_writer.write(
            f"Generation: {gen_num} / {config.MAX_GENERATIONS}\nLive: {live} | Dead: {dead}",
            align="left",
            font=("Arial", 12, "normal")
        )

    # --- 5. Simulation Loop ---
    def run_generation():
        """Performs one cycle of the simulation."""
        if gen_manager.generation_number >= config.MAX_GENERATIONS:
            print("Max generations reached. Simulation ended.")
            return

        # Get the current state from the cell objects
        current_grid_state = [[cell.state for cell in row] for row in grid_of_cells]

        # Calculate the next generation
        next_grid_state = gen_manager.next_gen(current_grid_state)

        # Update the cell objects with the new state and display them
        for r in range(grid_height):
            for c in range(grid_width):
                new_state = next_grid_state[r][c]
                grid_of_cells[r][c].set_state(new_state)
                grid_of_cells[r][c].display(grid_width, grid_height)
        
        update_status()
        screen.update() # Update the screen after all cells are drawn

        # Schedule the next generation
        screen.ontimer(run_generation, config.TIME_STEP)

    # --- 6. Exit Condition ---
    def exit_game(x=None, y=None):
        """Closes the turtle graphics window."""
        print("Exit signal received. Closing application.")
        screen.bye()

    screen.listen()
    screen.onkey(exit_game, "Escape")
    screen.onclick(exit_game)  # Exit on mouse click

    # --- 7. Start Simulation ---
    update_status() # Show initial status
    run_generation()  # Start the first generation cycle
    turtle.done() # Keep the window open

if __name__ == "__main__":
    main()
