import pygame

WinWidth = WinHeight = 1200
Window = pygame.display.set_mode((WinWidth, WinHeight))
pygame.display.set_caption("Solar system simulation")

mercury = Planet("Mercury", -0.39e11, 0, 3.3011e23, 2439.7, (0, 47870))
venus = Planet("Venus", 0.72e11, 0, 4.8675e24, 6051.8, (0, 35020))
earth = Planet("Earth", 1.496e11, 0, 5.972e24, 6371, (0, 29783))
mars = Planet("Mars", 2.28e11, 0, 6.39e23, 3389.5, (0, 24007))



def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        Window.fill((0, 0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygmae.QUIT:
                run = False
    pygame.quit()

