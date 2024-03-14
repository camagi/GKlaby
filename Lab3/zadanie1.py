import pygame
import sys
import math

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
cenx, ceny = 300, 300
surfaceorg = pygame.Surface((2 * cenx, 2 * ceny))
surnex = pygame.Surface((2 * cenx, 2 * ceny))

points = [(150, 150), (450, 150), (550, 450), (250, 450)]
num_sides = 6
radius = 150
vertices = []
for i in range(num_sides):
    angle = (2 * math.pi * i) / num_sides
    x = cenx + int(radius * math.cos(angle))
    y = ceny + int(radius * math.sin(angle))
    vertices.append((x, y))


def draw_polygon(vertices):
    pygame.draw.polygon(surfaceorg, red, vertices)  # Zmieniamy kolor na czerwony


running = True
while running:

    draw_polygon(vertices)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Przekształcenia po naciśnięciu klawiszy
            if event.key == pygame.K_1:
                screen.fill(black)
                screen.blit(surfaceorg, (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_2:
                screen.fill(black)
                screen.blit(pygame.transform.rotozoom(surfaceorg, 45, 1.4), (-270, -270))
                pygame.display.flip()
            if event.key == pygame.K_3:
                screen.fill(black)
                screen.blit(pygame.transform.flip(pygame.transform.scale_by(surfaceorg, (1, 1.4)), False, True), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_4:
                screen.fill(black)
                surnex.blit(pygame.transform.scale_by(surfaceorg, (2, 1)), (-300, -150))
                screen.blit(pygame.transform.rotozoom(surnex, 140, 0.5), (100, 50))
                pygame.display.flip()
            if event.key == pygame.K_5:
                screen.fill(black)
                screen.blit(pygame.transform.scale_by(surfaceorg, (1.5, 0.5)), (-150, -50))
                pygame.display.flip()
            if event.key == pygame.K_6:
                screen.fill(black)
                surnex.blit(pygame.transform.scale_by(surfaceorg, (2, 1)), (-300, -150))
                screen.blit(pygame.transform.rotozoom(surnex, 46, 0.6), (100, 50))
                pygame.display.flip()
            if event.key == pygame.K_7:
                screen.fill(black)
                screen.blit(pygame.transform.flip(pygame.transform.scale_by(surfaceorg,
                                                            (1, 1.4)), True, True), (0, 0))
                pygame.display.flip()
            if event.key == pygame.K_8:
                screen.fill(black)
                # Przeskalowanie szerokości obrazka bez zmiany wysokości
                scaled_width_surface = pygame.transform.scale(surfaceorg, (
                int(surfaceorg.get_width() * 1.5), surfaceorg.get_height()))
                # Spłaszczenie obrazka o połowę
                flattened_surface = pygame.transform.scale(scaled_width_surface, (
                int(scaled_width_surface.get_width() * 0.5), scaled_width_surface.get_height()))
                screen.blit(pygame.transform.rotozoom(flattened_surface, 45, 1), (-150, 20))
                pygame.display.flip()
            if event.key == pygame.K_9:
                screen.fill(black)
                # Skalowanie obrazka
                scaled_surface = pygame.transform.scale(surfaceorg,(int(surfaceorg.get_width() * 2), surfaceorg.get_height()))
                # Odwrócenie obrazka
                flipped_surface = pygame.transform.flip(scaled_surface, True, True)
                # Rysowanie obrazka
                screen.blit(pygame.transform.rotozoom(flipped_surface, 315, 0.5), (150, 150))
                pygame.display.flip()

        pygame.quit()
        sys.exit()
