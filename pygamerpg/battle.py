#battle -3
from config import *
#import random


class Battle:
    def __init__(self,game,screen):
        self.game=game
        self.screen=screen
        self.stamina=player_stamina
        self.hp=player_hp
        self.mp=player_mp
        self.color=[0,0,0]
        self.list=['ATTACK','MAGIC','DEFEND','RUN','INVENTORY','EQUIPMENT']
        self.font='fonts/Game-Font.ttf'
        self.posx=[60,200,60,220,600,320]
        self.posy=[400,400,450,450,425,25]
        self.atkposx=[50,20,600]
        self.atkposy=[300,250,250]
        self.angle=[320,320,320]
        self.atk=[]
        self.len=0
        self.block=1
        self.invposx=[600,600,680,680]
        self.invposy=[280,320,280,320]
        self.weapon=0
        self.spell=''
        self.spellno=0
        self.scroll=''
        #calcs
        self.timer=0
        self.turnofaction='player'
        self.word=''
        self.error=0
        self.temp=255
        self.ran=0
        self.time=pygame.time.get_ticks()
        self.wordlen=0
        #monster
        self.mhp=(1+player_lvl)*(100+random.randint(50,100)+random.randint(50,100))
        self.mhptemp=self.mhp
        self.confusion=0
        self.curse=0
        self.montext=''
        self.mch=10
        self.pastaction='player'
    def enemy_stats(self):
        pass
    def weaponcheck(self):
        if player_equip["weapon"]=='NONE' or 'REM_' in player_equip["weapon"]:
            self.weapon=1
        else:
            self.weapon=2
        if player_equip["armour"]=='NONE':
            self.block=1
        elif player_equip["armour"]=='BRONZE SET':
            self.block=0.9
        elif player_equip["armour"]=='SILVER SET':
            self.block=0.75
        elif player_equip["armour"]=='GOLD SET':
            self.block=0.5
    def scrollcheck(self):
        self.scroll= globals().get(player_equip["scroll"].lower())
        self.spell=self.scroll[self.spellno]
        
    def update(self,ch):
        self.game.typeerror=1
        if ch.lower()=='attack':
            self.weaponcheck()
            self.game.typeerror=0
            self.game.attack=1
            self.game.input_text=''
        if ch.lower()=='magic':
            self.game.typeerror=0
            if player_equip["scroll"]=='NONE':
                #print(self.temp)
                drawtext(self.screen,self.font,'*YOU DO NOT POSSES ANY SCROLL*','white',40,self.temp,(230,300))
                self.temp-=5
                if self.temp<=0:
                    self.temp=255
                    self.game.input_text=''
            else:
                self.game.typeerror=0
                self.game.input_text=''
                self.game.attack=2
        if ch.lower()=='defend':
            self.game.typeerror=0
            self.game.input_text=''
            self.game.attack=3
        if ch.lower()=='run':
            self.game.typeerror=0
            self.game.input_text=''
            self.game.player='ran'
        if ch.lower()=='inventory':
            self.game.typeerror=0
            self.temp=255
            self.game.attack=7
            self.game.input_text=''
        if self.game.attack==1 and self.atk:
            if ch.upper()==player_attack1[self.atk[0]] or ch.upper()==player_attack1[self.atk[1]] or ch.upper()==player_attack1[self.atk[2]]:
                self.game.typeerror=0
                self.word=ch
                self.game.attack=11             
                self.game.input_text=''
    def draw(self):
        pygame.draw.rect(self.screen,(255,255,255),(10,10,780,380),3)
        if self.game.action.burn>0:
            pygame.draw.rect(self.screen,(255,255,255),(15,15,40,45),1)
            drawtext(self.screen,self.font,str(self.game.action.burn),'white',15,255,(45,45))
        if self.game.action.lightning>0:
            pygame.draw.rect(self.screen,(255,255,255),(60,15,40,45),1)
            drawtext(self.screen,self.font,str(self.game.action.lightning),'white',15,255,(90,45))
        if self.game.action.water>0:
            pygame.draw.rect(self.screen,(255,255,255),(105,15,40,45),1)
            drawtext(self.screen,self.font,str(self.game.action.water),'white',15,255,(135,45))
        if self.game.action.earth>0:
            pygame.draw.rect(self.screen,(255,255,255),(150,15,40,45),1)
            drawtext(self.screen,self.font,str(self.game.action.water),'white',15,255,(180,45))
        if self.game.info==1:
            info(self.game,self.screen,self.font,self.hp,self.mp,self.stamina)
            pygame.draw.rect(self.screen,(255,255,255),(450,100,200,200),3)
            drawtext(self.screen,self.font,'*TAB*','white',40,255,(385,415))
        drawtext(self.screen,self.font,'*TAB*','white',40,90,(385,415))
        #pygame.draw.rect(self.screen,(255,255,255),(10,10,780,380),3)
        #pygame.draw.circle(self.screen, (255,255,255), [410, 30], 30, 3)
        #drawtext(self.screen,self.font,'MULTIPLIER','white',45,255,(345,20))
        drawtext(self.screen,self.font,'H',(self.hp*2.55,0,0),100,255,(350,400))
        drawtext(self.screen,self.font,'M',(0,0,self.mp*2.55),100,255,(450,400))
        drawtext(self.screen,self.font,'S',(self.stamina*2,self.stamina*2.55,0),100,255,(400,450))
        
        drawtext(self.screen,self.font,'ATTACK','white',60,90,(60,400))
        drawtext(self.screen,self.font,'MAGIC','white',60,90,(200,400))
        drawtext(self.screen,self.font,'DEFEND','white',60,90,(60,450))
        drawtext(self.screen,self.font,'RUN','white',60,90,(220,450))
        drawtext(self.screen,self.font,'EQUIPMENT','white',60,90,(320,25))
        drawtext(self.screen,self.font,'INVENTORY','white',60,90,(600,425))
        if self.game.attack==1:
            if not self.atk:
                self.atk= random.sample(range(0, len(player_attack1)), 3)
                #self.atk.append(random.randrange(len(player_attack2)))
            drawtext(self.screen,self.font,'ATTACK','white',60,255,(60,400))
            drawtext(self.screen,self.font,str(player_attack1[self.atk[0]]),'white',60,90,(50,300))
            drawtext(self.screen,self.font,str(player_attack1[self.atk[1]]),'white',60,90,(20,250))
            drawtext(self.screen,self.font,str(player_attack1[self.atk[2]]),'white',60,90,(600,250))
    def playerside(self,ch):
        if self.error==1:
            self.color[0]=189
            self.error=0
            self.hp-=1
            #print(self.hp)
        if self.color[0]>0 and self.error==0:
            self.color[0]-=6
            if self.color[0]<0:
                self.color[0]=0
        if self.game.attack==0:
            typing(self.game,self.screen,self.font,self.list,self.len,self.posx,self.posy,ch)
        elif self.game.attack==1:
            typing(self.game,self.screen,self.font,[player_attack1[self.atk[0]],player_attack1[self.atk[1]],player_attack1[self.atk[2]]],self.len,self.atkposx,self.atkposy,ch)
            self.wordlen=0
        elif self.game.attack==11:
            self.turnofaction='wait'
            drawtext(self.screen,self.font,self.word,'white',60,90,(350,300))
            self.timenow=pygame.time.get_ticks()
            if self.wordlen!=len(self.word) and self.timenow - self.time>300:
                self.wordlen+=1
                self.time=pygame.time.get_ticks()
                self.stamina-=self.weapon
            drawtext(self.screen,self.font,self.word[:self.wordlen],'white',60,255,(350,300))
            #print(self.stamina)
            if self.wordlen==len(self.word):
                self.mhptemp-=self.wordlen*self.weapon*(self.game.action.earth+1)
                #print(self.mhp , self.mhptemp)
                self.atk.clear()
                self.turnofaction='monster'
                self.game.attack=0
        elif self.game.attack==2:
            self.scrollcheck()
            drawtext(self.screen,self.font,self.spell,'white',40,90,(180,300))
            typingsingle(self.game,self.screen,self.font,self.spell,self.len,180,300,self.game.input_text,40)
            if self.game.input_text.upper()==self.spell:
                self.timer+=2*(len(self.scroll)-self.spellno)
                self.spellno+=1
                self.error=0
                self.game.input_text=''
            if self.spellno==len(self.scroll):
                self.game.typeerror=0
                self.game.input_text=''
                self.game.attack=0
                self.turnofaction='magic'
                self.game.action.scrolls(True)
        elif self.game.attack==3:
            drawtext(self.screen,self.font,'DEFEND','white',60,255,(60,450))
            drawtext(self.screen,self.font,'BLOCK ATTACK','white',40,90,(50,300))
            drawtext(self.screen,self.font,'INSPECT ENEMY','white',40,90,(300,300))
            drawtext(self.screen,self.font,'REGAIN COMPOSURE','white',40,90,(550,300))
            typing(self.game,self.screen,self.font,['BLOCK ATTACK','INSPECT ENEMY','REGAIN COMPOSURE'],self.len,[50,300,550],[300,300,300],ch,40)
        elif self.game.attack==7:
            if not player_battlebag:
                drawtext(self.screen,self.font,'*BAG IS EMPTY*','white',40,self.temp,(300,300))
                self.temp-=5
                if self.temp<=0:
                    self.game.attack=0
                    self.temp=255
            else:
                drawtext(self.screen,self.font,'INVENTORY','white',60,255,(600,425))
                pygame.draw.rect(self.screen,'white',(590,250,200,140),3)
                for x in player_battlebag:
                    drawtext(self.screen,self.font,x,'white',30,90,(self.invposx[player_battlebag.index(x)],self.invposy[player_battlebag.index(x)]))
                typing(self.game,self.screen,self.font,player_battlebag,self.len,self.invposx[:len(player_battlebag)],self.invposy[:len(player_battlebag)],ch,30)
                if ch.upper()=='H POTION' or ch.upper()=='M POTION' or ch.upper()=='S POTION':
                    if self.ran==0:
                        self.error=0
                        itemuse(self.game,self.screen,ch)
                    elif self.ran !=0:
                        pygame.draw.rect(self.screen,'black',(590,250,197,137))
                        self.error=0
                        self.temp-=10
                        if ch.upper()=='H POTION':
                            drawtext(self.screen,self.font,'*YOU HEALED 50 POINTS OF HEALTH*','white',40,self.temp,(230,300))
                        if ch.upper()=='M POTION':
                            drawtext(self.screen,self.font,'*YOU HEALED '+str(self.ran)+' POINTS OF MANA*','white',40,self.temp,(230,300))
                        if ch.upper()=='S POTION':
                            drawtext(self.screen,self.font,'*YOU HEALED '+str(self.ran)+' POINTS OF STAMINA*','white',40,self.temp,(230,300))
                    if self.temp<=0:
                        self.ran=0
                        remove(ch.upper())
                        self.game.input_text=''
                        self.game.attack=0
                        self.temp=255
    def initialstuff(self):
        if (self.turnofaction=='monster' or self.turnofaction=='player') and self.turnofaction!=self.pastaction:
            print(self.game.action.burn,self.game.action.lightning,self.game.action.earth)
            self.pastaction=self.turnofaction
            self.game.action.statuseffects()
            if self.game.action.burn>0:
                self.game.action.burn-=1
            elif self.game.action.lightning>0:
                self.game.action.lightning-=1
            elif self.game.action.earth>0:
                self.game.action.earth-=1
            elif self.game.action.water>0:
                self.game.action.water-=1
        if self.turnofaction=='magic':
            self.game.action.scrolls(True)
        elif self.turnofaction=='magicfail':
            self.game.action.scrolls(False)
        if self.hp>=player_hp:
            self.hp=player_hp
        if self.mhptemp>=self.mhp:
            self.mhptemp=self.mhp
        if self.mp>=player_mp:
            self.mp=player_mp
        if self.stamina>=player_stamina:
            self.stamina=player_stamina
        if self.hp<=0:
            self.game.player='dead'
            self.hp=0
        if self.mhptemp<=0:
            self.game.monster='dead'
            self.mhp=(1+random.randint(1,player_lvl))*100*random.randint(1,player_lvl)
            self.mhptemp=self.mhp*0.01
        if self.turnofaction=='player' and self.game.player=='alive':
            self.timenow=pygame.time.get_ticks()
            pygame.draw.rect(self.screen,'white',(360,360,110,30),3)
            pygame.draw.rect(self.screen,'white',(365,365,100-(self.timenow-self.time)/((timer+self.timer)*10),20))
            if self.timenow -self.time>(timer+self.timer)*1000:
                if self.game.attack==2:
                    self.turnofaction='magicfail'
                    self.game.attack=0
                    self.game.typeerror=0
                    self.game.input_text=''
                else:
                    self.turnofaction='timeup'
                self.time=pygame.time.get_ticks()
        elif self.turnofaction=='timeup':
            #print("hello",self.mhptemp)
            self.game.attack=0
            self.game.typeerror=0
            self.game.input_text=''
            drawtext(self.screen,self.font,'*TIME HAS RUN OUT*','white',40,self.temp,(300,300))
            self.temp-=5
            if self.temp<0:
                self.temp=255
                self.turnofaction='monster'
        elif self.turnofaction=='skip':
            drawtext(self.screen,self.font,"*THE CREATURE IS PARALYZED, UNABLE TO MOVE*",'white',40,self.temp,(190,300))
            self.temp-=4
            if self.temp<=0:
                self.game.action.defend=0
                self.turnofaction='player'
                self.temp=255
                self.game.attack=0
                self.time=pygame.time.get_ticks()
        elif self.turnofaction=='monster' and self.game.monster=='alive':
            self.game.input_text=''
            if self.mch>5:
                self.mch= random.randint(1,player_lvl)-1
            if self.mch==0 and self.game.action.defend==0:
                self.hp-=10*random.randint(1,player_lvl)*self.block
                self.montext='*THE CREATURE DECIDED TO ATTACK YOU*'
                self.mch=-1
            elif self.mch==1 and self.mhptemp<=self.mhp*0.50 and self.game.action.heal==0:
                self.mhptemp+=(self.mhp*0.25)*random.randint(1,player_lvl)
                #print("hello",self.mhp,self.mhp*0.5,self.mhptemp)
                self.game.action.heal=4
                self.montext='*THE CREATURE HEALED SOME OF ITS HEALTH*'
                self.mch=-1
            elif self.mch==2 and player_equip['weapon']!='NONE' and self.game.action.dearm==0 and self.game.action.defend==0:
                changeequip('weapon','REM_'+str(player_equip['weapon']))
                self.montext='*THE CREATURE TOSSED YOUR WEAPON AWAY*'
                self.game.action.dearm=7
                self.mch=-1
            elif self.mch==3 and self.confusion==0 and self.game.action.defend==0:
                self.hp-=30
                self.confusion=10
                self.game.conf=random.randint(0,1)
                self.montext='*THE CREATURE CURSES YOU WITH CONFUSION*'
                self.mch=-1
            elif self.mch==4 and self.curse!=1 and self.mhptemp<=self.mhp*0.35 and self.game.action.defend==0:
                self.montext='*THE CREATURE CHANTS A WEIRD CURSE ON YOU*'
                self.stamina=self.stamina*0.5
                self.hp=self.hp*0.75
                self.mp=player_mp*0.25
                self.curse=1
                self.mch=-1
            elif self.mch==5 and self.mhptemp<self.mhp*0.1 and self.game.action.run==0:
                self.montext='*THE CREATURE TRIES TO RUN AWAY FROM YOU*'
                self.game.action.run=20
                if random.randint(0,5)==5:
                    self.game.monster='ran'
                else:
                    self.montext='*THE CREATURE FAILED TO RUN AWAY FROM YOU*'
                    self.mch=-1
            elif self.mch in [0,2,3,4] and self.game.action.defend==1:
                self.montext='*THE CREATURE ATTACKED BUT YOU BLOCKED IT*'
                self.game.battle.stamina-=15
            elif self.mch!=-1:
                self.mch=random.randint(0,player_lvl)
            if self.montext:
                drawtext(self.screen,self.font,self.montext,'white',40,self.temp,(190,300))
                self.temp-=4
                if self.temp<=0:
                    self.game.action.defend=0
                    self.mch=10
                    self.turnofaction='player'
                    self.temp=255
                    self.game.attack=0
                    self.time=pygame.time.get_ticks()
    def main(self,inputtext):
        pygame.draw.rect(self.screen,self.color,(10,10,780,380))
        self.game.action.ranordead()
        self.initialstuff()
        self.update(inputtext)
        self.draw()
        self.playerside(inputtext)