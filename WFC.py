""" Wave Function Collapse Algorithm """

import random, pygame as py, time
from Connectivity.C import connectivity # Swap connectivity grid: C, S, T

py.init()
py.display.set_caption("Wave Function Collapse Algorithm")
clock = py.time.Clock()

pxl = 30
grid_w, grid_h = 64, 36
direc = "Assets/30/"
active = True
screen = py.display.set_mode((grid_w * pxl, grid_h * pxl))

first_row = []
for col in range(grid_w):
    if col == 0:
        tile = random.choice(list(connectivity.keys()))
    else:
        entropy_tile = random.choice(list(connectivity.keys()))
        while connectivity[first_row[col - 1]]["right"] != connectivity[entropy_tile]["left"]:
            entropy_tile = random.choice(list(connectivity.keys()))
        else:
            tile = entropy_tile
    first_row.append(tile)

matrix = [first_row]

for row in range(grid_h - 1):
    subseq_row = []
    for col in range(grid_w):
        if col == 0:
            tile = random.choice(list(connectivity.keys()))
            while connectivity[tile]["up"] != connectivity[matrix[row][col]]["down"]:
                tile = random.choice(list(connectivity.keys()))
        else:
            entropy_tile = random.choice(list(connectivity.keys()))
            while connectivity[entropy_tile]["up"] != connectivity[matrix[row][col]]["down"] or connectivity[subseq_row[col - 1]]["right"] != connectivity[entropy_tile]["left"]:
                entropy_tile = random.choice(list(connectivity.keys()))
            else:
                tile = entropy_tile
        subseq_row.append(tile)

    matrix += [subseq_row]

while active:
    for row in range(grid_h):
        for col in range(grid_w):
            screen.blit(py.image.load(direc + matrix[row][col] + ".png"), (col * pxl, row * pxl))
            py.display.update()

    for event in py.event.get():
        if event.type == py.QUIT:
            active = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                active = False
            if event.key == py.K_v:
                filename = ("Captures/Capture " + time.strftime("%Y-%H.%M.%S") + ".png")
                py.image.save(screen, filename)

    clock.tick(100)

py.quit()