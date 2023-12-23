import pygame as pg
from time import sleep

pg.init()
win = pg.display.set_mode((600,600))
speed = 1
spd = 1
spdr = 1
spdrin = 1
spider = 1
sped = 1

r = 0
c = 0
x,y = 600,0
xc,yc = 0,0


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    def kvad():
        global r
        global speed
        if r >= 600 or r <= -100:
            speed = -speed
        r += speed
    kvad()

    def cicr():
        global c
        global spd
        if c >= 600 or c <= -100:
            spd = -spd
        c += spd
    cicr()

    def dcic():
        global x,y,spdr,spdrin
        if x >= 600 or x <= 0 and y <= 0 or y >= 600:
            spdrin = spdrin
            spdr = -spdr
        y +=spdrin
        x += spdr
    #-заезжает за границы-#
    dcic()

    def dcic():
        global xc,yc,spider,sped
        if xc >= 0 or xc <= 600 and yc <= 600 or yc >= 0:
            spider = spider
            sped = sped
        yc +=spider
        xc += sped
    #-заезжает за границы-#
    dcic()
#________________________________________________________________________________________________________#
    #diagonal#


    win.fill((255,255,255))
    pg.draw.rect(win,(255,0,0), (r,300, 200,150))
    pg.draw.circle(win,(255,255,0), (300,c), 100)
    pg.draw.circle(win,(0,255,0), (x,y), 100)
    pg.draw.circle(win,(0,0,255), (xc,yc), 100)
    print(x,y)
    pg.display.update()