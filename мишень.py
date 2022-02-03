import pygame

w, n = input().split()

lst = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]

flag = True
if w.isdigit() and n.isdigit():
    def draw(screen):
        screen.fill((0, 0, 0))
        for i in range(1, int(n) + 1):
            pygame.draw.circle(screen, lst[i % 3], (int(w) * int(n), int(w) * int(n)), int(w) * i, int(w))
else:
    print('Неправильный формат ввода')
    flag = False


if __name__ == '__main__' and flag:
    pygame.init()
    size = width, height = int(w) * int(n) * 2, int(w) * int(n) * 2
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw(screen)
        pygame.display.flip()
