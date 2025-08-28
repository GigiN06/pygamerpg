from config import *
class StartPage:
    def __init__(self,game,screen):
        self.game=game
        self.screen=screen
        self.font='fonts/Game-Font.ttf'
        self.start='START'
        self.quit='QUIT'
        self.alpha1=0
        self.alpha2=0
        self.y1=200
        self.y2=350
        self.lock=0
#         self.start=pygame.rect()
#         self.exit=pygame.rect()
    def draw(self):
        drawtext(self.screen,self.font,'START','white',160,90,(300,200))
        drawtext(self.screen,self.font,'QUIT','white',60,80,(370,350))
    def userinput(self,inputtext):
        inputtext=inputtext.upper()
        self.len=len(inputtext)
        if inputtext=='':
            self.alpha1=0
            self.alpha2=0
        elif inputtext==self.start[:self.len]:
            drawtext(self.screen,self.font,inputtext,'white',160,255,(300,200))
            self.alpha1=255
            self.alpha2=0
        elif inputtext==self.quit[:self.len]:
            drawtext(self.screen,self.font,inputtext,'white',60,255,(370,350))
            self.alpha2=255
            self.alpha1=0
        else:
            if self.lock==0:
                self.lock=len(inputtext)
            drawtext(self.screen,self.font,inputtext[:self.lock].lower(),'white',160,self.alpha1,(300,self.y1))
            drawtext(self.screen,self.font,inputtext[:self.lock].lower(),'white',60,self.alpha2,(370,self.y2))
            if self.alpha1<0 and self.alpha2<0:
                self.lock=0
                self.game.input_text=''
                inputtext=''
                self.y1=200
                self.y2=350
            else:
                self.alpha1-=10
                self.alpha2-=10
                self.y1+=1
                self.y2+=1
    def main(self,inptxt):
        self.draw()
        self.userinput(inptxt)