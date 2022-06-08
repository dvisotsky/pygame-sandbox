import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
class Level:
    def __init__(self):

        # get display surface
        self.displaySurface = pygame.display.get_surface()

        # sprite group setup
        self.visibleSprites = YSortCameraGroup()
        self.obstacleSprites = pygame.sprite.Group()
        self.createMap()

    def createMap(self):
        layouts = {
            'boundary': import_csv_layout('./levels/01_walls.csv'),
            'grass': import_csv_layout('./levels/01_grass.csv'),
            'object': import_csv_layout('./levels/01_object.csv'),

        }
        for style,layout in layouts.items():
            for rowIndex,row in enumerate(layout):
                for colIndex,col in enumerate(row):
                    if col  != '-1':
                        x = colIndex * TILESIZE
                        y = rowIndex * TILESIZE 
                    if style == 'boundary':
                        Tile((x,y),[self.obstacleSprites],'invisible',)
                    if style == 'grass':
                        Tile((x,y),[self.visibleSprites],'grass')

        #         if col == 'x':
        #             Tile((x,y),[self.visibleSprites, self.obstacleSprites])
        #         elif col == 'p':
        #             self.player = Player((x,y),[self.visibleSprites], self.obstacleSprites)
    
        self.player = Player((700,700),[self.visibleSprites], self.obstacleSprites)

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

        #create floor
        self.floor_surf = pygame.transform.scale(pygame.image.load('./assets/map01.png').convert(), (TILESIZE*20, TILESIZE*20))
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        # get offset
        self.offset.x = player.rect.centerx - self.half_height
        self.offset.y = player.rect.centery - self.half_height
        # draw floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)


        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
