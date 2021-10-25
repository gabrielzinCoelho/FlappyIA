import pygame
import random
from constants import *

class Pipe():

    def __init__(self, displayGame, x, y, pipeType):
        self.displayGame = displayGame
        self.state = pipeMoving
        self.type = pipeType
        self.image = pygame.image.load(pipeFilePath)
        self.rect = self.image.get_rect()
        self.setPosition(x, y)
        print("Pipe is moving")
        
    def setPosition(self, x, y):
        self.rect.left = x
        self.rect.top = y

    def movePosition(self, dx, dy):
        self.rect.centerx += dx
        self.rect.centery += dy
    
    def draw(self):
        self.displayGame.blit(self.image, self.rect)

    def checkStatus(self):
        if self.rect.right < 0:
            self.state = pipeDone
            print("Pipe is done")

    def updatePosition(self, msPerFrame):
        if self.state == pipeMoving:
            self.movePosition((-sceneSpeed * msPerFrame), 0)
            self.draw()
            self.checkStatus()


class PipeCollection():

    def __init__(self, displayGame):
        self.displayGame = displayGame
        self.pipes = []

    def addPipePair(self, x):
        pipeUpperSize = random.randint(pipeMinSize, pipeMaxSize)
        print("Pipe upper size: " + str(pipeUpperSize))
        pipeUpperInstance = Pipe(self.displayGame, x, pipeUpperSize - pipeHeight, pipeUpper)
        pipeLowerInstance = Pipe(self.displayGame, x, pipeUpperSize + pipePairGap, pipeLower)

        self.pipes.append(pipeUpperInstance)
        self.pipes.append(pipeLowerInstance)

    def createNewSet(self):
        print("Configurando cena incial...")
        self.pipes = []
        for i in range(pipeFirstX, displayWidth + 1, pipeSequenceGap):
            self.addPipePair(i)
        
    def updatePipeArray(self, msPerFrame):

        rightMost = 0

        for pipeInstance in self.pipes:

            pipeInstance.updatePosition(msPerFrame)

            if pipeInstance.type == pipeUpper:
                if pipeInstance.rect.left > rightMost:
                    rightMost = pipeInstance.rect.left

        if (displayWidth - pipeSequenceGap) > rightMost:
            self.addPipePair(pipeStartX)

        self.pipes = [p for p in self.pipes if p.state == pipeMoving]