import numpy
import pygame
import scipy

from constants import *
from pipe import PipeCollection

def drawLabel(title, data, font, x, y, displayGame):
    label = font.render(title + " " + data, 1, defaultFontColor)
    displayGame.blit(label, (x, y))

def drawDataLabels(font, displayGame, msPerFrame, gameTime):
    drawLabel("FPS", str(round(1000/msPerFrame, 2)), font, 10, 30, displayGame)
    drawLabel("Game Time", str(round(gameTime/1000, 2)), font, 10, 60, displayGame)

def startGame():
    pygame.init()
    displayGame = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption("Flappy Bird")

    running = True
    backgroundImage = pygame.image.load(backgroundFilePath)
    birdImage = pygame.image.load(birdFilePath)
    labelFont = pygame.font.SysFont("monospace", defaultFontSize)

    clock = pygame.time.Clock()
    msPerFrame = 0
    gameTime = 0

    pipeCollectionInstance = PipeCollection(displayGame)
    pipeCollectionInstance.createNewSet()

    while running:

        msPerFrame = clock.tick(fps)
        gameTime += msPerFrame

        displayGame.blit(backgroundImage, (0, 0))
        displayGame.blit(birdImage, (100, displayHeight - 100))

        pipeCollectionInstance.updatePipeArray(msPerFrame)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False

        drawDataLabels(labelFont, displayGame, msPerFrame, gameTime)

        pygame.display.update()

if __name__ == "__main__":
    startGame()
