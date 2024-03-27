import pygame
import sys


class Game:
    def __init__(self):
        pygame.init() #initializes pygame api
        pygame.display.set_caption("Clicker Game") # sets name of opened window to the string
        self.screen = pygame.display.set_mode((800, 600)) #sets aspect ratio
        self.clock = pygame.time.Clock()
        
    def running(self):
        while True:
            for event in pygame.event.get(): #api can get 'events' that can be checked and can do actions depending on what events are found
                if event.type == pygame.QUIT: # exits video game and closes window
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill("Black")
            self.clock.tick(60) #set fps limited to 60
            
            # docs say that this updates screen with whatever we put on the screen
            pygame.display.flip()
            

                
        
if __name__ == "__main__":
    clickGame = Game() #instantiates the game
    clickGame.running() #runs the game








