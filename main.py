import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import *
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Asteroid.containers =(asteroids, updatable, drawable)
    player=Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroidfield=AsteroidField()
    while True: 
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        for ast in asteroids:
            for sh in shots:
                if sh.collides_with(ast):
                    log_event("asteroid_shot")
                    ast.kill()
                    sh.kill()
        for item in asteroids:
            if item.collides_with(player) == True:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        pygame.display.flip()
        
        
            
        dt = clock.tick(60)/1000
        
        

if __name__ == "__main__":
    main()
