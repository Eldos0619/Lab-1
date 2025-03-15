import pygame
import sys
import time
import math

pygame.init()

WIDTH=1400
HEIGHT=1050
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock=pygame.image.load("clock.png")
Minut=pygame.image.load("rightarm.png")
Sec=pygame.image.load("leftarm.png")

def draw_hand(image,angle,pos):
    rotate_image=pygame.transform.rotate(image,-angle)
    rect=rotate_image.get_rect(center=pos)
    screen.blit(rotate_image,rect)
run=True
while run:
    screen.fill((0,0,0))
    screen.blit(clock,(0,0))

    ltime = time.localtime()
    second = ltime.tm_sec
    minut = ltime.tm_min

    minut_angle=minut * 6
    second_angle = second * 6

    draw_hand(Minut,minut_angle,(WIDTH//2,HEIGHT//2))
    draw_hand(Sec, second_angle, (WIDTH // 2, HEIGHT // 2))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
pygame.quit()
sys.exit()


