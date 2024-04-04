import pygame
"""
Circle Class is NOT FINISHED
     At the moment I have not found a way to implement one function to render the
circle so we can calculate with it and one to draw the circle. This leads to some
strange code in the running method of the Game class where the circle is drawn so
we can calculate with it and then drawn once again later after we fill the screen black.
Not sure if there is a workaround for this but I will leave it for one of you guys
"""
class Circle:
    # draw_circle method requires self, radius, color ([x, y, z]), position (x, y), and returns it
    def draw_circle(self, radius, color = [], position = []):
        return pygame.draw.circle(self.screen, (color[0], color[1], color[2]), (position[0], position[1]), radius)
