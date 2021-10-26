import numpy
import pygame
import scipy

from constants import *
from pipe import PipeCollection
from bird import BirdCollection

def drawLabel(title, data, font, x, y, displayGame):
    label = font.render(title + " " + data, 1, defaultFontColor)
    displayGame.blit(label, (x, y))

def drawDataLabels(font, displayGame, msPerFrame, gameTime, attempts, numAlives):
    drawLabel("FPS", str(round(1000/msPerFrame, 2)), font, 10, 30, displayGame)
    drawLabel("Game Time", str(round(gameTime/1000, 2)), font, 10, 60, displayGame)
    drawLabel(str(attempts), "Attempt(s)", font, 10, 90, displayGame)
    drawLabel(str(numAlives), "Live bird(s)", font, 10, 120, displayGame)

def startGame():
    pygame.init()
    displayGame = pygame.display.set_mode((displayWidth, displayHeight))
    pygame.display.set_caption("Flappy Bird")

    running = True
    backgroundImage = pygame.image.load(backgroundFilePath)
    labelFont = pygame.font.SysFont("monospace", defaultFontSize)

    clock = pygame.time.Clock()
    msPerFrame = 0
    gameTime = 0
    attempts = 1

    pipeCollectionInstance = PipeCollection(displayGame)
    pipeCollectionInstance.createNewSet()

    birdCollectionInstance = BirdCollection(displayGame)
    birdCollectionInstance.createNewGeneration()

    while running:

        msPerFrame = clock.tick(fps)
        gameTime += msPerFrame

        displayGame.blit(backgroundImage, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    running = False

        pipeCollectionInstance.updatePipeArray(msPerFrame)
        numAlives = birdCollectionInstance.update(msPerFrame, pipeCollectionInstance.pipes)

        if not numAlives:
            gameTime = 0
            pipeCollectionInstance.createNewSet()
            birdCollectionInstance.evolvePopulation()
            attempts += 1

        drawDataLabels(labelFont, displayGame, msPerFrame, gameTime, attempts, numAlives)

        pygame.display.update()

if __name__ == "__main__":
    startGame()
