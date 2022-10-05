import pygame, sys
from settings import *
import time
import random

def laser_update(laser_list, dt):
    for lasers in laser_list:
        for meteor in meteor_list:
            if lasers.colliderect(meteor):
                meteor_list.remove(meteor)
                laser_list.remove(lasers)
                explosion_sound.play()

        screen.blit(laser, lasers)
        lasers.y -= round(1000 * dt)
        if lasers.y < -100:
            laser_list.remove(lasers)

def meteor_update(meteor_list, dt):
    for meteors in meteor_list:
        screen.blit(meteor, meteors)
        meteors.y += round(300 * dt)
        meteors.x += round(100 * dt)
        if meteors.y > WINDOW_H + 150:
            meteor_list.remove(meteors)
        if meteors.x > WINDOW_W + 150:
            meteor_list.remove(meteors)

def meteor_player_collision(meteor_list):
    for meteors in meteor_list:
        if meteors.colliderect(player_rect):
            return True


def laser_time(can_shoot, duration=500):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - start_time > duration:
            can_shoot = True
    return can_shoot

import time
# Default pygame variables
pygame.init()
WINDOW_W, WINDOW_H = 1200, 700
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
# Static program variables
background = pygame.image.load("background.png").convert()

player = pygame.image.load("ship.png").convert_alpha()
player_rotated = pygame.transform.rotate(player, (45))
player_rect = player.get_rect(center=(WINDOW_W / 2, WINDOW_H / 2))


font = pygame.font.Font("subatomic.ttf", 30)


laser = pygame.image.load("laser.png").convert_alpha()
laser_list = []

meteor = pygame.image.load("meteor.png").convert_alpha()
meteor_list = []

laser_sound = pygame.mixer.Sound("laser.ogg")
explosion_sound = pygame.mixer.Sound("explosion.wav")
music = pygame.mixer.Sound("music.wav")
music.play(loops=-1)


can_shoot = True
start_time = None


meteor_time = 0
colli = False

fps = 60
laser_vec = 0
velocity_x, velocity_y = 0, 0
speed = 4
while True:

    for event in pygame.event.get():
        if event.type == 256:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:

            laser_sound.play()
            laser_rect = laser.get_rect(midbottom=(player_rect.midtop))
            laser_list.append(laser_rect)


            can_shoot = False
            start_time = pygame.time.get_ticks()
            print(start_time)
            print("shoot")
    dt = clock.tick(fps) / 1000



    screen.blit(background, (0, 0))
    screen.blit(player, player_rect)



    meteor_update(meteor_list, dt)
    laser_update(laser_list, dt)

    can_shoot = laser_time(can_shoot, 300)

    meteor_time += 30
    if meteor_time > 500:
        meteorli = meteor.get_rect(midbottom=(random.randint(0, WINDOW_W - 300), 0))
        meteor_list.append(meteorli)
        if meteor_time > 501:
            meteor_time = 0


    colli = meteor_player_collision(meteor_list)
    if colli == True:
        pygame.quit()
        sys.exit()

    mx, my = pygame.mouse.get_pos()
    player_rect.centerx = mx
    player_rect.centery = my

    pygame.display.update()


# By ThallysonKodex