import pygame

class Rectangle:
    # rend_rect method requires rectangle width, height, and positon (x, y), and will return a rect object with those properties
    def rend_rect(width, height, position = []):
        rect = pygame.Rect(position[0], position[1], width, height)
        return rect
    # draw_rect method will take a screen obj, a color ([x, y, z]), the rendered rectangle obj, and draw the object on the screen
    def draw_rect(self, color, rect):
        pygame.draw.rect(self.screen, (color[0], color[1], color[2]), rect)
    # This method takcalculates the x and y coordinate for text within a given rect obj
    def center_rect_text(self, rect, rect_text):
        x = rect.left + rect.width/2 - rect_text.get_width()/2
        y = rect.top + rect.height/2 - rect_text.get_height()/2
        return x, y
