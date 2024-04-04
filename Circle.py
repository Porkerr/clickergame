import pygame
# Circle class
class Circle:
    # draw_circle method requires self, radius, color ([x, y, z]), position (x, y), and returns it
    def draw_circle(self, radius, color = [], position = []):
        return pygame.draw.circle(self.screen, (color[0], color[1], color[2]), (position[0], position[1]), radius)
