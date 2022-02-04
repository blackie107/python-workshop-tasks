import pygame
import numpy as np

color_about_to_die = (200, 100, 125)
color_alive = (100, 120, 200)
color_background = (250, 250, 250)
color_grid = (100, 100, 100)


def update(surface, current_cells, cell_size):
    next_step = np.zeros((current_cells.shape[0], current_cells.shape[1]))

    for row, column in np.ndindex(current_cells.shape):
        num_alive = np.sum(current_cells[row - 1:row + 2, column - 1:column + 2]) - current_cells[row, column]

        if current_cells[row, column] == 1 and num_alive < 2 or num_alive > 3:
            next_cell_color = color_about_to_die
        elif (current_cells[row, column] == 1 and 2 <= num_alive <= 3) or (current_cells[row, column] == 0 and num_alive == 3):
            next_step[row, column] = 1
            next_cell_color = color_alive

        next_cell_color = next_cell_color if current_cells[row, column] == 1 else color_background
        pygame.draw.rect(surface, next_cell_color, (column * cell_size, row * cell_size, cell_size - 1, cell_size - 1))

    return next_step


def init(dimension_x, dimension_y):
    cells = np.zeros((dimension_y, dimension_x))
    pattern = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
    pos = (30, 30)
    cells[pos[0]:pos[0] + pattern.shape[0], pos[1]:pos[1] + pattern.shape[1]] = pattern
    return cells


def main(dimension_x, dimension_y, cell_size):
    pygame.init()
    surface = pygame.display.set_mode((dimension_x * cell_size, dimension_y * cell_size))
    pygame.display.set_caption("Game of Life in Python")

    cells = init(dimension_x, dimension_y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        surface.fill(color_grid)
        cells = update(surface, cells, cell_size)
        pygame.display.update()


if __name__ == "__main__":
    main(100, 80, 12)
