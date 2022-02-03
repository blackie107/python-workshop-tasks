import pygame
import time

color_about_to_die = (200, 100, 125)
color_alive = (100, 120, 200)
color_background = (250, 250, 250)
color_grid = (100, 100, 100)


def update(surface, current_cells, cell_size):
    dimension_x = len(current_cells[0])
    dimension_y = len(current_cells)

    # Hinweis: mit pygame reicht diese Zeile, um alles zu zeichnen (jeweils eine Zelle)
    # pygame.draw.rect(surface, Zellen-Farbe (siehe Tupel ganz oben), (x-Koordinate , y-Koordinate, Breite, Höhe))

    # return Neues Zellen-Array


def init(dimension_x, dimension_y):
    print('Dimensions are ' + str(dimension_x) + ' ' + str(dimension_y))

    cells = [0 for y in range(dimension_y)]
    for i in range(len(cells)):
        cells[i] = [0 for x in range(dimension_x)]

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
