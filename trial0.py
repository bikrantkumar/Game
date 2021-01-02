import pygame
pygame.init()
win=pygame.display.set_mode((500,480))


pygame.display.set_caption("trial1")
bg=pygame.image.load("bg.jpg")
char =pygame.image.load("standing.png")
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
clock=pygame.time.Clock()
font=pygame.font.SysFont("comicsans",30,True,True)
bulletsound=pygame.mixer.Sound("bullet.wav")
hitsound=pygame.mixer.Sound("hit.wav")
music = pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
class player(object):
    def __init__(self,x,y,height,width,vel):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.vel=vel
        self.isjump=False
        self.walkcount=0
        self.left=False
        self.right=False
        self.isjump=False
        self.jumpcount=10
        self.isstanding=True
        self.hitbox=(self.x,self.y,32,32)
        
    def draw(self,win):
        if not(self.isstanding):
            if self.walkcount+1 >=27:
                self.walkcount=0
            if self.left:
                win.blit(walkLeft[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            elif self.right:
                win.blit(walkRight[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox=(self.x+20,self.y+16,32,46)
        #pygame.draw.rect(win,(255,0,0),self.hitbox,1)       

    def hit(self,win):
        self.isjump=False
        self.jumpcount=10
        self.x=30
        self.y=425
        print("selfhit")
        foul=pygame.font.SysFont("comicsans",100,True,True)
        text=foul.render("YOU GOT HIT",1,(255,0,0))
        win.blit(text,(250-text.get_width()/2,240))
        pygame.display.update(
            )
        pygame.time.delay(1000)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
            

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=10*facing
        
        
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

class enemy(object): 
    def __init__(self,x,y,vel,height,width,end):
        ~50,425,10,450
        self.x=x
        self.y=y
        self.vel=vel
        self.height=height
        self.width=width
        self.path=[x,end]
        self.walkcount=0
        self.hitbox=(self.x,self.y,32,32)
        self.health=10
        self.visible=True
    walkleft=[pygame.image.load("L%sE.png"%frame) for frame in range(1,12)]
    walkright=[pygame.image.load("R%sE.png"%frame) for frame in range(1,12)]
    def move(self):
        if self.x+self.vel<self.path[0]:
            self.vel=self.vel*-1
            self.x=self.x+self.vel
            
            
        elif self.x+ self.vel>self.path[1]:
            self.vel=self.vel*-1
            self.x=self.x+self.vel
            
        else:
            self.x=self.x+self.vel
           
    def draw(self,win):
        if self.visible:
            self.move()
            if self.walkcount>=33:
                self.walkcount=0
            if self.vel>0:
                win.blit(self.walkright[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            else:
                 win.blit(self.walkleft[self.walkcount//3],(self.x,self.y))
                 self.walkcount+=1
            self.hitbox=(self.x+20,self.y,32,64)
            pygame.draw.rect(win,(255,0,0),(self.x,self.y-20,100,10))
            pygame.draw.rect(win,(0,255,0),(self.x,self.y-20,100-10*(10-self.health),10))
            #pygame.draw.rect(win,(255,0,0),self.hitbox,1)

    def hit(self):
        
        if self.health==0:
            self.visible=False
            print(self.visible)
        else:
            self.health+=-1
        print("hit")
        hitsound.play()
        

        
def redraw():
    win.blit(bg,(0,0))
    man.draw(win)
    text=font.render("Score:"+str(score),1,(0,0,0))
    win.blit(text,(390,0))
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
   
    
def check(x):
    if x<500:
        return 1
    else:
        return 0
    
goblin=enemy(80,425,3,64,64,300)    
man=player(30,425,64,64,10)
run=True
bullets=[]
shootloop=0
score=0

while run:
    clock.tick(27)
    if shootloop>0:
        shootloop+=1
    if shootloop>=3:
        shootloop=0

    if goblin.visible: 
        if man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0] and man.hitbox[0]<goblin.hitbox[0]+goblin.hitbox[2]:
            if man.hitbox[1]+man.hitbox[3]>goblin.hitbox[1] and man.hitbox[1]<goblin.hitbox[1]+goblin.hitbox[3]:
                score-=5
                man.hit(win)
           
            
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run =False       
    for bullet in bullets:
         if goblin.visible:
             if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x+bullet.radius<goblin.hitbox[0]+goblin.hitbox[2]:
                if bullet.y+bullet.radius>goblin.hitbox[1] and bullet.y+bullet.radius<goblin.hitbox[1]+goblin.hitbox[3]:
                    goblin.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet))
             if bullet.x<500 and bullet.x>0:
                 bullet.x=bullet.x+ bullet.vel
             else:
                 bullets.pop((bullets.index(bullet)))
         else:
            if bullet.x<500 and bullet.x>0:
                bullet.x=bullet.x+bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

            
            
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_RETURN] and shootloop==0:
        if man.left:
            facing=-1
        else:
            facing=1
        if len(bullets)<5:
            bullets.append(projectile(round(man.x + man.width//2),round(man.y + man.height//2),5,(255,0,0),facing))
        shootloop=1
        bulletsound.play()
            
        
    if keys[pygame.K_LEFT] and man.x > 0:
        man.x =man.x-man.vel
        man.left=True
        man.right=False
        man.isstanding=False
    elif keys[pygame.K_RIGHT] and check(man.x+man.width):
            man.x =man.x+man.vel
            man.left=False
            man.right=True
            man.isstanding=False
    else:
        man.isstanding=True

    if not(man.isjump):  
        if keys[pygame.K_DOWN] and check(man.y+man.height+20):
                man.y=man.y+man.vel 
        
        if keys[pygame.K_UP] and man.y>0:
                man.y =man.y-man.vel
        if keys[pygame.K_SPACE]:
               man.isjump=True
    else :
       if  man.jumpcount>=-10:
           if man.jumpcount<0:
               neg=-1
           else: 
               neg=1
           man.y=man.y-(man.jumpcount**2)*0.5*neg
           man.jumpcount=man.jumpcount -1
           
       else:
           man.isjump=False
           man.jumpcount=10
        
    redraw()
            
   
pygame.quit()