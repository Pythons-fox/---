from pygame import * 
mixer.init() 
from random import randint
font.init()
from time import time as timer

window = display.set_mode((500, 600))
window.fill((255,200,100))

class game_sprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class player(game_sprite):
    def update(self):
            keys = key.get_pressed()
            if keys[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed
            if keys[K_RIGHT] and self.rect.x < 630: 
                self.rect.x += self.speed

cloick = time.Clock()
game = True

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    display.update()
    cloick.tick(60) 


    




