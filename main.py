import pygame
from SolarSys.planets import *

WinWidth = WinHeight = 900
Window = pygame.display.set_mode((WinWidth, WinHeight))
pygame.display.set_caption("Solar system simulation")


if __name__ == "__main__":
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        Window.fill((0, 0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for object in CelestialObjects:
            object.draw(Window)

        pygame.display.update()
            
    pygame.quit() 

