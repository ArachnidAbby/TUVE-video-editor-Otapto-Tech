import pygame, ffmpeg, sys
pygame.init()
sys.path.insert(0, 'Resources\Tools')
from GuiTools import *
gameDisplay  = pygame.display.set_mode((1600,900),pygame.RESIZABLE)
pygame.display.set_caption("The Ultimate Video Editor")
icon = pygame.image.load('Resources\Image Files\T.png')
pygame.display.set_icon(icon)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running = False
            
        gameDisplay.fill((255,255,255))

        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        pygame.display.update()
pygame.quit()