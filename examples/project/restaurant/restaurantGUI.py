import sgc
from sgc.locals import *

import pygame
from pygame.locals import *


class RestaurantButton(sgc.Button):
    def gameInit(self):
        self.on = False
        self.config_set = False

    def on_click(self):
        self.message = "This is the text"
        self.on = True

pygame.init()
pygame.display.init()
pygame.font.init()

PURPLE = (199, 46, 245)
MINT = (193, 248, 230)

screen = sgc.surface.Screen((800, 600))

clock = pygame.time.Clock()

fontOhio = pygame.font.Font("fnt/ohio.ttf", 30)
fontLarge = pygame.font.Font("fnt/ohio.ttf", 52)

btn = RestaurantButton(label="Capitola",
                       label_font=fontOhio,
                       label_col=MINT,
                       col=PURPLE,
                       pos=(100, 100))

btn.gameInit()

label = sgc.Label(pos=(100, 200),
                  col=(255, 255, 255),
                  text="this is the text",
                  font=fontLarge)

btn.add(0)
# label.add()

while True:
    time = clock.tick(30)

    for event in pygame.event.get():
        sgc.event(event)
        if event.type == QUIT:
            exit()
 
    sgc.update(time)
    if btn.on:
        if not btn.config_set:
            label.text = str(pygame.time.get_ticks())
            label.add()
            btn.config_set = True
    screen.fill((0, 0, 0))
    sgc.update(time)
    pygame.display.flip()