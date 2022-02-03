import pygame

class Cell():
    def __init__(self, pos, size, type):
        self.x, self.y = pos
        self.type = type
        self.size = size
        self.animation = False
        self.animation_size = 0
        self.animation_orientation = -1

    def draw(self, wnd):
        if self.animation:
            if self.animation_orientation == -1:
                if self.type == 1:
                    color = (255, 255, 255)
                else:
                    color = (0, 255, 255)
            else:
                if self.type == 1:
                    color = (0, 255, 255)
                else:
                    color = (255, 255, 255)
            self.animation_size += self.animation_orientation
            if self.animation_orientation == -1 and self.animation_size <= 0:
                self.animation_orientation = 1
            elif self.animation_size >= self.size:
                self.animation = False

            pygame.draw.rect(wnd, color, (self.x + 2 - self.animation_size // 2 + self.size // 2 ,
                                          self.y + 2,
                                          self.animation_size,
                                          self.size - 2))
        else:
            if self.type == 1:
                color = (0, 255, 255)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(wnd, color, (self.x + 2, self.y + 2, self.size - 2, self.size - 2))

    def cell_on_click(self):
        if not self.animation:
            self.animation = True
            self.animation_size = self.size
            self.animation_orientation = -1
            self.type = not self.type


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        self.cell_size = 30
        self.left = 10
        self.top = 10
        for i in range(height):
            lst = []
            for j in range(width):
                lst.append(Cell((j * self.cell_size + self.left,
                                 i * self.cell_size + self.left),
                                self.cell_size,
                                1))
            self.board.append(lst)


    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, wnd):
        wnd.fill((255, 0, 0), (self.top, self.left,
                                   self.cell_size * self.width + 2,
                                   self.cell_size * self.height + 2))
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].draw(wnd)

    def on_click(self, x, y):
        if x in range(self.width) and y in range(self.height):
            self.board[y][x].cell_on_click()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 170, 230
    screen = pygame.display.set_mode(size)

    fps = 60
    clock = pygame.time.Clock()

    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x = (x - board.left) // board.cell_size
                y = (y - board.top) // board.cell_size
                board.on_click(x, y)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
