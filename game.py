import pygame
import sys
@Hey guys - Alex here
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
        self.circle_position = (self.circle_radius, 300)  # Positions circle on  left side of screen

        # Upgrade buttons (rectangles) properties
        self.rect_width = 300  # width of the rectangle
        self.rect_height = 100  # height of the rectangle
        self.rect_color = (0, 0, 255)  # blue color for the top rectangle
        self.rect2_color = (0,120,120)  # green color for the bottom rectangle
        self.rect1_position = (450, 50)  # pos for the top rectangle
        self.rect2_position = (450, 200)  # pos for the bottom rectangle

        # the font for our text, can change later if u feelin fancy
        self.font = pygame.font.Font(None, 36)  # Set font for text rendering

        # text for when u click circle
        self.circle_text = self.font.render("Click me for points", True, (255, 255, 255))  # This is gonna render our 'click me' text for circle
        self.circle_text_rect = self.circle_text.get_rect(center=self.circle_position)  # tHis positions the text within the circle's center

        # text for upgrade buttons(they're rectangles so i used rect)
        self.rect_text = self.font.render("Upgrade", True, (255, 255, 255))  # Render text for rectangles

    def running(self):
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
                        print("Circle clicked!")  # For demonstration purposes

                    # Check if mouse click occurred within the top upgrade button
                    #For checking if the rectangles are clicked, our code directly compares the mouse coordinates (mouse_x, mouse_y)                      
                    #with the bounding box defined by the positions and dimensions of the rectangles.                                          
                    if (self.rect1_position[0] <= mouse_x <= self.rect1_position[0] + self.rect_width) and \
                       (self.rect1_position[1] <= mouse_y <= self.rect1_position[1] + self.rect_height):
                        print("Rectangle 1 clicked!")

                    # Check if mouse click occurred within the bottom rectangle button
                    if (self.rect2_position[0] <= mouse_x <= self.rect2_position[0] + self.rect_width) and \
                       (self.rect2_position[1] <= mouse_y <= self.rect2_position[1] + self.rect_height):
                        print("Rectangle 2 clicked!")

            # Fill the screen  
            self.screen.fill("Black")
            
            # Draws the circle on the screen
            pygame.draw.circle(self.screen, self.circle_color, self.circle_position, self.circle_radius)
            
            # Draw the rectangles (upgrade buttons) on the screen
            pygame.draw.rect(self.screen, self.rect_color, (self.rect1_position, (self.rect_width, self.rect_height)))
            pygame.draw.rect(self.screen, self.rect2_color, (self.rect2_position, (self.rect_width, self.rect_height)))
            
            # render/display text for the circle
            self.screen.blit(self.circle_text, self.circle_text_rect)
            
            #  render/display text for the rectangles
            self.screen.blit(self.rect_text, (self.rect1_position[0] + self.rect_width/2 - self.rect_text.get_width()/2, 
                                              self.rect1_position[1] + self.rect_height/2 - self.rect_text.get_height()/2))
            self.screen.blit(self.rect_text, (self.rect2_position[0] + self.rect_width/2 - self.rect_text.get_width()/2, 
                                              self.rect2_position[1] + self.rect_height/2 - self.rect_text.get_height()/2))

            sVYTelf.clock.tick(60)  # Limits frame rate to 60 FPS
            
            pygame.display.flip()  # Update the display

if __name__ == "__main__":
    clickGame = Game()  # Instantiate the game
    clickGame.running()  # Run the game
