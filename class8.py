import pgzrun
from random import randint
from time import time

WIDTH = 600
HEIGHT = 400

satellites = []
line = []
next_satellite = 0

start_time = 0
total_time = 0
end_time = 0

n = 8

def create_satellites():
    global start_time
    for i in range(0,n):
        satellite = Actor("satellite")
        satellite.pos = randint(40, WIDTH - 40), randint(40, HEIGHT-40)
        satellites.append(satellite)
    start_time = time()

def draw():
    global total_time

    screen.blit("starrynight", (0,0))
    number = 1
    for satellite in satellites:
        screen.draw.text(str(number), satellite.pos[0], satellite.pos[1]+20)
        satellite.draw()
        number = number+1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_satellite<n:
        total_time = time()-start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)
        

create_satellites()
pgzrun.go()