"""
prompt:
please write a Python script to create an animated starfield simulating zooming through space
"""
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Starfield Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Star class
class Star:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = random.uniform(-WIDTH/2, WIDTH/2)
        self.y = random.uniform(-HEIGHT/2, HEIGHT/2)
        self.z = random.uniform(0, WIDTH)
        self.pz = self.z

    def update(self, speed):
        self.z -= speed
        if self.z < 1:
            self.reset()

    def show(self):
        sx = int((self.x / self.z) * WIDTH + WIDTH / 2)
        sy = int((self.y / self.z) * HEIGHT + HEIGHT / 2)

        r = int((1 - self.z / WIDTH) * 5)
        pygame.draw.circle(screen, WHITE, (sx, sy), r)

        px = int((self.x / self.pz) * WIDTH + WIDTH / 2)
        py = int((self.y / self.pz) * HEIGHT + HEIGHT / 2)
        self.pz = self.z

        pygame.draw.line(screen, WHITE, (px, py), (sx, sy), 1)

# Create a list of stars
num_stars = 200
stars = [Star() for _ in range(num_stars)]

# Speed of the stars
speed = 10

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update stars
    for star in stars:
        star.update(speed)

    # Draw stars
    screen.fill(BLACK)
    for star in stars:
        star.show()

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
