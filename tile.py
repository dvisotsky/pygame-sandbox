import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.transform.scale(pygame.image.load('./assets/sprites/tilesets/grass.png').convert_alpha(),(TILESIZE,TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-4,-10)
