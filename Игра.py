import pygame


class Field:
    def __init__(self, width, height, color_line):
        self.width = width
        self.height = height
        self.color_line = color_line

    def draw(self, screen):
        for i in range(-1, 10, 2):
            pygame.draw.rect(screen, (80, 166, 50),
                             (self.width // 10 * i, 0, self.width // 10, self.height))
        pygame.draw.polygon(screen, self.color_line,
                            ((0, 0), (self.width, 0), (self.width, self.height), (0, self.height)), self.height // 50)
        pygame.draw.polygon(screen, self.color_line,
                            ((self.width + 10, self.height // 6), (self.width - self.width // 5, self.height // 6),
                             (self.width - self.width // 5, self.height - self.height // 6),
                             (self.width + 10, self.height - self.height // 6)), self.height // 100)
        pygame.draw.polygon(screen, self.color_line,
                            ((0 - 10, self.height // 6), (self.width // 5, self.height // 6),
                             (self.width // 5, self.height - self.height // 6),
                             (0 - 10, self.height - self.height // 6)), self.height // 100)
        pygame.draw.line(screen, (255, 75, 75),
                         (0, self.height // 3), (0, self.height - self.height // 3), self.height // 50)
        pygame.draw.line(screen, (75, 75, 255),
                         (self.width, self.height // 3), (self.width, self.height - self.height // 3),
                         self.height // 50)
        pygame.draw.circle(screen, self.color_line,
                           (self.width // 2, self.height // 2), self.height // 50)
        pygame.draw.line(screen, self.color_line,
                         (self.width // 2, 0), (self.width // 2, self.height),
                         self.height // 100)
        pygame.draw.circle(screen, self.color_line,
                           (self.width // 2, self.height // 2), self.height // 4, self.height // 100)


clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y, color, keys, polygon):
        self.keys = keys
        self.x = x
        self.x_speed = 0
        self.y = y
        self.y_speed = 0
        self.size = height // 14
        self.color = color
        self.polygon = polygon

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)

    def keydown(self, key):
        if self.keys[0] == key:
            self.y_speed += -1
        elif self.keys[1] == key:
            self.y_speed += 1
        elif self.keys[2] == key:
            self.x_speed += -1
        elif self.keys[3] == key:
            self.x_speed += 1

    def keyup(self, key):
        if self.keys[0] == key:
            self.y_speed += 1
        elif self.keys[1] == key:
            self.y_speed += -1
        elif self.keys[2] == key:
            self.x_speed += 1
        elif self.keys[3] == key:
            self.x_speed += -1

    def update(self):
        self.x = self.x + self.x_speed * height // 100
        self.y = self.y + self.y_speed * height // 100
        self.borders()

    def borders(self):
        x, y, w, h = self.polygon
        if self.x < x:
            self.x = x
        elif self.x > x + w:
            self.x = x + w

        if self.y < y:
            self.y = y
        elif self.y > y + h:
            self.y = y + h


class Ball:
    def __init__(self, xb, yb, polygon):
        self.xb = xb
        self.yb = yb
        self.polygon = polygon

    def draw(self, surface):
        pygame.draw.circle(surface, (200, 200, 200), (self.xb, self.yb), height // 18)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущиеся круги')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    color_line = (230, 230, 230)

    running = True

    field = Field(width, height, color_line)

    player1 = Player(width // 2 - width // 4, height // 2, (255, 55, 0), [pygame.K_w, pygame.K_s,
                                                                          pygame.K_a, pygame.K_d],
                     (height // 14, height // 14,
                      width - height // 14 * 2, height - height // 14 * 2))
    player2 = Player(width // 2 + width // 4, height // 2, (0, 55, 255), [pygame.K_UP, pygame.K_DOWN,
                                                                          pygame.K_LEFT, pygame.K_RIGHT],
                     (height // 14, height // 14,
                      width - height // 14 * 2, height - height // 14 * 2))

    ball = Ball(width // 2, height // 2, (height // 14, height // 14,
                                          width - height // 14 * 2, height - height // 14 * 2))

    v = height // 2
    fps = 60
    clock = pygame.time.Clock()

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                player1.keydown(event.key)
                player2.keydown(event.key)

            elif event.type == pygame.KEYUP:
                player1.keyup(event.key)
                player2.keyup(event.key)

        screen.fill((95, 161, 50))

        field.draw(screen)

        player1.update()
        player2.update()

        player1.draw(screen)
        player2.draw(screen)

        ball.draw(screen)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
