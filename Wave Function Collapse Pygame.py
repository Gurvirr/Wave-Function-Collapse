''' Wave Function Collapse Algorithm '''

import sys, random, pygame as py

# Pygame setup
py.init()
py.display.set_caption("Wave Function Collapse")
clock = py.time.Clock()

pxl = 64
grid_w = 10
grid_h = 10

run_program = True
screen = py.display.set_mode((grid_w * pxl, grid_h * pxl))

images = {
    "A0": "A0.png",
    "A1": "A1.png",
    "A2": "A2.png",
    "A3": "A3.png",
    "A4": "A4.png"
}

grid_2D = [[random.choice(list(images)) for _ in range(grid_w)] for _ in range(grid_h)]

for x in range(0, len(grid_2D)):
     print("".join(grid_2D[x]))

# Program loop
while run_program:
    screen.fill((59, 75, 91))
    for y in range(grid_h):
        for x in range(grid_w):
            image = images.get(grid_2D[y][x])
            if image:
                screen.blit(py.image.load(image), (x * pxl, y * pxl))

    for event in py.event.get():
        if event.type == py.QUIT:
            run_program = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                run_program = False

    py.display.update()
    clock.tick(74)

py.quit()
