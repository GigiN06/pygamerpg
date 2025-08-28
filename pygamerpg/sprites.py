from config import *

class Sprites(pygame.sprite.Sprite):
    def __init__(self,game,screen,):            
        pygame.sprite.Sprite.__init__(self)
        self.game=game
        self.screen=screen
        
class Spriteload:
    def __init__(self,game,screen):
        super().__init__()
        self.start = pygame.image.load("sprites/tv.png").convert_alpha()
        self.game=game
        self.screen=screen
        self.scene=0
    def update(self):
        self.scene=self.game.scene
    def draw(self):
        if self.scene<=1:
            self.screen.blit(self.start,(0,0),)
    def main(self):
        self.update()
        self.draw()