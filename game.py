import pygame
import sys
from Hitbox import Hitbox
from Text import Text
from pygame import mixer

class Game:
    def __init__(self):
        pygame.init()  # Initialize pygame
        
        # Set up the display window
        pygame.display.set_caption("Clicker Game")  # Sets the window title!
        self.screen = pygame.display.set_mode((1100, 800))  # sets the aspect ratio
        self.clock = pygame.time.Clock()  # clock for controlling frame rate
        
        # the font for our text, can change later if u feelin fancy
        self.font = pygame.font.Font("assets\\fonts\\8bit madness.ttf", 48)  # Set font for text rendering
        
        # Idle point gainer variables
        self.idle_gainer_interval = 1000  # 1000 milliseconds (1 second)
        self.idle_gainer_timer = pygame.time.get_ticks() + self.idle_gainer_interval  # Timer to track next point gain
        
    def running(self):
        # Render rects for Upgrade buttons
        ppc_hitbox = Hitbox.rend_hitbox(465, 180, [450, 130])
        pps_hitbox = Hitbox.rend_hitbox(465, 180, [450, 370])
        # Draw circle hitbox for calculating properties
        alien_hitbox = Hitbox.draw_circle_hitbox(self, 130, [0, 0, 0], [225, 300])
        
        idlepoints = 0 # Number of points gained while idle
        points = 0 # Number of times circle clicked
        ppc = 0 # Number of points you get per click
        goal = 1000000

        mixer.init() # init music mixer
        
        while True:
            # play music on loop
            if pygame.mixer.music.get_busy() == False:
                mixer.music.load("assets\\songs\\mii.mp3") # also have fallen_meown.mp3
                pygame.mixer.music.play()

            current_time = pygame.time.get_ticks()  # Get current time
            for event in pygame.event.get():  # Check for events
                if event.type == pygame.QUIT:  # if quit event is detected makes ya leave the game
                    pygame.quit()  # quits pygame
                    sys.exit()  # exits the program
                elif event.type == pygame.MOUSEBUTTONDOWN:  # THIS is important. It basically can detect whenever the mouse button is pressed
                    # Play noise when clicking
                    click = pygame.mixer.Sound('assets\\sounds\\coin.mp3')
                    
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position. We need this so we know what's being clicked.
                    # Check if mouse click occurred within the clicker hitbox
                    if (Hitbox.circle_hitbox_detect(alien_hitbox, mouse_x, mouse_y)):
                        # Singles out left click button only
                        if event.button == 1:
                            # If the bonus ppc is 0 just add 1, otherwise add the bonus
                            if ppc == 0:
                                points+=1
                            else:
                                points+=ppc # Increment times circle is clicked
                            print("Hitbox clicked!")  # For demonstration purposes
                            print("Points: " + str(points)) # For demonstration purposes
                            mixer.Sound.play(click)
                            
                    # Check if mouse click occurred within the top upgrade button                                
                    if (Hitbox.rect_hitbox_detect(ppc_hitbox, mouse_x, mouse_y)):
                        if event.button == 1:
                            print("Points Per Click Upgrade Clicked!")
                        # check if they have enough points to buy
                        # if yes buy, if no display "not enough points :("
                            if (points >= 25):
                                points -= 25
                                ppc += 10
                                mixer.Sound.play(click)
                            else:
                                print("Not enough points!") # demo only
                            #TODO: implement not enough points message if they can't afford upgrade, visible to player
                            print("Current points per click: " + str(ppc)) # for demonstration purposes
                        
                    # Check if mouse click occurred within the bottom rectangle button. If so, upgrade idle point clicker and charge 25 points.
                    if (Hitbox.rect_hitbox_detect(pps_hitbox, mouse_x, mouse_y)):
                        if event.button  == 1:
                            print("Points Per Second Upgrade Clicked!")
                            if ( points >= 25):
                                points -= 25
                                idlepoints += 10
                                mixer.Sound.play(click)
                            else:
                                print("Not enough points!")
                            print("Current points per second: " + str(idlepoints))
                        
            # Idle point gainer
            if current_time >= self.idle_gainer_timer:  # Check if it's time to gain points
                points += idlepoints  # Increment points
                self.idle_gainer_timer = current_time + self.idle_gainer_interval  # Reset timer
            
            # Fill the screen 
            self.screen.fill("Black")
            
            # Draws the clicking circle on the screen
           #  Hitbox.draw_circle_hitbox(self, 200, [0, 255, 0], [225, 375])
             
            # create a surface object, image is drawn on it.
            clickIcon = pygame.image.load("assets\\alien.png")
            # Using blit to copy content from one surface to other
            self.screen.blit(clickIcon, (65, 160))
            
            # Sets the icon in the top left to the logo, our alien
            icon = pygame.image.load('assets\\greencubeguy.png')
            pygame.display.set_icon(icon)
        
            # Draw the upgrade buttons on the screen
            # Rectangle.draw_hitbox(self, (0, 0, 255), ppc_hitbox)
            #PPC Upgrade
            upgradePPC = pygame.image.load("assets\\points per click.png")
            # Using blit to copy content from one surface to other
            self.screen.blit(upgradePPC, (400, 94))

            # Rectangle.draw_hitbox(self, (125, 125, 12), pps_hitbox)
            #PPS Upgrade
            upgradePPS = pygame.image.load("assets\\points per second.png")
            # Using blit to copy content from one surface to other
            self.screen.blit(upgradePPS, (400, 334))
            
            """ Draws Hitboxes
            Hitbox.draw_circle_hitbox(self, 130, [200, 200, 200], [225, 300])
            Hitbox.draw_hitbox(self, (200, 200, 200), ppc_hitbox)
            Hitbox.draw_hitbox(self, (200, 200, 200), pps_hitbox)
            """
            self.points_text = self.font.render("Points: " + Text.abbr_num(points), True, (255, 255, 255))
            self.pps_text = self.font.render("Points Per Second: " + Text.abbr_num(idlepoints), True, (255, 255, 255))
            self.ppc_text = self.font.render("Points Per Click: " + Text.abbr_num(ppc), True, (255, 255, 255))
            self.goal_text = self.font.render("Current Goal: " + Text.abbr_num(goal), True, (255, 255, 255))
            self.screen.blit(self.points_text, (0, 0))
            self.screen.blit(self.goal_text, (0, 50))
            self.screen.blit(self.pps_text, (550, 0))
            self.screen.blit(self.ppc_text, (550, 50))
            
            # Check if goal is reached
            if points >= goal:
                #Multiply goal by a thousand if reached
                goal *= 1000
            
            self.clock.tick(60)  # Limits frame rate to 60 FPS
            
            pygame.display.flip()  # Update the display

if __name__ == "__main__":
    clickGame = Game()  # Instantiate the game
    clickGame.running()  # Run the game
