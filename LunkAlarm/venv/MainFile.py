import pygame
from pygame.locals import *
pygame.init()

DISPLAYSURF = pygame.display.set_mode([1000,1000])
pygame.display.set_caption('Lunk Alarm!')
playerSprite = pygame.image.load("/Users/andrewwu/PycharmProjects/LunkAlarm/venv/lib/Chad.png")

class PlanetFitnessGuard:
    def __init__(self, guardx, guardy):
        self.guardx = guardx
        self.guardy = guardy

class Player:
    def __init__(self, playerX, playerY):
        self.playerX = playerX
        self.playerY = playerY

    def draw(self):
        DISPLAYSURF.blit(playerSprite, (self.playerX, self.playerY))

    def moveXLeft(self):

        self.playerX -= 5

    def moveXRight(self):

        self.playerX += 5

    def moveYUp(self):

        self.playerY -= 5

    def moveYDown(self):

        self.playerY += 5
    #def interact(self):

player = Player(0,0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                player.moveXLeft()
            elif event.key == K_d:
                player.moveXRight()
            elif event.key == K_w:
                player.moveYUp()
            elif event.key == K_s:
                player.moveYDown()
    DISPLAYSURF.fill((255, 255, 255))
    player.draw()
    pygame.display.flip()

