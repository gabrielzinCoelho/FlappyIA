import pygame
import random
import numpy as np

from constants import *
from neuralNet import NeuralNetwork 

class Bird():

    def __init__(self, displayGame, birdIndex):
        self.displayGame = displayGame
        self.image = pygame.image.load(birdFilePath[birdIndex])
        self.rect = self.image.get_rect()
        self.state = birdAlive
        self.speedY = 0
        self.fitness = 0
        self.timeAlived = 0 #determinar qual pássaro da geração obteve melhor performance e, portanto, deve reproduzir
        self.neuralNet = NeuralNetwork(neuralNetInputs, neuralNetHidden, neuralNetOutput)
        self.setPosition(birdStartX, birdStartY)

    def reset(self):
        self.state = birdAlive
        self.speedY = 0
        self.fitness = 0
        self.timeAlived = 0 
        self.setPosition(birdStartX, birdStartY)

    def setPosition(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y

    def move(self, dt):
        distance = self.speedY * dt + gravity * pow(dt, 2) * 0.5
        self.rect.centery += distance
        self.speedY = self.speedY + gravity * dt

        if self.rect.top < 0:
            self.rect.top = 0
            self.speedY = 0
    
    def flyUp(self, pipes):
        inputs = self.getNeuralNetInputs(pipes)
        if self.neuralNet.getMaxValue(inputs) >= flyUpChance:
            self.speedY = birdFlyUpSpeed

    def draw(self):
        self.displayGame.blit(self.image, self.rect)

    def checkStatus(self, pipes):
        if self.rect.bottom > displayHeight or self.detectCollision(pipes):
            self.state = birdDead
    
    def update(self, dt, pipes):
        if self.state == birdAlive:
            self.timeAlived += dt
            self.move(dt)
            self.flyUp(pipes)
            self.draw()
            self.checkStatus(pipes)

    def assignCollisionFitness(self, pipe):
        gapY = 0
        if pipe.type == pipeUpper:
            gapY = pipe.rect.bottom + pipePairGap/2
        else:
            gapY = pipe.rect.top - pipePairGap/2

        self.fitness = -(abs(self.rect.centery - gapY))

    def detectCollision(self, pipes):
        for pipe in pipes:
            if pipe.rect.colliderect(self.rect):
                self.assignCollisionFitness(pipe)
                return True
        return False

    def getNeuralNetInputs(self, pipes):
        nextPipePositionX = displayWidth * 2
        nextPipePositionY = 0
        for pipe in pipes:
            if(pipe.type == pipeUpper and pipe.rect.right > self.rect.left and pipe.rect.right < nextPipePositionX):
                nextPipePositionX = pipe.rect.right
                nextPipePositionY = pipe.rect.bottom
        distanceX = nextPipePositionX - self.rect.centerx
        distanceY = self.rect.centery - (nextPipePositionY + pipePairGap/2)

        inputs = [
            distanceX/displayWidth * 0.99 + 0.01,
            (distanceY + yShift) / normalizer * 0.99 + 0.01
        ]

        return inputs
    
    def createOffSpring(b1, b2, displayGame, birdIndex):
        newBird = Bird(displayGame, birdIndex)
        newBird.neuralNet.createMixedWeights(b1.neuralNet, b2.neuralNet)
        return newBird


class BirdCollection():

    def __init__(self, displayGame):
        self.birds = []
        self.displayGame = displayGame
        self.createNewGeneration()

    def createNewGeneration(self):
        for i in range(0, generationSize):
            self.birds.append(Bird(self.displayGame, i % len(birdFilePath)))
    
    def update(self, dt, pipes):
        numAlives = 0

        for bird in self.birds:
            bird.update(dt, pipes)
            if bird.state == birdAlive:
                numAlives += 1
        return numAlives

    def evolvePopulation(self):
        for bird in self.birds:
            bird.fitness += bird.timeAlived * sceneSpeed
        
        self.birds.sort(key=lambda x: x.fitness, reverse=True)

        cutOff = int(mutationCutOff * len(self.birds))
        goodBirds = self.birds[0:cutOff]
        badBirds = self.birds[cutOff:]
        numBadToTake = int(mutationBadToKeep * len(self.birds))

        for bird in badBirds:
            bird.neuralNet.modifyWeights()

        newBirds = []

        idxBadToTake = np.random.choice(np.arange(len(badBirds)), numBadToTake, replace=False)

        for index in idxBadToTake:
            newBirds.append(badBirds[index])
        
        newBirds.extend(goodBirds)

        numChildren = len(self.birds) - len(newBirds)

        newBirdIndex = 0

        while len(newBirds) < len(self.birds):
            idxToBreed = np.random.choice(np.arange(len(goodBirds)), 2, replace=False)
            newBird = Bird.createOffSpring(goodBirds[idxToBreed[0]], goodBirds[idxToBreed[1]], self.displayGame, newBirdIndex % len(birdFilePath))
            if random.random() < mutationModifyChanceLimit:
                newBird.neuralNet.modifyWeights()
            newBirds.append(newBird)
            newBirdIndex += 1
        
        for bird in newBirds:
            bird.reset()

        self.birds = newBirds
    