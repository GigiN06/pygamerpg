from config import *
from start_page import *
from sprites import *
from battle import *
from actions import *
#from outsourced.dev import *
from kingdom import *
from places import *

def shift_letter(char, shift):
    if char.isalpha():
        base = ord('A') if char.isupper() else ord('a')
        return chr((ord(char) - base + shift) % 26 + base)
    return char

class Game:
    def __init__(self):
        self.run=True
        self.screen=pygame.display.set_mode((win_width,win_height))
        self.clock=pygame.time.Clock()
        self.scene=1
        self.input_text=''
        self.attack=0 #change
        self.typeerror=1
        self.info=0
        self.conf=0
        self.player='alive'
        self.monster='alive'
    def objects(self):
        self.start=StartPage(game,game.screen)
        self.kingdom=Kingdom(game,game.screen)
        self.battle=Battle(game,game.screen)
        self.sprite=Spriteload(game,game.screen)
        self.action=Actions(game,game.screen)
        self.place=Places(game,self.screen)
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_RETURN :
                    if self.scene==0:
                        if self.input_text.lower()=='start':
                            self.scene=1
                            self.input_text=''
                        elif self.input_text.lower()=='quit':
                            self.run = False
                    elif self.scene==1:
                        if self.input_text.lower()=='gui':
                            self.input_text=''
                            #flag=index=alph=tempy=lock=-1
                            self.scene=3
                    elif self.scene==3:
                        pass
                elif event.key== pygame.K_BACKSPACE:
                    self.input_text=self.input_text[:-1]
                elif event.key== pygame.K_ESCAPE:
                    if self.scene==1:
                        print(self.place.typed)
                        self.input_text=''
                        self.place.typed=0
                    if self.scene==3:
                        self.input_text=''
                        self.attack=0
                elif event.key==pygame.K_SPACE:
                    self.input_text+=' '
                elif event.key==pygame.K_TAB:
                    self.info=1
                elif event.unicode.isalpha():
                    print(self.input_text)
                    if self.battle.confusion<8:
                        self.input_text+=event.unicode
                    else:
                        if self.conf==0:
                            print("right")
                            self.input_text+= shift_letter(event.unicode,(self.battle.confusion-7))
                        elif self.conf==1:
                            print("left")
                            self.input_text+= shift_letter(event.unicode,-(self.battle.confusion-7))
            elif event.type== pygame.KEYUP:
                if event.key==pygame.K_TAB:
                    self.info=0
    def update(self):
        self.events()
    
    def draw(self):
        self.screen.fill('black')
        self.clock.tick(FPS)
        if self.scene==0:
            self.start.main(self.input_text)
        if self.scene==1:
            self.kingdom.main(self.input_text)
        if self.scene==3:
            self.battle.main(self.input_text)
        self.action.main(self.battle.turnofaction)
        pygame.display.flip()
    def main(self):
        self.update()
        self.draw()
# mine                    
game=Game()
game.objects()
#outsource
#effects=Effects(game,game.screen)

while game.run:
    game.main()
pygame.quit()
sys.exit()