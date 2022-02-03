import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 700, 700

    screen = pygame.display.set_mode(size)

    v = 50
    fps = 60
    clock = pygame.time.Clock()
    radius = 0
    x_pos = -10000000
    y_pos = -10000000

    flag = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = event.pos
                radius = 0
                flag = True
        screen.fill((0, 0, 255))
        if flag:
            radius += v / fps
            if radius <= 200:
                pygame.draw.circle(screen, (255, 255, 0), (x_pos, y_pos), int(radius))
            else:
                pygame.draw.circle(screen, (0, 0, 0), (0, 0), 0)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
