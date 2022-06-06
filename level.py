import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):

        # get display surface
        self.displaySurface = pygame.display.get_surface()

        # sprite group setup
        self.visibleSprites = YSortCameraGroup()
        self.obstacleSprites = pygame.sprite.Group()
        self.createMap()

    def createMap(self):
        for rowIndex,row in enumerate(WORLD_MAP):
            for colIndex,col in enumerate(row):
                x = colIndex * TILESIZE
                y = rowIndex * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visibleSprites, self.obstacleSprites])
                elif col == 'p':
                    self.player = Player((x,y),[self.visibleSprites], self.obstacleSprites)

    def run(self):
        # todo: update level
        clock = pygame.time.Clock()
        clock.tick(30)
        self.visibleSprites.custom_draw(self.player)
        self.visibleSprites.update()
        self.player.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_height
        self.offset.y = player.rect.centery - self.half_height

        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
