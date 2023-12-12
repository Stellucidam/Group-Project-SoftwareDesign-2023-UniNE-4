from super_element import SuperElement

class SuperPerson(SuperElement):
    def __init__(self, pygame, image_name, width, height, x_pos, y_pos):
        super().__init__(pygame, image_name, width, height)
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        image_rect = self.image.get_rect()
        image_rect.topleft = (self.x_pos, self.y_pos)
        self.image_rect = image_rect
        