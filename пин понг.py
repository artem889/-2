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

# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, player_speed,size_x, size_y):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image),(size_x, size_y))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))


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
# finish = False

# asteroids = sprite.Group()

# for i in range(1, 3):
#     asteroid = Enemy('asteroid.png', randint(80, 620), -40, randint(1, 3), 80, 50)
#     asteroids.add(asteroid)


# monsters = sprite.Group()

# for i in range(1, 3):
#     monster = Enemy('ufo.png',randint(80, 620), -40, randint(1, 3), 80, 50)
#     monsters.add(monster)
   
# font.init()
# font1 = font.SysFont('Arial', 36)
# win = font1.render('YOU WIN!', True, (255, 255, 255))
# lose = font1.render('YOU LOSE!', True, (180, 0, 0))
# bullets = sprite.Group()

# rel_time = False

# num_fire = 0          

while game:
    
#     for e in event.get():
#         if e.type == QUIT:
#             game = False
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 if num_fire < 5 and rel_time == False:
#                     num_fire = num_fire +1
#                     fire.play()
#                     ship.fire()
#                 if num_fire >=5 and rel_time == False:
#                     last_time = timer()
#                     rel_time = True
                
#     if finish != True:
#         window.blit(background,(0,0))
#         ship.reset()
#         ship.update()

#         text = font1.render('Счет:' + str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))

#         text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))

#         asteroids.draw(window)
#         asteroids.update()

#         monsters.draw(window)
#         monsters.update()

#         bullets.draw(window)
#         bullets.update()

#         ship.reset()
#         monsters.draw(window)
#         bullets.draw(window)

#         if rel_time == True:
#             now_time = timer()

#             if now_time - last_time < 3:
#                 reload = font1.render('Wait, reload...', 1, (150, 0, 0))
#                 window.blit(reload, (260, 460))
#             else:
#                 num_fire = 0
#                 rel_time = False


#         sprites_list = sprite.groupcollide(monsters, bullets, True, True)
    

#         for c in sprites_list:
#             score = score + 1
#             monster = Enemy('ufo.png', randint(80, 620), -40, randint(1, 3), 80, 50)
#             monsters.add(monster)

#         if sprite.spritecollide(ship, monsters, False) or lost >= 5:
#             finish = True
#             window.blit(lose, (200, 200))

#         if sprite.spritecollide(ship, asteroids, False) or lost >= 5:
#             finish = True
#             window.blit(lose, (200, 200))

#         if score >= 10 :
#             finish = True
#             window.blit(win, (200, 200))
#     else:
#         finish = False
#         score = 0
#         lost = 0
#         rel_time = False
#         num_fire = 0 
#         for b in bullets:
#             b.kill()
#         for m in monsters:
#             m.kill()
#         for a in asteroids:
#             a.kill()

#         time.delay (3000)
#         for i in range(1, 6):
#             monster = Enemy('ufo.png', randint(80, 620), -40, randint(1, 3), 80, 50)
#             monsters.add(monster)
#         for i in range(1, 3):
#             asteroid = Enemy('asteroid.png', randint(80, 620), -40, randint(1, 3), 80, 50)
#             asteroids.add(asteroid)

      
    clock.tick(FPS)
    display.update()