import pygame
pygame.init()

#Width, Height
#X Position, Y Position
#Passive Color, Hover Color, Active Color
#Text, Text Color
#Border Thickness, Border Color
#Icon

#x = GUITools.button(91090921)]
#x.update()
#if x.action:
    #jdopjsdpof

class color:
    black = (0,0,0)
    darkGray = (64,64,64)
    gray = (128,128,128)
    lightGray = (192,192,192)
    white = (255,255,255)
    pink = (255,0,128)
    red = (255,0,0)
    orange = (255,128,0)
    yellow = (255,255,0)
    green = (0,255,0)
    blue = (0,0,255)
    purple = (128,0,255)

class button:
    def __init__(self,x,y,w,h,icon="--ignor--"):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hover = False
        self.pressed = False
        self.once = False
        self.ac = color.black
        self.pc = color.gray
        if icon =="--ignor--":
            self.icon = False
        if icon != "--ignor--":
            self.icon = icon
    def update(self):
        MPos = pygame.mouse.get_pos()
        MClic = pygame.mouse.get_pressed()
        if self.pressed:
            self.once = False
        if MPos[0] >= self.x and MPos[1] >= self.y:
            if MPos[0] <= self.w+self.x and MPos[1] <= self.h+self.y:
                self.hover = True
                if MClic[0]==1:
                    if not self.pressed:
                        self.once = True
                    self.pressed = True
                else:
                    self.pressed = False
                    self.once = False
        else:
            self.hover = False
    def ChangeColors(self,pc, ac = color.black):
        self.ac = ac
        self.pc = pc
    def render(self, display):
        if self.pressed:
            pygame.draw.rect(display,self.pc,(self.x,self.y,self.w,self.h))
        else:
            pygame.draw.rect(display,self.ac,(self.x,self.y,self.w,self.h))