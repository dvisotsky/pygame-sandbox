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
        self.visibleSprites = pygame.sprite.Group()
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
        self.visibleSprites.draw(self.displaySurface)
        self.visibleSprites.update()
        self.player.update()
        debug(self.player.direction)
