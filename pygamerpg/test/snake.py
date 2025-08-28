import pygame,random,time
from config import *
pygame.init()

def displaytext(screen,text,size,color,pos,alph):
    font=pygame.font.Font('fonts/Game-Font.ttf',size)
    text_surface=font.render(text,True,color)
    text_surface.set_alpha(alph)
    text_rect=text_surface.get_rect()
    text_rect.x=pos[0]
    text_rect.y=pos[1]
    screen.blit(text_surface,text_rect)


def defeated():
    for body in game.snake.snake_body:
        pass
    game.snake.snake_pos=[(win_width/2)-10,(win_height/2)-10]
    game.snake.snake_body=[game.snake.snake_pos]
    game.snake.snake_direction='center'
    
class stats:
    def __init__():
        pass

class Snake:
    def __init__(self,screen):
        self.snake_value=1
        self.snake_direction='center'
        self.snake_pos=[(win_width/2)-10,(win_height/2)-10]
        self.snake_rect=pygame.Rect(self.snake_pos[0],self.snake_pos[1],10,10)
        self.snake_body=[self.snake_pos]
        self.screen=screen
    def update(self):
        if self.snake_direction=='left':
            self.snake_pos[0]-=10
        elif self.snake_direction=='right':
            self.snake_pos[0]+=10
        elif self.snake_direction=='up':
            self.snake_pos[1]-=10
        elif self.snake_direction=='down':
            self.snake_pos[1]+=10
        self.snake_rect=pygame.Rect(self.snake_pos[0],self.snake_pos[1],10,10)
    def draw(self):
        for pos in self.snake_body:
            pygame.draw.rect(self.screen,(255,255,255),(pos[0],pos[1],10,10))
    def main(self):
        self.update()
        self.draw()
        
class Apple:
    def __init__(self,screen):
        self.screen=screen
        self.apple_exist=True
        self.apple_pos=[random.randint(25,win_width-25),random.randint(25,win_height-25)]
        self.apple_rect=pygame.Rect(self.apple_pos[0],self.apple_pos[1],10,10)
    def update(self):
        game.snake.snake_body.insert(0,list(game.snake.snake_pos))
        if self.apple_exist==False:
            self.apple_exist=True
            self.apple_pos=[random.randrange(30,650//10)*10,random.randrange(30,350//10)*10]
            print(self.apple_pos)
            self.apple_rect=pygame.Rect(self.apple_pos[0],self.apple_pos[1],10,10)
        if pygame.Rect.colliderect(self.apple_rect, game.snake.snake_rect):
            self.apple_exist=False
            game.snake.snake_value+=1
        else:
            game.snake.snake_body.pop()
    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255),(self.apple_pos[0],self.apple_pos[1],10,10))
    def main(self):
        self.update()
        self.draw()
class Game:
    def __init__(self):
        self.screen=pygame.display.set_mode((win_width,win_height))
        self.run=True
        self.defeat_status=False
        self.clock=pygame.time.Clock()
        self.alpha=0
        self.reason=''
    def envi(self):
        pygame.draw.rect(self.screen,(255,255,255),(0,0,win_width,win_height),3)
        displaytext(self.screen,'Score : '+str(game.snake.snake_value),30,(255,0,0),(370,450),255)
    def create(self):
        self.snake=Snake(self.screen)
        self.apple=Apple(self.screen)
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.run=False
            if event.type==pygame.KEYDOWN:
                if self.defeat_status==True:
                    game.snake.snake_value=1
                self.defeat_status=False
                if event.key==pygame.K_LEFT and self.snake.snake_direction!='right':
                    self.snake.snake_direction='left'
                if event.key==pygame.K_RIGHT and self.snake.snake_direction!='left':
                    self.snake.snake_direction='right'
                if event.key==pygame.K_UP and self.snake.snake_direction!='down':
                    self.snake.snake_direction='up'
                if event.key==pygame.K_DOWN and self.snake.snake_direction!='up':
                    self.snake.snake_direction='down'
                if event.key==pygame.K_ESCAPE:
                   self.defeat_status=True
    def defeat(self):
        for snek in self.snake.snake_body[1:]:
            if snek[0]==self.snake.snake_pos[0] and snek[1]==self.snake.snake_pos[1]:
                self.defeat_status=True
                self.reason='Snake crashed into itself'
        if self.snake.snake_pos[0]<0 or self.snake.snake_pos[0]>win_width-10:
            self.defeat_status=True
            self.reason='Snake went out of bounds'
        if self.snake.snake_pos[1]<0 or self.snake.snake_pos[1]>win_height-10:
            self.defeat_status=True
            self.reason='Snake went out of bounds'
    def update(self):
        self.defeat()
        self.events()
    def draw(self):
        self.screen.fill((0,0,0))
        self.envi()
        self.clock.tick(25)
        self.apple.main()
        self.snake.main()
        if self.defeat_status==True:
            defeated()
            self.alpha=255
        if self.alpha!=0 and self.defeat_status==False:
            self.alpha-=20
        displaytext(self.screen,'Game Over',120,(255,0,0),(250,100),self.alpha)
        displaytext(self.screen,self.reason,60,(255,0,0),(200,160),self.alpha)
        pygame.display.flip()
    def main(self):
        self.update();
        self.draw()
    
    
game=Game()
game.create()
while game.run:
    game.main()
   
pygame.quit()   