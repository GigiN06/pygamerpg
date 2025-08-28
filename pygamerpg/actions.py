#battle -3
from config import *

class Actions:
    def __init__(self,game,screen):
        self.game=game
        self.screen=screen
        self.font='fonts/Game-Font.ttf'
        self.confusion=self.game.battle.confusion
        self.heal=0
        self.equipment=''
        self.defend=0
        self.invposx=[320,320,320,320,420,420,420,420]
        self.invposy=[140,180,220,260,140,180,220,260]
        self.len=0
        self.dearm=0
        self.run=0
        self.player=0
        self.time=pygame.time.get_ticks()
        self.temp=255
        self.txt=''
        self.spellmistake=0
        self.spellstatus=-1
        self.spelflg=0
        self.burn=self.lightning=self.earth=self.water=self.earth=0
    def other(self):
        if self.game.input_text.upper()=='EQUIPMENT' :
            self.game.battle.error=0
            self.game.attack=4
            self.game.input_text=''
        if self.game.attack==4:
            drawtext(self.screen,self.font,'EQUIPMENT','white',60,255,(320,25))
            pygame.draw.rect(self.screen,'black',(300,100,200,200))
            pygame.draw.rect(self.screen,'white',(300,100,200,200),3)
            drawtext(self.screen,self.font,'WEAPON','white',35,90,(310,110))
            drawtext(self.screen,self.font,'ARMOUR','white',35,90,(310,140))
            drawtext(self.screen,self.font,'SCROLL','white',35,90,(310,170))
            typing(self.game,self.screen,self.font,['WEAPON','ARMOUR','SCROLL'],self.len,[310,310,310],[110,140,170],self.game.input_text,35)
        if self.game.input_text.upper() in ['WEAPON','ARMOUR','SCROLL']:
            self.equipment=self.game.input_text.lower()
            self.game.attack=41
            self.game.battle.error=0
            self.game.input_text=''
        if self.game.attack==41:
            drawtext(self.screen,self.font,'EQUIPMENT','white',60,255,(320,25))
            pygame.draw.rect(self.screen,'black',(300,100,200,200))
            pygame.draw.rect(self.screen,'white',(300,100,200,200),3)
            drawtext(self.screen,self.font,'CHOOSE '+str(self.equipment.upper()),'white',40,255,(310,110))
            for x in player_inventory:
                    drawtext(self.screen,self.font,x,'white',30,90,(self.invposx[player_inventory.index(x)],self.invposy[player_inventory.index(x)]))
            typing(self.game,self.screen,self.font,player_inventory,self.len,self.invposx[:len(player_inventory)],self.invposy[:len(player_inventory)],self.game.input_text,30)
            if self.equipment.upper()=='WEAPON' and self.game.input_text.upper() in ['AXE','SWORD','DAGGER']:
                inventory(1,self.equipment.lower(),self.game.input_text.upper())
                self.game.battle.error=0
                self.game.input_text=''
                self.game.attack=0
            elif self.equipment.upper()=='ARMOUR' and self.game.input_text.upper() in ['BRONZE SET','SILVER SET','GOLD SET']:
                inventory(1,self.equipment.lower(),self.game.input_text.upper())
                self.game.battle.error=0
                self.game.input_text=''
                self.game.attack=0
            elif self.equipment.upper()=='SCROLL' and self.game.input_text.upper() in ['FIRE','LIGHTNING','WATER','EARTH']:
                inventory(1,self.equipment.lower(),self.game.input_text.upper())
                self.game.battle.error=0
                self.game.input_text=''
                self.game.attack=0
    def statuseffects(self):
        if self.burn>0:
            self.game.battle.mhptemp-=player_lvl*random.randint(1,self.burn)
        if self.lightning>0:
            if self.game.battle.turnofaction=='monster':
                self.game.battle.turnofaction='skip'
        if self.water>0:
            self.game.battle.hp+=player_lvl*random.randint(1,15)
    def defence(self):
        if self.game.input_text.upper()=='BLOCK ATTACK':
            self.defend=1
            self.txt='*YOU BRACED YOURSELF TO TANK AN ATTACK*'
        elif self.game.input_text.upper()=='INSPECT ENEMY':
            self.txt='*THE HEALTH OF THE MONSTER IS *'+str(self.game.battle.mhptemp)+"/"+str(self.game.battle.mhp)
        elif self.game.input_text.upper()=='REGAIN COMPOSURE':
            self.h=player_lvl*random.randint(-10,25)
            self.m=player_lvl*random.randint(-5,10)
            self.s=random.randint(-25,50)
            self.game.battle.hp+=self.h
            self.game.battle.mp+=self.m
            self.game.battle.stamina+=self.s
            self.txt='*PLAYER REGAINED '+str(self.h)+' HP '+str(self.m)+' MP '+str(self.s)+' STAMINA'
        if self.txt!='':
            self.game.battle.error=0
            self.game.input_text=''
            self.game.attack=0
            drawtext(self.screen,self.font,self.txt,'white',30,self.temp,(230,300))
            self.temp-=3
            if self.temp<=0:
                self.txt=''
                self.game.battle.turnofaction='monster'
                self.temp=255
    def scrolls(self,status):
        if status:
            if self.spellmistake>15:
                self.txt='*THE SPELL INCANTATION WAS ALRIGHT*'
                self.spellstatus=100-self.spellmistake
            elif self.spellmistake>60:
                self.txt='*THE SPELL INCANTATION FAILED BADLY*'
                self.spellstatus=0
            elif self.spellmistake==0:
                self.txt='*THE SPELL INCANTATION WAS PERFECT*'
                self.spellstatus=200
            else:
                self.txt='*THE SPELL INCANTATION WAS GOOD*'
                self.spellstatus=random.randint(85,95)
        else:
            if self.spellmistake>(self.game.battle.spellno+2)*10:
                self.txt='*THE SPELL INCANTATION FAILED BADLY*'
                self.spellstatus=0
            else:
                self.txt='*YOU FAILED TO COMPLETE BUT . . . . . .*'
                self.spellstatus=(self.game.battle.spellno*100)//len(self.game.battle.scroll)
        if self.spellstatus!=0 and self.spelflg==0:
            print("spell status",self.spellstatus)
            if player_equip["scroll"]=='FIRE':
                self.burn+=self.spellstatus//10
            elif player_equip["scroll"]=='WATER':
                self.water+=self.spellstatus//15
            elif player_equip["scroll"]=='LIGHTNING':
                self.lightning+=self.spellstatus//25
            elif player_equip["scroll"]=='EARTH':
                self.earth+=1+(self.spellstatus//50)
            self.spelflg=1
        self.spellstatus=0
        print("spell status outside",self.spellstatus)
        if self.spellstatus==0 and  self.txt!='':
            drawtext(self.screen,self.font,self.txt,'white',40,self.temp,(190,300))
            self.temp-=5
            if self.temp<=0:
                self.txt=''
                self.spelflg=0
                changeequip('scroll','NONE')
                self.game.battle.spell=''
                self.game.battle.scroll=''
                self.game.battle.spellno=0
                self.spellmistake=0
                self.spellstatus=-1
                self.game.battle.timer=0
                self.temp=255
                self.game.battle.pastaction='player'
                self.game.battle.turnofaction='monster'
                
    def monster(self):
        if self.game.battle.confusion>0:
            self.game.battle.confusion-=1
        if self.heal>0:
            self.heal-=1
        if self.dearm>0:
            self.run-=1
    def update(self,toa):
        if toa=='player' and self.player==0:
            self.monster()
            self.player=1
        if toa=='monster':
            self.player=0
        self.confusion=self.game.battle.confusion
    
    def ranordead(self):
        pygame.draw.rect(self.screen,(255,255,255),(10,10,780,380),3)
        if self.game.player!='alive' or self.game.monster!='alive':
            pygame.draw.rect(self.screen,'black',(10,10,780,380))
            if self.game.player=='dead':
                drawtext(self.screen,self.font,'DEFEAT','white',100,self.temp,(320,150))
                self.temp-=1
                if self.temp<=10:
                    pygame.quit()
                    sys.exit()
            if self.game.player=='ran':
                drawtext(self.screen,self.font,'YOU RAN AWAY','white',100,self.temp,(230,150))
            if self.game.monster=='ran':
                drawtext(self.screen,self.font,'MONSTER RAN AWAY','white',100,self.temp,(190,150))
            if self.game.monster=='dead':
                drawtext(self.screen,self.font,'VICTORY','white',100,self.temp,(310,150))
            self.temp-=3
            if self.temp<=0:
                self.game.monster=self.game.player='alive'
                self.temp=255
                self.game.battle.error=0
                self.game.input_text=''
                self.game.scene=1
    
    def draw(self):
        #print(self.spellstatus)
        if self.game.battle.turnofaction=='player':
            self.other()
            self.defence()
        if self.confusion>=8:
            if self.game.conf==0:
                drawtext(self.screen,self.font,'*YOUR THOUGHTS ARE SPINNING CLOCKWISE*','white',30,85*(self.confusion-7),(230,40))
            elif self.game.conf==1:
                drawtext(self.screen,self.font,'*YOUR THOUGHTS ARE SPINNING ANTI-CLOCKWISE*','white',30,85*(self.confusion-7),(215,40))
    def main(self,toa):
        self.update(toa)
        self.draw()