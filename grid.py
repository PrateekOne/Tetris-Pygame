class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.color = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()

def get_cell_colors(self):

    dark_grey=(26,31,40)
    green= (57, 255, 20)
    red= (255, 16, 16)
    yellow= (255, 255, 20)
    purple= (191, 0, 255)
    cyan= (0, 255, 255)
    blue= (0, 150, 255)
    return[dark_grey,green,red,yellow,purple,cyan,blue]

def draw(self):
    for row in range(self.num.row):
        for column in range(self.num.cols):
            cell_value=self.grid[rows][columns]
            cell_rect = pygame.Rect(column*self.cell_size,row*self.cell_size,self.cell_size,self.cell_size)