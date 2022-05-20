from stage import Stage


class Character:
    def __init__(self, name=None, extention="jpg"):
        if name:
            self.file_name = name + "." + extention
        self.set_pos()

    def get_file_name(self):
        if self.file_name:
            return self.file_name
        return None

    def get_pos(self):
        return (self.x, self.y)

    def set_pos(self, pos=[]):
        if len(pos) == 2:
            self.x = pos[0]
            self.y = pos[1]
            return

        stage = Stage()
        self.x, self.y = stage.get_lower_left()

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost
