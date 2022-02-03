import pygame

w = input()
h = input()

flag = True
if w.isdigit() and h.isdigit() and (int(w) % 4 == 0 and int(w) <= 100 and int(h) <= 360):
    def draw(screen):
        color = pygame.Color(255, 0, 0)
        hsv = color.hsva
        color.hsva = (h, 100, 75)
        pygame.draw.rect(screen, color, (width // 2 - int(w) // 2,
                                         height // 2 - int(w) // 2,
                                         int(w), int(w)))
        color.hsva = (h, 100, 100)
        pygame.draw.polygon(screen, color, ((width // 2 - int(w) // 2,
                                             height // 2 - int(w) // 2),
                                            (width // 2,
                                             height // 2 - int(w)),
                                            (width // 2 + int(w),
                                             height // 2 - int(w)),
                                            (width // 2 - int(w) // 2 + int(w),
                                             height // 2 - int(w) // 2)))
        color.hsva = (h, 100, 50)
        pygame.draw.polygon(screen, color, ((width // 2 - int(w) // 2 + int(w),
                                             height // 2 - int(w) // 2),
                                            (width // 2 + int(w),
                                             height // 2 - int(w),
                                            (width // 2 + int(w),
                                             height // 2),
                                            (width // 2 + int(w) // 2,
                                             height // 2 + int(w) // 2))))

else:
    print('Неправильный формат ввода')
    flag = False

if __name__ == '__main__' and flag:
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    while pygame.event.wait().type != pygame.QUIT:
        draw(screen)
        pygame.display.flip()
    pygame.quit()
