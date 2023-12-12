from super_person import SuperPerson

class Trump(SuperPerson):
    default_width, default_height = 133, 100
    def __init__(self, pygame, image_name, width, height, x_pos, y_pos):
        super().__init__(pygame, image_name, width, height, x_pos, y_pos)