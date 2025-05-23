import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updateable,drawable)
    
    dt = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    
    player = Player(x, y)
    
    group_asteroids = pygame.sprite.Group()
    Asteroid.containers = (group_asteroids, updateable, drawable)
    
    AsteroidField.containers = (updateable)
    
    asteroid_field = AsteroidField()
    
    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updateable, drawable)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        updateable.update(dt)
                    
        for asteroid in group_asteroids:
            if asteroid.collision_detected(player):
                print("Game over!")
                sys.exit()
            
            for bullet in shots_group:
                if asteroid.collision_detected(bullet):
                    asteroid.split()
                    bullet.kill()
                
        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()