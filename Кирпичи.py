import pygame


def draw(screen):
    color = pygame.Color(255, 0, 0)
    screen.fill((255, 255, 255))
    w = 30
    h = 15
    for i in range(0, 200 // 17 + 1, 1):
        for j in range(-15 * (i % 2), 300, 32):
            pygame.draw.rect(screen, color, (j, i * 17, w, h))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 200
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw(screen)
        pygame.display.flip()
    pygame.quit()
