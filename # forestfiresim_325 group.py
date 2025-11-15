# forestfiresim.py
# Modified for Module 6
# Student: [Mitchel Cotton & Aysa Jordan]
# Course: CSD-325

import random
import os
import time

# Grid settings
WIDTH = 30
HEIGHT = 15
TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # Water feature character

# Colors (for command line output)
COLOR_TREE = '\033[32m'   # Green
COLOR_FIRE = '\033[31m'   # Red
COLOR_EMPTY = '\033[37m'  # White/Gray
COLOR_WATER = '\033[34m'  # Blue
COLOR_RESET = '\033[0m'   # Reset

# Probability settings
GROW_PROB = 0.01
LIGHTNING_PROB = 0.0001

def initialize_forest():
    """Create initial forest grid."""
    forest = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if random.random() <= 0.6:
                row.append(TREE)
            else:
                row.append(EMPTY)
        forest.append(row)
    add_lake(forest)
    return forest

def add_lake(forest):
    """Add a lake (water feature) in the center of the grid."""
    lake_width = WIDTH // 5
    lake_height = HEIGHT // 4
    start_x = WIDTH // 2 - lake_width // 2
    start_y = HEIGHT // 2 - lake_height // 2

    for y in range(start_y, start_y + lake_height):
        for x in range(start_x, start_x + lake_width):
            forest[y][x] = WATER

def display_forest(forest):
    """Display forest grid with colors."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in forest:
        for cell in row:
            if cell == TREE:
                print(COLOR_TREE + TREE + COLOR_RESET, end='')
            elif cell == FIRE:
                print(COLOR_FIRE + FIRE + COLOR_RESET, end='')
            elif cell == WATER:
                print(COLOR_WATER + WATER + COLOR_RESET, end='')
            else:
                print(COLOR_EMPTY + EMPTY + COLOR_RESET, end='')
        print()
    print()

def next_state(forest):
    """Compute next generation of forest based on fire spread and regrowth."""
    new_forest = [row.copy() for row in forest]

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if forest[y][x] == WATER:
                continue  # Water never changes

            elif forest[y][x] == EMPTY:
                if random.random() <= GROW_PROB:
                    new_forest[y][x] = TREE

            elif forest[y][x] == TREE:
                if is_adjacent_fire(forest, x, y) or random.random() <= LIGHTNING_PROB:
                    new_forest[y][x] = FIRE

            elif forest[y][x] == FIRE:
                new_forest[y][x] = EMPTY
    return new_forest

def is_adjacent_fire(forest, x, y):
    """Check for adjacent fire, ignoring water."""
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                if forest[ny][nx] == FIRE:
                    return True
    return False

def main():
    forest = initialize_forest()

    while True:
        display_forest(forest)
        forest = next_state(forest)
        time.sleep(0.2)

if __name__ == '__main__':
    main()
