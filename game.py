import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()  # Initialize pygame

        # Set up the display window
        pygame.display.set_caption("Clicker Game")  # Sets the window title !
        self.screen = pygame.display.set_mode((800, 600))  # sets the aspect ratio
        self.clock = pygame.time.Clock()  # clock for controlling frame rate
        
        # Circle properties
        self.circle_radius = 200  # radius of  circle
        self.circle_color = (0, 255, 0)  #  color of circle
        self.circle_position = (self.circle_radius, 375)  # Positions circle on  left side of screen

        # Upgrade buttons (rectangles) properties
        self.rect1_width = 300  # width of the rectangle1
        self.rect1_height = 100  # height of the rectangle1
        self.rect1_color = (0, 0, 255)  # blue color for the top rectangle1
        self.rect1_position = (450, 50)  # pos for the top rectangle1
        
        self.rect2_width = 300  # width of the rectangle2
        self.rect2_height = 100  # height of the rectangle2
        self.rect2_color = (0,120,120)  # green color for the bottom rectangle2
        self.rect2_position = (450, 200)  # pos for the bottom rectangle2

        # Times Clicked tracker
        self.rect3_width = 300  # width of the rectangle3
        self.rect3_height = 100  # height of the rectangle3
        self.rect3_color = (0, 125, 125) # color for rectangle3
        self.rect3_position = (50, 50) # pos for rectangle3

        # the font for our text, can change later if u feelin fancy
        self.font = pygame.font.Font(None, 36)  # Set font for text rendering

        # text for when u click circle
        self.circle_text = self.font.render("Click me for points", True, (255, 255, 255))  # This is gonna render our 'click me' text for circle
        self.circle_text_rect = self.circle_text.get_rect(center=self.circle_position)  # tHis positions the text within the circle's center

        # text for upgrade buttons(they're rectangles so i used rect)
        self.rect1_text = self.font.render("Upgrade", True, (255, 255, 255))  # Render text for rectangle1
        self.rect2_text = self.font.render("Upgrade", True, (255, 255, 255))  # Render text for rectangle2

    def running(self):
        times_clicked = 0 # Number of times circle clicked
        while True:
            for event in pygame.event.get():  # Check for events
                if event.type == pygame.QUIT:  # if quit event is detected makes ya leave the game
                    pygame.quit()  # quits pygame
                    sys.exit()  # exits the program
                elif event.type == pygame.MOUSEBUTTONDOWN:  # THIS is important. It basically can detect whenever the mouse button is pressed
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position. We need this so we know what's being clicked.
                    # Check if mouse click occurred within the circle
                    #For checking if a mouse is over something, I figured out you can use the distance formula (Euclidean distance).. some complex math thing you probably dont want me to explain bc you're tired of math classes
                    if ((mouse_x - self.circle_position[0])**2 + (mouse_y - self.circle_position[1])**2) <= self.circle_radius**2:
                        times_clicked+=1 # Increment times circle is clicked
                        print("Circle clicked!")  # For demonstration purposes
                        print("Times clicked: " + str(times_clicked)) # For demonstration purposes
                        
                    # Check if mouse click occurred within the top upgrade button
                    #For checking if the rectangles are clicked, our code directly compares the mouse coordinates (mouse_x, mouse_y)                      
                    #with the bounding box defined by the positions and dimensions of the rectangles.                                          
                    if (self.rect1_position[0] <= mouse_x <= self.rect1_position[0] + self.rect1_width) and \
                       (self.rect1_position[1] <= mouse_y <= self.rect1_position[1] + self.rect1_height):
                        print("Rectangle 1 clicked!")

                    # Check if mouse click occurred within the bottom rectangle button
                    if (self.rect2_position[0] <= mouse_x <= self.rect2_position[0] + self.rect2_width) and \
                       (self.rect2_position[1] <= mouse_y <= self.rect2_position[1] + self.rect2_height):
                        print("Rectangle 2 clicked!")

            # Fill the screen  
            self.screen.fill("Black")
            
            # Draws the circle on the screen
            pygame.draw.circle(self.screen, self.circle_color, self.circle_position, self.circle_radius)
            
            # Draw the rectangles (upgrade buttons) on the screen
            pygame.draw.rect(self.screen, self.rect1_color, (self.rect1_position, (self.rect1_width, self.rect1_height)))
            pygame.draw.rect(self.screen, self.rect2_color, (self.rect2_position, (self.rect2_width, self.rect2_height)))
            pygame.draw.rect(self.screen, self.rect3_color, (self.rect3_position, (self.rect3_width, self.rect3_height)))
            
            # render/display text for the circle
            self.screen.blit(self.circle_text, self.circle_text_rect)
            
            #  render/display text for the rectangles
            self.rect3_text = self.font.render("Times Clicked: " + str(times_clicked), True, (255, 255, 255)) # Render text for rectangle3
            
            self.screen.blit(self.rect1_text, (self.rect1_position[0] + self.rect1_width/2 - self.rect1_text.get_width()/2, 
                                              self.rect1_position[1] + self.rect1_height/2 - self.rect1_text.get_height()/2))
            self.screen.blit(self.rect2_text, (self.rect2_position[0] + self.rect2_width/2 - self.rect2_text.get_width()/2, 
                                              self.rect2_position[1] + self.rect2_height/2 - self.rect2_text.get_height()/2))
            self.screen.blit(self.rect3_text, (self.rect3_position[0] + self.rect3_width/2 - self.rect3_text.get_width()/2, 
                                              self.rect3_position[1] + self.rect3_height/2 - self.rect3_text.get_height()/2))

            self.clock.tick(60)  # Limits frame rate to 60 FPS
            
            pygame.display.flip()  # Update the display

if __name__ == "__main__":
    clickGame = Game()  # Instantiate the game
    clickGame.running()  # Run the game
