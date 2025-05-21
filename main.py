import pygame
from constants import *
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill((0,0,0))
        dt = fps.tick(60) / 1000
        pygame.display.flip()
        


if __name__ == "__main__":
    main()