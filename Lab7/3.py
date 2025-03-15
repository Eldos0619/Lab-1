import pygame
from pygame.examples.sprite_texture import running

pygame.init()

screen=pygame.display.set_mode((800,800))
pygame.display.set_caption("Ball Game")

white=(255,255,255)
red=(255,0,0)

x,y=400,400
radius=25
move=20

run=True
while run:
    screen.fill(white)
    pygame.draw.circle(screen,red,(x,y),radius)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and y-radius-move>=0:
                y-=move
            elif event.key==pygame.K_DOWN and y+radius+move<=800:
                y+=move
            elif event.key==pygame.K_LEFT and x-radius-move>=0:
                x-=move
            elif event.key==pygame.K_RIGHT and x+radius+move<=800:
                x+=move
    pygame.display.flip()
pygame.quit()