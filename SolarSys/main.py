import pygame

WinWidth = WinHeight = 1200
Window = pygame.display.set_mode((WinWidth, WinHeight))
pygame.display.set_caption("Solar system simulation")

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

