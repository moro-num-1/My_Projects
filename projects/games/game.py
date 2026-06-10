import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Jumper")
clock = pygame.time.Clock()

#Surfaces
sur1 = pygame.Surface((300, 150))
sur2 = pygame.Surface((300, 150))
sur3 = pygame.Surface((300, 150))

#Coloring surfaces
sur1.fill("Blue")
sur2.fill("Red")
sur3.fill("Green")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sur1, (200, 1h00))
    pygame.display.update()
    clock.tick(60) 