import pygame
import random
import constants
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen,(255, 255, 255), (self.position[0], self.position[1]), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        velocity1 = self.velocity.rotate(angle)
        velocity2 = self.velocity.rotate(-angle)

        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)

        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2