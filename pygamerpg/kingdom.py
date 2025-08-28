from config import *

class Kingdom:
    def __init__(self,game,screen):
        self.game=game
        self.screen=screen
        self.list=['CHURCH','BLACKSMITH','TAVERN','SHAMAN','MARKET PLACE','GUILD']
        self.font='fonts/Game-Font.ttf'
        self.posx=[370,60,100,600,330,620]
        self.posy=[400,400,450,450,450,400,10]
        self.len=0
        self.time=0
        self.day=0
        self.size=60
        #other
        self.place=0
    def update(self):
        if self.game.input_text.upper()=="RETURN":#heal/story/oracle
            self.place=0
            self.game.input_text=''
            self.list=['CHURCH','BLACKSMITH','TAVERN','MARKET PLACE','SHAMAN','GUILD']
            self.posx=[370,60,100,600,330,620]
            self.posy=[400,400,450,450,450,400,10]
            self.size=60
        if self.game.input_text.upper()=="CHURCH":#heal/story/oracle
            pass
        if self.game.input_text.upper()=="BLACKSMITH":#equipments/tips
            pass
        if self.game.input_text.upper()=="TAVERN":#sleep/quest/ food
            self.place=2
            self.game.input_text=''
            self.list=['DRINK','SLEEP','BUY RATIONS','RETURN']
            self.posx=[60,200,90,380,560,590]
            self.posy=[400,400,450,425,400,450]
            self.size=60
        if self.game.input_text.upper()=="GUILD":#quest/remove equipment
            self.place=1
            self.game.input_text=''
            self.list=['JOBS','RANK','DONATIONS','RETURN','JOIN GUILD','VENTURE']
            self.posx=[60,200,90,380,560,590]
            self.posy=[400,400,450,425,400,450]
            self.size=60
        if self.game.input_text.upper()=="SHAMAN":#potions/herbs/scrolls
            pass
        if self.game.input_text.upper()=="CULT":
            pass
    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255),(10,10,780,380),3)
        if self.place==0:
            drawtext(self.screen,self.font,'CHURCH','white',60,90,(370,400))
            drawtext(self.screen,self.font,'BLACKSMITH','white',60,90,(60,400))
            drawtext(self.screen,self.font,'TAVERN','white',60,90,(100,450))
            drawtext(self.screen,self.font,'SHAMAN','white',60,90,(600,450))
            drawtext(self.screen,self.font,'MARKET PLACE','white',60,90,(330,450))
            drawtext(self.screen,self.font,'GUILD','white',60,90,(620,400))
        if self.place==1:
            drawtext(self.screen,self.font,'JOBS','white',60,90,(60,400))
            drawtext(self.screen,self.font,'RANK','white',60,90,(200,400))
            drawtext(self.screen,self.font,'DONATIONS','white',60,90,(90,450))
            drawtext(self.screen,self.font,'RETURN','white',60,90,(380,425))
            drawtext(self.screen,self.font,'JOIN GUILD','white',60,90,(560,400))
            drawtext(self.screen,self.font,'VENTURE','white',60,90,(590,450))
            self.game.place.guild()
        typing(self.game,self.screen,self.font,self.list,self.len,self.posx,self.posy,self.game.input_text,self.size)
        
    def main(self,inptxt):
        self.update()
        self.draw()