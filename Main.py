from pygame import * 
mixer.init() 
from random import randint
font.init()
from time import time as timer

finish = False

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
boll640 = game_sprite('Boll.png', 200, 90, 1, 40, 40)

cloick = time.Clock()
game = True

speed_x = 2
speed_y = 2

font1 = font.Font(None, 35)
Lose1 = font1.render('PLAYER 1 LOSE!', True, (255, 0, 0)) 
Lose2 = font1.render('PLAYER 2 LOSE!', True, (255, 0, 0)) 

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    window.fill((255,200,100))
    
    if finish != True:
        boll640.rect.x += speed_x
        boll640.rect.y += speed_y
        if boll640.rect.y > 400 - 50 or boll640.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(rocet640_l, boll640) or sprite.collide_rect(rocet640_r, boll640):
            speed_x *= -1
            boll640.rect.x += speed_x
            boll640.rect.y += speed_y
        rocet640_r.update_r()
        rocet640_l.update_l()
        if boll640.rect.x < -50:
            finish = True
            window.blit(Lose1, (100,100))
        if boll640.rect.x > 400:
            finish = True
            window.blit(Lose2, (160,160))

        
        rocet640_r.reset()
        rocet640_l.reset()
        boll640.reset()
        display.update()
        cloick.tick(60) 

    




