class Colors:
    dark_grey = (26, 31, 40)
    green = (57, 255, 20)
    red = (255, 16, 16)
    orange = (255, 97, 3)
    yellow = (255, 255, 20)
    purple = (191, 0, 255)
    cyan = (0, 255, 255)
    blue = (0, 150, 255)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]