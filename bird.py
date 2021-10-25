import pygame

from constants import *

class Bird():

    def __init__(self, displayGame):
        self.displayGame = displayGame
        self.image = pygame.image.load(birdFilePath)
        self.rect = self.image.get_rect()
        self.state = birdAlive
        self.speedY = 0
        self.timeAlived = 0 #determinar qual pássaro da geração obteve melhor performance e, portanto, deve reproduzir
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
    
    def flyUp(self):
        self.speedY = birdFlyUpSpeed

    def draw(self):
        self.displayGame.blit(self.image, self.rect)

    def checkStatus(self, pipes):
        if self.rect.bottom > displayHeight or self.detectCollision(pipes):
            self.state = birdDead
            print("Bird died")
    
    def update(self, dt, pipes):
        if self.state == birdAlive:
            self.timeAlived += dt
            self.move(dt)
            self.draw()
            self.checkStatus(pipes)

    def detectCollision(self, pipes):
        for pipe in pipes:
            if pipe.rect.colliderect(self.rect):
                return True
        return False