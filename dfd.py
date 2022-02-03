import pygame
from random import randint


class MyDrop():
    def __init__(self, pos):
        self.radius = 0
        self.pos = pos
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.speed_increase = randint(50, 200) / 100
        self.max_size = randint(50, 300)

    def increase(self):
        self.radius += self.speed_increase
        if self.radius > self.max_size:
            return False
        self.draw()
        return True

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, int(self.radius))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Капли')
    size = width, height = 1920, 1080

    screen = pygame.display.set_mode(size)

    v = 50
    fps = 60
    clock = pygame.time.Clock()

    list_drop = [MyDrop((randint(0, width), randint(0, height))) for i in range(100)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                list_drop.append(MyDrop(event.pos))
        screen.fill((0, 0, 255))

        list_drop = [i for i in list_drop if i.increase()]
        while len(list_drop) < 500:
            list_drop.append(MyDrop((randint(0, width), randint(0, height))))

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
