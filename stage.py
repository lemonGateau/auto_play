import random


class Stage:
    def __init__(self):
        self.MAX_LEFT  = 35
        self.MAX_RIGHT = 1000
        self.max_upper = 350
        self.MAX_LOWER = 1700
        self.BRIDGE_Y  = 1150

    def get_random_pos(self):
        x = random.randint(self.MAX_LEFT, self.MAX_RIGHT)
        y = random.randint(self.BRIDGE_Y, self.MAX_LOWER)
        return (x, y)

    def get_lower_left(self):
        return (self.MAX_LEFT, self.MAX_LOWER)

    def get_lower_right(self):
        return (self.MAX_RIGHT, self.MAX_LOWER)

    def get_lower_center(self):
        return ((self.MAX_LEFT + self.MAX_RIGHT)/2, self.MAX_LOWER)

    def get_left_bridge(self):
        return (210, self.BRIDGE_Y)

    def get_right_bridge(self):
        return (855, self.BRIDGE_Y)

    def get_left_enemy(self):
        return (120, 527)

    def get_right_enemy(self):
        return (950, 527)

    def get_card_pos(self, num=0):
        if num < 0 or num > 3:
            return (350, 2104)

        return (350 + 200*num, 2104)
