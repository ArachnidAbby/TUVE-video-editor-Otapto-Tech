import pygame, ffmpeg, sys
pygame.init()
sys.path.insert(0, 'Resources\Tools')
from GuiTools import *
gameDisplay  = pygame.display.set_mode((1600,900),pygame.RESIZABLE)
pygame.display.set_caption("The Ultimate Video Editor")
icon = pygame.image.load('Resources\Image Files\T.png')
pygame.display.set_icon(icon)


running = True
class FileDropDown:
        def __init__(self):
                self.toggle = False
                self.file = button(0,0,100,50)
                self.newFile = button(0,0,100,50)
		self.openFile = button(0,50,100,50)
		self.saveFile = button(0,100,100,50)
		self.saveAsFile = button(0,150,100,50)
		self.importMedia = button(0,200,100,50)
		self.exportProject= button(0,250,100,50)
	def update(self):
		self.newFile.update()
		self.openFile.update()
		self.saveFile.update()
		self.saveAsFile.update()
		self.importMedia.update()
		self.exportProject.update()
        def show(self):
                g = self.file.hover or self.newFile.hover or self.saveFile.hover
                if self.file.once:
                        self.toggle =True
                if g:
                        if self.toggle:
                                self.newFile.render(gameDisplay)
		                self.openFile.render(gameDisplay)
		                self.saveFile.render(gameDisplay)
		                self.saveAsFile.render(gameDisplay)
		                self.importMedia.render(gameDisplay)
		                self.exportProject.render(gameDisplay)
                else:
                        self.toggle = False
FileDrop = FileDropDown()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running = False
        FileDrop.update()
        
        gameDisplay.fill((255,255,255))

        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        FileDrop.show()
        pygame.display.update()
pygame.quit()