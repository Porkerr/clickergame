import pygame
import sys
from Circle import Circle
from Rectangle import Rectangle
from pygame import mixer

class Game:
    def __init__(self):
        pygame.init()  # Initialize pygame
        
        # Set up the display window
        pygame.display.set_caption("Clicker Game")  # Sets the window title !
        self.screen = pygame.display.set_mode((1000, 600))  # sets the aspect ratio
        self.clock = pygame.time.Clock()  # clock for controlling frame rate
        
        # the font for our text, can change later if u feelin fancy
        self.font = pygame.font.Font(None, 36)  # Set font for text rendering
        
        # text for when u click circle
        #self.circle_text = self.font.render("Click me for points", True, (255, 255, 255))  # This is gonna render our 'click me' text for circle
        
        # text for upgrade buttons(they're rectangles so i used rect)
        # self.rect1_text = self.font.render("+10 Points Per Click (25 pts)", True, (255, 255, 255))  # Render text for rectangle1
        # self.rect2_text = self.font.render("Upgrade Idle Clicker (25 pts)", True, (255, 255, 255))  # Render text for rectangle2
        
        # Idle point gainer variables
        self.idle_gainer_interval = 1000  # 1000 milliseconds (1 second)
        self.idle_gainer_timer = pygame.time.get_ticks() + self.idle_gainer_interval  # Timer to track next point gain
        
    def running(self):
        # Render rects for Upgrade buttons
        rect1 = Rectangle.rend_rect(300, 100, [450, 200])
        rect2 = Rectangle.rend_rect(300, 100, [450, 400])
        # Render rect for counter
        rect3 = Rectangle.rend_rect(300, 100, [75, 50])    
        # Draw circle for calculating properties
        circle = Circle.draw_circle(self, 200, [0, 0, 0], [225, 375])
        
        idlepoints = 1 # Number of points gained while idle
        points = 0 # Number of times circle clicked
        ppc = 1 # Number of points you get per click

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
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position. We need this so we know what's being clicked.
                    # Check if mouse click occurred within the circle
                    # For checking if a mouse is over something, I figured out you can use the distance formula (Euclidean distance).. some complex math thing you probably dont want me to explain bc you're tired of math classes
                    if ((mouse_x - circle.centerx)**2 + (mouse_y - circle.centery)**2) <= (circle.width/2)**2:
                        points+=ppc # Increment times circle is clicked
                        print("Circle clicked!")  # For demonstration purposes
                        print("Points: " + str(points)) # For demonstration purposes
                        
                    # Check if mouse click occurred within the top upgrade button
                    #For checking if the rectangles are clicked, our code directly compares the mouse coordinates (mouse_x, mouse_y)                      
                    #with the bounding box defined by the positions and dimensions of the rectangles.                                          
                    if (rect1.x <= mouse_x <= rect1.x + rect1.width) and \
                       (rect1.y <= mouse_y <= rect1.y + rect1.height):
                        print("Points Per Click Upgrade Clicked!")
                         # check if they have enough points to buy
                        # if yes buy, if no display "not enough points :("
                        if (points >= 25):
                            points -= 25
                            ppc += 10
                        else:
                            print("Not enough points!") # demo only
                            #TODO: implement not enough points message if they can't afford upgrade, visible to player
                        print("Current points per click: " + str(ppc)) # for demonstration purposes
                        
                    # Check if mouse click occurred within the bottom rectangle button. If so, upgrade idle point clicker and charge 25 points.
                    if (rect2.x <= mouse_x <= rect2.x + rect2.width) and \
                       (rect2.y <= mouse_y <= rect2.y + rect2.height):
                        print("Rectangle 2 clicked!")
                        if ( points >= 25):
                            points -= 25
                            idlepoints += 10
                        
            # Idle point gainer
            if current_time >= self.idle_gainer_timer:  # Check if it's time to gain points
                points += idlepoints  # Increment points by 1
                self.idle_gainer_timer = current_time + self.idle_gainer_interval  # Reset timer
            
            # Fill the screen 
            self.screen.fill("Black")
            
            # Draws the clicking circle on the screen
           #  Circle.draw_circle(self, 200, [0, 255, 0], [225, 375])
 
 
            # create a surface object, image is drawn on it.
            clickIcon = pygame.image.load("alien.png").convert()
            # Using blit to copy content from one surface to other
            self.screen.blit(clickIcon, (90, 234))

            
            
            # Sets the icon in the top left to the logo, our alien
            icon = pygame.image.load('alien.png')

            
            pygame.display.set_icon(icon)
            

            # Draw the upgrade buttons on the screen
            # Rectangle.draw_rect(self, (0, 0, 255), rect1)
            #PPC Upgrade
            upgradePPC = pygame.image.load("points per click.png").convert()
            # Using blit to copy content from one surface to other
            self.screen.blit(upgradePPC, (400, 94))

           # Rectangle.draw_rect(self, (125, 125, 12), rect2)
            #PPS Upgrade
            upgradePPS = pygame.image.load("points per second.png").convert()
            # Using blit to copy content from one surface to other
            self.screen.blit(upgradePPS, (400, 334))

            
            # Draw the counter on the screen
            Rectangle.draw_rect(self, (200, 40, 60), rect3)
            
            # render/display text for the circle
            # tHis positions the text within the circle's center
            # self.screen.blit(self.circle_text, self.circle_text.get_rect(center=circle.center))
            
            # render/display text for the rectangles
            # rect3_text must be rendered each time the text is drawn to screen  
            # self.screen.blit(self.rect1_text, Rectangle.center_rect_text(self, rect1, self.rect1_text))
            # self.screen.blit(self.rect2_text, Rectangle.center_rect_text(self, rect2, self.rect2_text))
            self.rect3_text = self.font.render("Times Clicked: " + str(points), True, (255, 255, 255))
            self.screen.blit(self.rect3_text, Rectangle.center_rect_text(self, rect3, self.rect3_text))

            self.clock.tick(60)  # Limits frame rate to 60 FPS
            
            pygame.display.flip()  # Update the display

if __name__ == "__main__":
    clickGame = Game()  # Instantiate the game
    clickGame.running()  # Run the game
