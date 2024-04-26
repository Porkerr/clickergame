import pygame

# Rectangle Class
class Hitbox:
    # rend_hitbox method requires rectangle width, height, and positon (x, y),
    # and will return a rect object with those properties
    def rend_hitbox(width, height, position = []):
        rect = pygame.Rect(position[0], position[1], width, height)
        return rect
    
    # draw_hitbox method will take a screen obj, a color ([x, y, z]), the rendered rectangle obj,
    # and draw the object on the screen
    def draw_hitbox(self, color, rect):
        pygame.draw.rect(self.screen, (color[0], color[1], color[2]), rect)
        
    # This method calculates the x and y coordinate for text within a given rect obj
    def center_hitbox_text(self, rect, rect_text):
        x = rect.left + rect.width/2 - rect_text.get_width()/2
        y = rect.top + rect.height/2 - rect_text.get_height()/2
        return x, y

    # For checking if the rectangles are clicked, our code directly compares the mouse coordinates
    # (mouse_x, mouse_y) with the bounding box defined by the positions and dimensions of the rectangles.  
    def rect_hitbox_detect(rect, mouse_x, mouse_y):
        if ((rect.x <= mouse_x <= rect.x + rect.width) and \
                       (rect.y <= mouse_y <= rect.y + rect.height)) == True:
            return True
        else:
            return False

    # draw_circle_hitbox method requires self, radius, color ([x, y, z]), position (x, y), and returns hitbox
    def draw_circle_hitbox(self, radius, color = [], position = []):
        return pygame.draw.circle(self.screen, (color[0], color[1], color[2]), (position[0], position[1]), radius)
    
    # For checking if a mouse is over circle, I figured out you can use the distance formula (Euclidean distance)...
    # some complex math thing you probably dont want me to explain bc you're tired of math classes
    def circle_hitbox_detect(rect, mouse_x, mouse_y):
        if (((mouse_x - rect.centerx)**2 + (mouse_y - rect.centery)**2) <= (rect.width/2)**2) == True:
            return True
        else:
            return False 
