import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Static Effect")

running = True
intensity = 0.2
static_chance = intensity
clock = pygame.time.Clock()

def draw_static(intensity):
    static_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    for y in range(0, height, 8):
        if random.random() < static_chance:
            pygame.draw.line(static_surface, (255, 255, 255, random.randint(30, 80)), (0, y), (width, y))
    screen.blit(static_surface, (0, 0), special_flags=pygame.BLEND_ADD)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_static(intensity)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()