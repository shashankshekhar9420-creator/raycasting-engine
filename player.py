import pygame
import math
from settings import *

class Player:
    def __init__(self, map):
        self.map = map

        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT /2
        self.radius = 3

        self.collisionRadius = 10

        self.turnDirection = 0
        self.walkDirection = 0
        self.rotationAngle = 0
        self.moveSpeed = 2.5
        self.rotationSpeed = 2 * (math.pi / 180)

    def update(self):
        keys=pygame.key.get_pressed()

        self.turnDirection = 0
        self.walkDirection = 0

        if keys[pygame.K_RIGHT]:
            self.turnDirection = 1
        if keys[pygame.K_LEFT]:
            self.turnDirection = -1
        if keys[pygame.K_UP]:
            self.walkDirection = 1
        if keys[pygame.K_DOWN]:
            self.walkDirection = -1

        moveStep = self.walkDirection * self.moveSpeed
        self.rotationAngle += self.turnDirection * self.rotationSpeed

        new_x = self.x + math.cos(self.rotationAngle) * moveStep
        new_y = self.y + math.sin(self.rotationAngle) * moveStep

        if not self.collidesWithWall(new_x, self.y):
            self.x = new_x
        if not self.collidesWithWall(self.x, new_y):
            self.y = new_y

    def collidesWithWall(self, x, y):
        for dx, dy in [(-self.collisionRadius, 0), (self.collisionRadius, 0),
                       (0, -self.collisionRadius), (0, self.collisionRadius)]:
            if self.map.has_wall_at(x + dx, y + dy):
                return True
        return False

    def render(self, screen):
        pygame.draw.circle(screen, (255,0,0), (self.x, self.y), self.radius)

        pygame.draw.line(screen, (255,0,0), (self.x, self.y), (self.x + math.cos(self.rotationAngle) * 50, self.y + math.sin(self.rotationAngle) * 50))