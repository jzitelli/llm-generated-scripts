"""
prompt:
please write a Python script to create an animated starfield simulating zooming through space
"""
import pygame
import random
import math

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

# Number of stars
NUM_STARS = 300

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Starfield Simulation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Star class
class Star:
    def __init__(self):
        self.x = random.uniform(-CENTER_X, CENTER_X)
        self.y = random.uniform(-CENTER_Y, CENTER_Y)
        self.z = random.uniform(1, SCREEN_WIDTH)

    def update(self, speed):
        self.z -= speed
        if self.z <= 0:
            self.z = random.uniform(1, SCREEN_WIDTH)
            self.x = random.uniform(-CENTER_X, CENTER_X)
            self.y = random.uniform(-CENTER_Y, CENTER_Y)

    def draw(self, surface):
        sx = int(CENTER_X + self.x / self.z * SCREEN_WIDTH)
        sy = int(CENTER_Y + self.y / self.z * SCREEN_HEIGHT)
        radius = max(1, int((SCREEN_WIDTH - self.z) / SCREEN_WIDTH * 5))
        if 0 <= sx < SCREEN_WIDTH and 0 <= sy < SCREEN_HEIGHT:
            pygame.draw.circle(surface, WHITE, (sx, sy), radius)

# Create stars
stars = [Star() for _ in range(NUM_STARS)]

# Main loop
running = True
speed = 10

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update and draw stars
    for star in stars:
        star.update(speed)
        star.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
