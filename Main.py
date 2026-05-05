from pygame import * 
mixer.init() 
from random import randint
font.init()
from time import time as timer

window = display.set_mode((400, 400))

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
    def update_r(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 350: 
                self.rect.y += self.speed
    def update_l(self):
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < 350: 
                self.rect.y += self.speed

rocet640_r = player('rocet1.png', 20, 30, 4, 30, 50 ) 
rocet640_l = player('rocet2.png', 350, 30, 4, 30, 50 )  
boll640 = game_sprite('Boll.png', 200, 200, 3, 40, 40)

cloick = time.Clock()
game = True

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False 

    rocet640_r.update_r()
    rocet640_l.update_l()

    window.fill((255,200,100))
    rocet640_r.reset()
    rocet640_l.reset()
    boll640.reset()
    display.update()
    cloick.tick(60) 


    




