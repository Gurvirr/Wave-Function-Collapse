import sys
import random
import pygame as py

# Pygame setup
py.init()
py.display.set_caption("Wave Function Collapse")
clock = py.time.Clock()

pxl = 64
Running = True
screen = py.display.set_mode((640, 640))

A0 = py.image.load("A0.png")
A1 = py.image.load("A1.png")
A2 = py.image.load("A2.png")
A3 = py.image.load("A3.png")
A4 = py.image.load("A4.png")

grid = [["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""],
        ["","","","","","","","","",""]]

for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        rng = random.randint(0, 4)
        if rng == 0:
            grid[y].insert(x, "A0")
        elif rng == 1:
            grid[y].insert(x, "A1") 
        elif rng == 2:
            grid[y].insert(x, "A2")
        elif rng == 3:
            grid[y].insert(x, "A3")
        elif rng == 4:
            grid[y].insert(x, "A4")
    
for x in range(0, len(grid)):
    print("".join(grid[x]))

while Running:
    screen.fill((59,75,91))
  
    y = 0

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == "A0":
                screen.blit(A0, (x * pxl, y * pxl))
            if grid[y][x] == "A1":
                screen.blit(A1, (x * pxl, y * pxl))
            if grid[y][x] == "A2":
                screen.blit(A2, (x * pxl, y * pxl))
            if grid[y][x] == "A3":
                screen.blit(A3, (x * pxl, y * pxl))
            if grid[y][x] == "A4":
                screen.blit(A4, (x * pxl, y * pxl))
                
# game loop and key input presses
    for event in py.event.get():
        if event.type == py.QUIT:
            Running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                Running = False

    py.display.update()
    clock.tick(74)
    
py.quit()