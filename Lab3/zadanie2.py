import pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 600, 600
BACKGROUND_COLOR = (0, 0, 0)
RECT_COLOR = (0, 250, 5)
TRIANGLE_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, RECT_COLOR, pygame.Rect(200, 200, 200, 200))
    pygame.draw.polygon(screen, TRIANGLE_COLOR, [(300, 300), (400, 400), (200, 400)])
    pygame.display.flip()

pygame.quit()
