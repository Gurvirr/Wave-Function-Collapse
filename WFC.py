""" Wave Function Collapse Algorithm """

import random, pygame as py
from connectivity.T import connectivity # Swap connectivity grid: C, S, T

# Pygame setup
py.init()
py.display.set_caption("Wave Function Collapse Algorithm")
clock = py.time.Clock()

pxl = 30
grid_w = 64
grid_h = 36

direc = "assets/30/"
run_program = True
screen = py.display.set_mode((grid_w * pxl, grid_h * pxl))

first_row = []
for i in range(grid_w):
    if i == 0:
        first_tile = random.choice(list(connectivity.keys()))
    else:
        entropy_tile = random.choice(list(connectivity.keys()))
        while connectivity[first_row[i - 1]]["right"] != connectivity[entropy_tile]["left"]:
            entropy_tile = random.choice(list(connectivity.keys()))
        else:
            first_tile = entropy_tile
    first_row.append(first_tile)

matrix = [first_row]

for row in range(grid_h - 1):
    subseq_row = []
    for col in range(grid_w):
        if col == 0:
            first_tile = random.choice(list(connectivity.keys()))
            while connectivity[first_tile]["up"] != connectivity[matrix[row][col]]["down"]:
                first_tile = random.choice(list(connectivity.keys()))
        else:
            entropy_tile = random.choice(list(connectivity.keys()))
            while connectivity[entropy_tile]["up"] != connectivity[matrix[row][col]]["down"] or connectivity[subseq_row[col - 1]]["right"] != connectivity[entropy_tile]["left"]:
                entropy_tile = random.choice(list(connectivity.keys()))
            else:
                first_tile = entropy_tile   
        subseq_row.append(first_tile)

    matrix += [subseq_row]
    
while run_program:
    for row in range(grid_h):
        for col in range(grid_w):
            screen.blit(py.image.load(direc + matrix[row][col] + ".png"), (col * pxl, row * pxl))
            
    for event in py.event.get():
        if event.type == py.QUIT:
            run_program = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                run_program = False

    py.display.update()
    clock.tick(100)

py.quit()