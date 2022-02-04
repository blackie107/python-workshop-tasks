import pygame
import time

color_about_to_die = (200, 100, 125)
color_alive = (100, 120, 200)
color_background = (250, 250, 250)
color_grid = (100, 100, 100)


def update(surface, current_cells, cell_size):
    dimension_x = len(current_cells[0])
    dimension_y = len(current_cells)

    next_step = [0 for y in range(dimension_y)]
    for i in range(dimension_y):
        next_step[i] = [0 for x in range(dimension_x)]

    for y in range(dimension_y - 1):
        for x in range(dimension_x - 1):

            neighbours_alive_count = 0

            if current_cells[y][x - 1] == 1:
                neighbours_alive_count += 1
            if current_cells[y][x + 1] == 1:
                neighbours_alive_count += 1

            if current_cells[y - 1][x] == 1:
                neighbours_alive_count += 1
            if current_cells[y + 1][x] == 1:
                neighbours_alive_count += 1

            if current_cells[y - 1][x - 1] == 1:
                neighbours_alive_count += 1
            if current_cells[y + 1][x - 1] == 1:
                neighbours_alive_count += 1

            if current_cells[y - 1][x + 1] == 1:
                neighbours_alive_count += 1
            if current_cells[y + 1][x + 1] == 1:
                neighbours_alive_count += 1

            if current_cells[y][x] == 1 and neighbours_alive_count < 2 or neighbours_alive_count > 3:
                next_cell_color = color_about_to_die
            elif (current_cells[y][x] == 1 and 2 <= neighbours_alive_count <= 3) or (current_cells[y][x] == 0 and neighbours_alive_count == 3):
                next_step[y][x] = 1
                next_cell_color = color_alive

            next_cell_color = next_cell_color if current_cells[y][x] == 1 else color_background
            pygame.draw.rect(surface, next_cell_color, (x * cell_size, y * cell_size, cell_size - 1, cell_size - 1))

    return next_step


def init(dimension_x, dimension_y):
    print('Dimensions are ' + str(dimension_x) + ' ' + str(dimension_y))

    cells = [0 for y in range(dimension_y + 1)]
    for i in range(len(cells)):
        cells[i] = [0 for x in range(dimension_x + 1)]

    print('Dimensions of array are ' + str(len(cells[0])) + ' ' + str(len(cells)))

    pattern = [
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    ]
    pos = (30, 30)
    for y in range(len(pattern)):
        for x in range(len(pattern[0])):
            cells[pos[0] + y][pos[1] + x] = pattern[y][x]

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

        time.sleep(0.1)


if __name__ == "__main__":
    main(100, 80, 12)
