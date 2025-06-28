import os

# Default file for the initial pattern
DEFAULT_PATTERN_FILE = 'pattern.txt'

# Simulation parameters
TIME_STEP = 1000  # Milliseconds between generations
MAX_GENERATIONS = 1000

# Screen and cell colors
SCREEN_BG_COLOR = "white"
CELL_COLOR = "black"
CELL_SIZE = 20  # Pixels



def load_initial_pattern(file_path=None):
    """
    Loads the initial pattern from a specified file or the default file.
    If the default file does not exist, it creates it with a glider pattern.

    Args:
        file_path (str, optional): The path to the pattern file. 
                                   If None, uses DEFAULT_PATTERN_FILE.

    Returns:
        list[list[int]]: A 2D list representing the initial state of the grid.
    """
    if file_path is None:
        file_path = DEFAULT_PATTERN_FILE

    # Create the default file with a glider if it doesn't exist
    if not os.path.exists(file_path) and file_path == DEFAULT_PATTERN_FILE:
        with open(DEFAULT_PATTERN_FILE, 'w') as f:
            f.write("010\n001\n111\n")

    grid = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    grid.append([int(char) for char in line])
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the path.")
        return None
    except ValueError:
        print(f"Error: The file '{file_path}' contains non-numeric characters.")
        return None
        
    return grid
