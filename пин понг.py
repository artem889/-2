from pygame import *
# from random import randint
# from time import time as timer
window = display.set_mode((700, 500))
# display.set_caption('пин понг')
# background = transform.scale(image.load("galaxy.jpg"),(700, 500))
window.fill((50, 12, 45))
clock = time.Clock()
FPS = 60


# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# fire = mixer.Sound('fire.ogg')
# # fire.play()

# score = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y > 500:
#            self.rect.y = 0
#            self.rect.x = randint (50, 650)
        
        

# lost = 0
# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > 500:
#             self.rect.x = randint(80, 620)
#             self.rect.y = 0
#             lost = lost + 1
         
    


# class Player(GameSprite):
#     def update(self):
#         keys = key.get_pressed()
#         if keys[K_LEFT] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys[K_RIGHT] and self.rect.x < 620:
#             self.rect.x += self.speed


#     def fire(self):
#         bullet1 = Bullet(('bullet.png'), self.rect.centerx, self.rect.top, -15, 20, 15)
#         bullets.add(bullet1)
 

# class Bullet(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y < 0:
#             self.kill()


# ship = Player('rocket.png', 5, 400, 10, 80, 100)



game = True
finish = False

ball = GameSprite('14.jpg' , 250, 40, 3, 50, 50)



# font.init()
# font1 = font.SysFont('Arial', 36)
# win = font1.render('YOU WIN!', True, (255, 255, 255))
# lose = font1.render('YOU LOSE!', True, (180, 0, 0))
# bullets = sprite.Group()

# rel_time = False

# num_fire = 0          
speed_x = 3
speed_y = 3
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    
            
    if finish != True:
        window.fill((50, 12, 45))

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        # if ball.colliderect(platform.rect):
        #     speed_y *= -1
        # if ball.rect.y < 0:
        #     speed_y *= -1
        # if ball.rect.x > 450 or ball.rect.x < 0:
        #     speed_x *= -1    
        
        ball.reset()
        # ship.update()

#         text = font1.render('Счет:' + str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))

#         text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))


#         ship.reset()
#         monsters.draw(window)
#         bullets.draw(window)

# 

#         sprites_list = sprite.groupcollide(monsters, bullets, True, True)

#         if sprite.spritecollide(ship, monsters, False) or lost >= 5:
#             finish = True
#             window.blit(lose, (200, 200))

#         if sprite.spritecollide(ship, asteroids, False) or lost >= 5:
#             finish = True
#             window.blit(lose, (200, 200))

#         if score >= 10 :
#             finish = True
#             window.blit(win, (200, 200))

      
    clock.tick(FPS)
    display.update()