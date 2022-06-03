import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.transform.scale( pygame.image.load("./assets/sprites/characters/player0.png").convert_alpha(), (32,32))
        
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5
        
        self.obstacle_sprites = obstacle_sprites

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
        self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
            else: 
                self.direction.y = 0
    
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
            else:
                self.direction.x = 0
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
               
            self.rect.x += self.direction.x * self.speed
            self.collision('h')
            self.rect.y += self.direction.y * self.speed
            self.collision('v')
        

    def collision(self,direction):
        if direction == 'h':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == 'v':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: 
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
            
    def update(self):
        # update and draw player
        self.move()