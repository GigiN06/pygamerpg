from config import *

class Places:
    def __init__(self,game,screen):
        self.game=game
        self.screen=screen
        self.typed=0
        self.len=0
        self.temp=255
        self.drunk=0
        self.font='fonts/Game-Font.ttf'
        #print statement
        self.size=[]
        self.text=[]
        self.posx=[]
        self.posy=[]
        self.alph=[]
    def tavern(self):
        if self.game.input_text.upper()=='DRINK' and money>=25:
            self.drunk=15 #x2 damage end this -50% health
            #-25 money
            self.game.input_text=''
        if self.game.input_text.upper()=='SLEEP' and money>=50:
             self.day+=1 #next day
             self.time=0 #morning
             self.game.input_text=''
             if self.game.battle.hp<player_hp:
                 self.game.battle.hp+=random.randint(10,25)
                 if self.game.battle.hp>player_hp:
                     self.game.battle.hp=player_hp
             #-50 money
        if self.game.input_text.upper()=='BUY RATIONS':
            self.typed=21
            self.game.input_text=''
            self.game.kingdom.list=['BUY RATIONS','CUSTOMARY DISH MENU','PICK 2 INGRIDIENTS','','','','','','','','']
            self.game.kingdom.posx=[60,60,60,60]
            self.game.kingdom.posy=[110,140,170,200]
            self.game.kingdom.size=40
    def guild(self):
        pygame.draw.rect(self.screen,(255,255,255),(50,50,380,280),3)
        if self.game.input_text.upper() in ('JOBS', 'DONATIONS', 'RANK') and guild=='none':
            self.draw("*REQUIRED TO BE PART OF A GUILD TO PERFORM ACTION*") 
        elif self.game.input_text.upper()=='JOBS':
            self.typed=11
            self.game.input_text=''
            self.game.kingdom.list=['ROOKIE TRAINING','RECEPTION DUTY','PREACH FOR THE GUILD','FINAL QUEST']
            self.game.kingdom.posx=[60,60,60,60]
            self.game.kingdom.posy=[110,140,170,200]
            self.game.kingdom.size=40
        elif self.game.input_text.upper()=='RANK': #fire,water,earth,lightning 
            self.typed=12
            self.game.kingdom.list=['IMBUE WEAPON WITH THE POWER OF '+str(guild.upper()),'IMPRINT ARMOUR WITH THE CREST OF '+str(guild.upper()),'BECOME ONE WITH '+str(guild.upper())]
            self.game.kingdom.posx=[60,60,60]
            self.game.kingdom.posy=[170,200,230]
            self.game.kingdom.size=30
            self.game.input_text=''
        elif self.game.input_text.upper()=='DONATIONS':
            self.typed=13
            self.game.kingdom.list=['SMALL DONATION','MEDIUM DONATION','HUGE DONATION','DONATE EVERYTHING']
            self.game.kingdom.posx=[60,60,60,60]
            self.game.kingdom.posy=[125,155,185,215]
            self.game.kingdom.size=40
            self.game.input_text=''
        if self.game.input_text.upper()=='VENTURE':
            self.typed=14
            self.game.input_text=''
        if self.game.input_text.upper()=='JOIN GUILD':
            self.typed=15
            self.game.kingdom.list=glist
            self.game.kingdom.posx=[60,250,60,250]
            self.game.kingdom.posy=[125,125,250,250]
            self.game.kingdom.size=40
            self.game.input_text=''
        self.action()

    def action(self):
        if self.typed==0:
            self.game.kingdom.list=['JOBS','RANK','DONATIONS','RETURN','JOIN GUILD','VENTURE']
            self.game.kingdom.posx=[60,200,90,380,560,590]
            self.game.kingdom.posy=[400,400,450,425,400,450]
            self.game.kingdom.size=60
        if self.typed==11:
            self.text=['JOBS','GUILD JOBS','ROOKIE TRAINING','RECEPTION DUTY','PREACH FOR THE GUILD','FINAL QUEST','*PRESS ESCAPE TO GO BACK*']
            self.size=[60,60,40,40,40,40,25]
            self.posx=[60,170,60,60,60,60,160]
            self.posy=[400,70,110,140,170,200,300]
            self.alph=[255,255,90,90,90,90,255]
            drawmultiple(self.screen,self.font,self.text,'white',self.size,self.alph,self.posx,self.posy)
        if self.typed==12:
            self.text=['RANK','GUILD STATS','RANK :','GUILD PERKS','IMBUE WEAPON WITH THE POWER OF FIRE','IMPRINT ARMOUR WITH THE CREST OF FIRE','BECOME ONE WITH FIRE','*PRESS ESCAPE TO GO BACK*']
            self.size=[60,50,40,40,30,30,30,25]
            self.posx=[200,170,190,60,60,60,60,160]
            self.posy=[400,70,110,140,170,200,230,300]
            self.alph=[255,255,255,255,90,90,90,255]
            drawmultiple(self.screen,self.font,self.text,'white',self.size,self.alph,self.posx,self.posy)
        if self.typed==13:
            self.text=['DONATIONS','DONATION BOARD','SMALL DONATION','MEDIUM DONATION','HUGE DONATION','DONATE EVERYTHING','*PRESS ESCAPE TO GO BACK*']
            self.size=[60,50,40,40,40,40,25]
            self.posx=[90,150,60,60,60,60,160]
            self.posy=[450,70,125,155,185,215,300]
            self.alph=[255,255,90,90,90,90,255]
            drawmultiple(self.screen,self.font,self.text,'white',self.size,self.alph,self.posx,self.posy)
        if self.typed==14:
            pass #Knight duty(),gather resources(),MOnster hunting(battle),dragon hunting()
        if self.typed==15:
            self.text=['JOIN GUILD','GUILDS','FIRE','WATER','EARTH','LIGHTNING','*PRESS ESCAPE TO GO BACK*']
            self.size=[60,50,40,40,40,40,25]
            self.posx=[560,190,60,250,60,250,160]
            self.posy=[400,70,125,125,250,250,300]
            self.alph=[255,255,90,90,90,90,255]
            drawmultiple(self.screen,self.font,self.text,'white',self.size,self.alph,self.posx,self.posy)
            if self.game.input_text.lower()==guild:
                self.draw("*YOU ARE ALREADY A PART OF THE "+str(guild.upper())+" GUILD*")
    def draw(self,text):
        drawtext(self.screen,self.font,text,'white',30,self.temp,(190,360))
        self.temp-=3
        if self.temp<=0:
            self.temp=255
            self.game.input_text=''
            