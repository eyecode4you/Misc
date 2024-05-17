'''
dvd_screensaver.py
eyecode4you

CC0 - do what you want with this!
'''

import pygame
import random

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Will it Ever Hit a Corner?")

# dvd icon
dvd = pygame.image.load("./dvdlogo.png")
dvd = pygame.transform.scale(dvd, (138, 66))
dvd = dvd.convert_alpha()
dvd_rect = dvd.get_rect()
dvd_start = (random.randint(1, 400), random.randint(1, 400))
dvd_speed = (2, 2)
dvd_served = True
sx, sy = dvd_speed
dvd_rect.topleft = dvd_start

clock = pygame.time.Clock()
game_over = False

while not game_over:
    dt = clock.tick(60)
    screen.fill((128, 170, 255))

    screen.blit(dvd, dvd_rect)
    dvd_rect[0] += sx
    dvd_rect[1] += sy

    # keep icon within boundary
    if dvd_rect[1] <= 0:  # top
        dvd_rect[1] = 0
        sy *= -1

    if dvd_rect[1] >= screen.get_height() - dvd_rect.height:  # bottom
        dvd_rect[1] = screen.get_height() - dvd_rect.height
        sy *= -1

    if dvd_rect[0] <= 0:  # left
        dvd_rect[0] = 0
        sx *= -1

    if dvd_rect[0] >= screen.get_width() - dvd_rect.width: # right
        dvd_rect[0] = screen.get_width() - dvd_rect.width
        sx *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
pygame.quit()
