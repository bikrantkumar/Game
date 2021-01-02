# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:23:57 2020

@author: aa
"""


import pygame
pygame.init()
win=pygame.display.set_mode((500,480))
run=True
x=50
y=425
height=64
width=64
vel=10
isjump=False
jumpcount=10
left=False
right=False
walkcount=0
clock=pygame.time.Clock()


pygame.display.set_caption("trial1")
bg=pygame.image.load("bg.jpg")
char =pygame.image.load("standing.png")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]



def redraw():
    walkcount =0
    win.blit(bg,(0,0))
    if walkcount+1 >=27:
        walkcount=0
    if left:
        win.blit(walkLeft[walkcount//3],(x,y))
        walkcount+=1
    elif right:
        win.blit(walkRight[walkcount//3],(x,y))
        walkcount+=1
    else:
        win.blit(char,(x,y))
        
        
    pygame.display.update()
    
def check(x):
    if x<500:
        return 1
    else:
        return 0
    
while run:
    clock.tick(27)
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           run =False
           
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
            x =x-vel
            left=True
            right=False
    
    elif keys[pygame.K_RIGHT] and check(x+width):
            x =x+vel
            left=False
            right=True
    else:
         left=False
         right=False
    if not(isjump):  
        if keys[pygame.K_DOWN] and check(y+height+20):
                y=y+vel 
        
        if keys[pygame.K_UP] and y>0:
                y =y-vel
        if keys[pygame.K_SPACE]:
               isjump=True
    else :
       if  jumpcount>=-10:
           if jumpcount<0:
               neg=-1
           else: 
               neg=1
           y=y-(jumpcount**2)*0.5*neg
           jumpcount=jumpcount -1
           
       else:
           isjump=False
           jumpcount=10
        
    redraw()
            
   
pygame.quit()