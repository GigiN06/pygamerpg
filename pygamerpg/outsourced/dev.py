#https://dev.to/chrisgreening/simulating-simple-crt-and-glitch-effects-in-pygame-1mf1
import pygame,random
pygame.init()
class Effects:
    def __init__(self,game,screen):
        self.game=game
        self.screen=screen
        self.width,self.height=self.screen.get_size()
    def scanlines(self):
        self.width,self.height=self.screen.get_size()
        scanline=pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        for y in range(0,self.height,4):
            pygame.draw.line(scanline,(0,0,0,120),(0,y),(self.width,y))
        self.screen.blit(scanline,(0,0))
        
    def pixelation(self,pixelation):
        pixelation = {"minimum": 2, "medium": 4, "maximum": 6}.get(pixelation, 2)
        self.width, self.height = self.screen.get_size()
        small_surf = pygame.transform.scale(self.screen, (self.width // pixelation, self.height // pixelation))
        self.screen.blit(pygame.transform.scale(small_surf, (self.width, self.height)), (0, 0))
        
    def flicker(self):
        if random.randint(0, 20) == 0:
            flicker_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
            flicker_surface.fill((255, 255, 255, 5))
            self.screen.blit(flicker_surface, (0, 0))
    def glow(self):
        self.width, self.height = self.screen.get_size()
        glow_surf = pygame.transform.smoothscale(self.screen, (self.width // 2, self.height // 2))
        glow_surf = pygame.transform.smoothscale(glow_surf, (self.width, self.height))
        glow_surf.set_alpha(100)
        self.screen.blit(glow_surf, (0, 0))
        
    def glitch(self,  intensity):
        shift_amount = {"minimum": 10, "medium": 20, "maximum": 40}.get(intensity, 20)
        glitch_surface=self.screen.copy()
        if random.random() < 0.1:
            y_start = random.randint(0, self.height - 20)
            slice_height = random.randint(5, 20)
            offset = random.randint(-shift_amount, shift_amount)

            slice_area = pygame.Rect(0, y_start, self.width, slice_height)
            slice_copy = glitch_surface.subsurface(slice_area).copy()
            glitch_surface.blit(slice_copy, (offset, y_start))
    def static( self, intensity):
        static_chance = {"minimum": 0.1, "medium": 0.3, "maximum": 0.8}.get(intensity, 0.2)
        static_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        for y in range(0, self.height, 8):
            if random.random() < static_chance:
                pygame.draw.line(static_surface, (255, 255, 255, random.randint(30, 80)), (0, y), (self.width, y))

        self.screen.blit(static_surface, (0, 0), special_flags=pygame.BLEND_ADD)
    def main(self):
        self.scanlines()
        self.pixelation("minimum")
        self.flicker()
        self.glow()
        self.glitch("maximum")
        #self.static("minimum")
