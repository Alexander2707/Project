from pygame import*
from button import Button
import time as t
import random

init()

YELLOW = (247, 244, 47)
GREY = (104, 100, 97)

bullets = sprite.Group()
enemies = sprite.Group()

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, width, height, im, speed = 3):
        super().__init__()
        self.w = width
        self.h = height
        self.image = transform.scale(image.load(im), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def reset2(self):
        draw.rect(screen, GREY, self.rect)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        click = False
            
    def reset3(self):
        draw.rect(screen, GREY, self.rect)
        draw.rect(screen, YELLOW, self.rect, 5)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update(self):
        if win == False:
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.top > 0:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += self.speed
    
    def fire(self):
        if win == False:
            bullet = Bullet(self.rect.right, self.rect.centery, 50, 50, "images/bullet.webp", 10)
            bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.kill()

class Enemy(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.kill()

class Skin():       
    def __init__(self, x, y, width, height, im, click = False):
        self.w = width
        self.h = height
        self.image = transform.scale(image.load(im), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = click
        
    def reset1(self):
        draw.rect(screen, GREY, self.rect)
        screen.blit(self.image, (self.rect.x, self.rect.y))
            
    def reset2(self):
        draw.rect(screen, GREY, self.rect)
        draw.rect(screen, YELLOW, self.rect, 5)
        screen.blit(self.image, (self.rect.x, self.rect.y))

            
    
screen = display.set_mode((0,0), FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
lvl1_bg = transform.scale(image.load("images/game_bg.jpg"), (WIDTH, HEIGHT))
menu_bg = transform.scale(image.load("images/menu_bg.png"), (WIDTH, HEIGHT))
start_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2-60), 200, 100, "images/start.png", "sounds/click.wav", "", "images/start2.png")
quit_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2+60), 200, 100, "images/exit.png", "sounds/click.wav", "", "images/exit2.png")
lvl_btn = Button(20, 20, 200, 75, "images/red_but.png", "sounds/click.wav", "LEVELS", "")
help_btn = Button(WIDTH-220, 20, 200, 75, "images/blue_but.png", "sounds/click.wav", "HELP", "")
mus_btn = Button(WIDTH-100, HEIGHT-100, 75, 75, "images/musb.png", "sounds/click.wav", "", "images/musb2.png")
skins_btn = Button(20, HEIGHT-95, 200, 75, "images/blue_but.png", "sounds/click.wav", "SKINS", "")

player = Player(50, HEIGHT/2-150, 200, 200, "images/hero.png", 5)

skin1 = Skin(50, HEIGHT/2-150, 200, 200, "images/player.png")
skin2 = Skin(300, HEIGHT/2-150, 200, 200, "images/hero.png")
skin3 = Skin(550, HEIGHT/2-150, 200, 200, "images/skin2.png")
skin4 = Skin(800, HEIGHT/2-150, 200, 200, "images/skin3.png")

mixer.init()
mixer.music.load("sounds/menu.wav")
mixer.music.set_volume(0.4)
mixer.music.play(-1)
hit = mixer.Sound('sounds/damage2.mp3')

scroll = True
enemy_spawn_timer = 0
next_spawn = random.randint(1000, 1500)
win = False
move_up = False
move_down = False
clock = time.Clock()
bg_speed = 1.5
x1 = 0
x2 = WIDTH
music = "on"
a = "menu"
run = True
while run:   
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            if e.key == K_SPACE:
                    player.fire()
        elif e.type == MOUSEBUTTONDOWN:
            if start_btn.rect.collidepoint(e.pos):
                start_btn.check_click(mouse.get_pos(), e)
                a = "lvl1"
                start = t.time()
            if quit_btn.rect.collidepoint(e.pos):
                quit_btn.check_click(mouse.get_pos(), e)
                run = False
            if lvl_btn.rect.collidepoint(e.pos):
                lvl_btn.check_click(mouse.get_pos(), e)
            if help_btn.rect.collidepoint(e.pos):
                help_btn.check_click(mouse.get_pos(), e)
            if skins_btn.rect.collidepoint(e.pos):
                skins_btn.check_click(mouse.get_pos(), e)
                a = "skins"
            if mus_btn.rect.collidepoint(e.pos):
                mus_btn.check_click(mouse.get_pos(), e)
                if music == "on":
                    mixer.music.pause()
                    music = "off"
                else:
                    mixer.music.unpause()
                    music = "on"
            if skin1.rect.collidepoint(e.pos):
                skin1.click = True
            if skin2.rect.collidepoint(e.pos):
                skin2.click = True
            if skin3.rect.collidepoint(e.pos):
                skin3.click = True
            if skin4.rect.collidepoint(e.pos):
                skin4.click = True

    if a == "menu":
        screen.blit(menu_bg, (0, 0))
        start_btn.draw(screen)
        quit_btn.draw(screen)
        lvl_btn.draw(screen)
        help_btn.draw(screen)
        mus_btn.draw(screen)
        skins_btn.draw(screen)
        quit_btn.reset()
        start_btn.reset()
        lvl_btn.reset()
        help_btn.reset()
        mus_btn.reset()
    elif a == "skins":
        screen.blit(menu_bg, (0, 0))
        if skin1.click == False:
            skin1.reset1()
        elif skin1.click == True:
            skin1.reset2()
            skin2.click = False
            skin3.click = False
            skin4.click = False
        if skin2.click == False:
            skin2.reset1()
        elif skin2.click == True:
            skin2.reset2()
            skin1.click = False
            skin3.click = False
            skin4.click = False
        if skin3.click == False:
            skin3.reset1()
        elif skin3.click == True:
            skin3.reset2()
            skin1.click = False
            skin2.click = False
            skin4.click = False
        if skin4.click == False:
            skin4.reset1()
        elif skin4.click == True:
            skin4.reset2()
            skin1.click = False
            skin2.click = False
            skin3.click = False
    elif a == "lvl1":
        
        screen.blit(lvl1_bg, (x1, 0))
        screen.blit(lvl1_bg, (x2, 0))
        
        x1 -= bg_speed
        x2 -= bg_speed

        if x1 <= -WIDTH:
            x1 = WIDTH

        if x2 <= -WIDTH:
            x2 = WIDTH
        
        end = t.time()
        timer = int(end-start)

        if timer >= 20:
            bg_speed = 0
            win = True
            scroll = False
            
            enemies.empty()
            
            if player.rect.x < WIDTH:
                player.rect.x += player.speed 
            else:
                run = False
            
        enemy_spawn_timer += clock.get_time()
        if scroll and enemy_spawn_timer >= next_spawn:
            enemy_spawn_timer = 0
            next_spawn = random.randint(1000, 1500)
            enemy = Enemy(WIDTH+10, random.randint(0, HEIGHT-200), 150, 150, "images/enemy.png")
            enemies.add(enemy)
        
        player.reset()
        player.update()
        bullets.draw(screen)
        bullets.update()
        enemies.draw(screen)
        enemies.update()
        
        if sprite.groupcollide(bullets, enemies, True, True):
            hit.play()
            
    clock.tick(90)
    display.update()