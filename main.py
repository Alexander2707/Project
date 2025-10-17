from pygame import*
from button import Button
import time as t
import random

rules = transform.scale(image.load("images/rules.png"), (1000, 700))

init()

txt_font = font.Font(None, 48)
YELLOW = (247, 244, 47)
GREY = (104, 100, 97)

bullets2 = sprite.Group()
coins2 = sprite.Group()
enemies2 = sprite.Group()
bullets = sprite.Group()
enemies = sprite.Group()
coins = sprite.Group()

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
            bullets2.add(bullet)

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
    def __init__(self, x, y, width, height, im, click = False, active = False, price = 0):
        self.w = width
        self.h = height
        self.image = transform.scale(image.load(im), (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = click
        self.active = active
        self.price = price
        
        self.price_txt = txt_font.render(f'price: {self.price}', True, (255, 255, 255))
        self.button = Button(self.rect.x, self.rect.y+200, self.w, 50, "images/red_but.png", 'sounds/click.wav', "Buy")
    def reset1(self):
        
        if self.active:
            draw.rect(screen, GREY, self.rect)
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            image2 = self.image.copy()
            image2.fill((0, 0, 0, 150))
            screen.blit(self.image, (self.rect.x, self.rect.y))
            screen.blit(image2, (self.rect.x, self.rect.y))
            draw.rect(screen, (0,0,0), self.rect, 5)
            screen.blit(self.price_txt, (self.rect.x+10, self.rect.y+10)) 
            self.button.draw(screen)
            
            
    def reset2(self):
        if self.active:
            draw.rect(screen, GREY, self.rect)
            draw.rect(screen, YELLOW, self.rect, 5)
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            image2 = self.image.copy()
            image2.fill((0, 0, 0, 150))
            screen.blit(self.image, (self.rect.x, self.rect.y))
            screen.blit(image2, (self.rect.x, self.rect.y))
            draw.rect(screen, (0,0,0), self.rect, 5)
            screen.blit(self.price_txt, (self.rect.x+10, self.rect.y+10)) 
            self.button.draw(screen)
        
    # def skin_locked(self):
        

def move_skins():
    skin1.rect.y = 10000
    skin2.rect.y = 10000
    skin3.rect.y = 10000
    skin4.rect.y = 10000
    
def restart():
    global scroll, coin_spawn_timer, enemy_spawn_timer, next_coin_spawn, next_spawn, win, lose, start
    start = t.time()
    enemies.empty()
    coins.empty()
    scroll = True
    coin_spawn_timer = 0
    enemy_spawn_timer = 0
    next_coin_spawn = random.randint(3000, 5000)
    next_spawn = random.randint(1000, 1500)
    win = False
    lose = False
    
def restart2():
    global scroll, coin2_spawn_timer, enemy2_spawn_timer, next_coin_spawn2, next_spawn2, win, lose2, start
    start = t.time()
    enemies2.empty()
    coins2.empty()
    scroll = True
    coin2_spawn_timer = 0
    enemy2_spawn_timer = 0
    next_coin_spawn2 = random.randint(3000, 5000)
    next_spawn2 = random.randint(1000, 1500)
    win = False
    lose2 = False        
    
screen = display.set_mode((0,0), FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
lvl1_bg = transform.scale(image.load("images/game_bg.jpg"), (WIDTH, HEIGHT))
lvl2_bg = transform.scale(image.load("images/lvl2.jpg"), (WIDTH, HEIGHT))
menu_bg = transform.scale(image.load("images/menu_bg.png"), (WIDTH, HEIGHT))
start_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2-60), 200, 100, "images/start.png", "sounds/click.wav", "", "images/start2.png")
quit_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2+60), 200, 100, "images/exit.png", "sounds/click.wav", "", "images/exit2.png")
lvl_btn = Button(20, 20, 200, 75, "images/red_but.png", "sounds/click.wav", "LEVELS", "")
help_btn = Button(WIDTH-220, 20, 200, 75, "images/blue_but.png", "sounds/click.wav", "HELP", "")
mus_btn = Button(WIDTH-100, HEIGHT-100, 75, 75, "images/musb.png", "sounds/click.wav", "", "images/musb2.png")
skins_btn = Button(20, HEIGHT-95, 200, 75, "images/blue_but.png", "sounds/click.wav", "SKINS", "")
menu_btn = Button(WIDTH-220, 20, 200, 75, "images/blue_but.png", "sounds/click.wav", "MENU", "")
lvl1_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2-60), 200, 75, "images/blue_but.png", "sounds/click.wav", "LEVEL 1", "")
lvl2_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2+60), 200, 75, "images/red_but.png", "sounds/click.wav", "LEVEL 2", "")

restart_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2), 200, 75, "images/btn1.png", "sounds/click.wav", "RESTART", "")
home_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2+90), 200, 75, "images/btn2.png", "sounds/click.wav", "MENU", "")
exit_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2+180), 200, 75, "images/btn3.png", "sounds/click.wav", "QUIT", "")

restart2_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2), 200, 75, "images/btn1.png", "sounds/click.wav", "RESTART", "")
home2_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2+90), 200, 75, "images/btn2.png", "sounds/click.wav", "MENU", "")
exit2_btn = Button((WIDTH/2-200/2), (HEIGHT/2-100/2+180), 200, 75, "images/btn3.png", "sounds/click.wav", "QUIT", "")

player = Player(50, HEIGHT/2-150, 200, 200, "images/player.png", 5)

skin1 = Skin(50, HEIGHT/2-150, 200, 200, "images/player.png", True, True)
skin2 = Skin(300, HEIGHT/2-150, 200, 200, "images/hero.png", False, False, 5)
skin3 = Skin(550, HEIGHT/2-150, 200, 200, "images/skin2.png", False, False, 10)

skin4 = Skin(800, HEIGHT/2-150, 200, 200, "images/skin3.png", False, False, 15)

mixer.init()
mixer.music.load("sounds/menu.wav")
mixer.music.set_volume(0.4)
mixer.music.play(-1)
hit = mixer.Sound('sounds/damage2.mp3')
coin_sound = mixer.Sound('sounds/coin.wav')

skins = []


########################### LEVEL 1 ###########################

scroll = True
coin_spawn_timer = 0
enemy_spawn_timer = 0
next_coin_spawn = random.randint(3000, 5000)
next_spawn = random.randint(1000, 1500)
win = False
lose = False
bg_speed = 2
# score = 0


########################### LEVEL 2 ###########################

coin2_spawn_timer = 0
enemy2_spawn_timer = 0
next_coin_spawn2 = random.randint(3000, 5000)
next_spawn2 = random.randint(1000, 1500)
lose2 = False
# score2 = 0

balance = 0
txt_font = font.Font(None, 48)
txt_font2 = font.Font(None, 96)
lose_txt = txt_font.render("YOU LOSE!", True, (255, 255, 255))
win_txt = txt_font2.render("YOU WIN!", True, (0, 0, 0))
clock = time.Clock()
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
                restart()
                start = t.time()
            if quit_btn.rect.collidepoint(e.pos):
                quit_btn.check_click(mouse.get_pos(), e)
                run = False
            if lvl_btn.rect.collidepoint(e.pos):
                lvl_btn.check_click(mouse.get_pos(), e)
                a = "levels"
            if help_btn.rect.collidepoint(e.pos):
                help_btn.check_click(mouse.get_pos(), e)
                a = "help"
            if menu_btn.rect.collidepoint(e.pos):
                menu_btn.check_click(mouse.get_pos(), e)
                a = "menu"
            if skins_btn.rect.collidepoint(e.pos):
                skins_btn.check_click(mouse.get_pos(), e)
                a = "skins"
            if lvl1_btn.rect.collidepoint(e.pos):
                lvl1_btn.check_click(mouse.get_pos(), e)
                a = "lvl1"
                start = t.time()
            if lvl2_btn.rect.collidepoint(e.pos):
                lvl2_btn.check_click(mouse.get_pos(), e)
                a = "lvl2"
                start = t.time()
            if restart_btn.rect.collidepoint(e.pos):
                restart_btn.check_click(mouse.get_pos(), e)
                a = "lvl1"
                restart()
            if home_btn.rect.collidepoint(e.pos):
                home_btn.check_click(mouse.get_pos(), e)
                a = "menu"
                restart()
            if exit_btn.rect.collidepoint(e.pos):
                exit_btn.check_click(mouse.get_pos(), e)
                run = False
            if restart2_btn.rect.collidepoint(e.pos):
                restart_btn.check_click(mouse.get_pos(), e)
                a = "lvl2"
                restart2()
            if home2_btn.rect.collidepoint(e.pos):
                home_btn.check_click(mouse.get_pos(), e)
                a = "menu"
                restart2()
            if exit2_btn.rect.collidepoint(e.pos):
                exit_btn.check_click(mouse.get_pos(), e)
                run = False
            if mus_btn.rect.collidepoint(e.pos):
                mus_btn.check_click(mouse.get_pos(), e)
                if music == "on":
                    mixer.music.pause()
                    music = "off"
                else:
                    mixer.music.unpause()
                    music = "on"
            if skin4.button.rect.collidepoint(e.pos) and balance >= skin4.price:
                    skin4.active = True
                    balance -= skin4.price
                    
            if skin3.button.rect.collidepoint(e.pos) and balance >= skin3.price:
                    skin3.active = True
                    balance -= skin3.price
                    
            if skin2.button.rect.collidepoint(e.pos) and balance >= skin2.price:
                    skin2.active = True
                    balance -= skin2.price
            
            if skin1.rect.collidepoint(e.pos):
                skins.clear()
                skins.append(skin1)
                skin1.click = True
                skin2.click = False
                skin3.click = False
                skin4.click = False
                player = Player(50, HEIGHT/2-150, 200, 200, "images/player.png", 5)
            if skin2.rect.collidepoint(e.pos):
                skins.clear()
                skins.append(skin1)
                skin2.click = True
                skin1.click = False
                skin3.click = False
                skin4.click = False
                if skin2.active:
                    player = Player(50, HEIGHT/2-150, 200, 200, "images/hero.png", 5)
            if skin3.rect.collidepoint(e.pos):
                skins.clear()
                skins.append(skin3)
                skin3.click = True
                skin2.click = False
                skin1.click = False
                skin4.click = False
                if skin3.active:
                    player = Player(50, HEIGHT/2-150, 200, 200, "images/skin2.png", 5)
            if skin4.rect.collidepoint(e.pos):
                skins.clear()
                skins.append(skin4)
                skin4.click = True
                skin2.click = False
                skin3.click = False
                skin1.click = False
                if skin4.active:
                    player = Player(50, HEIGHT/2-150, 200, 200, "images/skin3.png", 5)

    if a == "menu":
        a = "menu"
        restart_btn.rect.y = 10000
        home_btn.rect.y = 10000
        exit_btn.rect.y = 10000
        restart2_btn.rect.y = 10000
        home2_btn.rect.y = 10000
        exit2_btn.rect.y = 10000
        lvl1_btn.rect.y = 10000
        lvl2_btn.rect.y = 10000
        menu_btn.rect.y = 10000
        start_btn.rect.y = (HEIGHT/2-100/2-60)
        quit_btn.rect.y = (HEIGHT/2-100/2+60)
        lvl_btn.rect.y = 20
        help_btn.rect.y = 20
        skins_btn.rect.y = HEIGHT-95
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
        start_btn.rect.y = (HEIGHT/2-100/2-60)
        quit_btn.rect.y = (HEIGHT/2-100/2+60)
        lvl_btn.rect.y = 20
        help_btn.rect.y = 20
        skins_btn.rect.y = HEIGHT-100
        move_skins()
    elif a == "skins":
        txt_balance = txt_font.render(f'Balance: {balance}', True, (255,255,255))
        start_btn.rect.y = 10000
        quit_btn.rect.y = 10000
        lvl_btn.rect.y = 10000
        help_btn.rect.y = 10000
        skins_btn.rect.y = 10000
        restart_btn.rect.y = 10000
        home_btn.rect.y = 10000
        exit_btn.rect.y = 10000
        lvl1_btn.rect.y = 10000
        lvl2_btn.rect.y = 10000
        restart2_btn.rect.y = 10000
        home2_btn.rect.y = 10000
        exit2_btn.rect.y = 10000
        skin1.rect.y = HEIGHT/2-150
        skin2.rect.y = HEIGHT/2-150
        skin3.rect.y = HEIGHT/2-150
        skin4.rect.y = HEIGHT/2-150
        menu_btn.rect.x = WIDTH-220
        menu_btn.rect.y = 20
        screen.blit(menu_bg, (0, 0))
        screen.blit(txt_balance, (20, HEIGHT-50))
        menu_btn.draw(screen)
        menu_btn.reset()
        mus_btn.draw(screen)
        mus_btn.reset()
        if skin1.click == False:
            skin1.reset1()
        elif skin1.click == True:      
            skin1.reset2()
        if skin2.click == False:
            skin2.reset1()
        elif skin2.click == True:
            skin2.reset2()
        if skin3.click == False:
            skin3.reset1()
        elif skin3.click == True:
            skin3.reset2()
        if skin4.click == False:
            skin4.reset1()
        elif skin4.click == True:
            skin4.reset2()
    elif a == "levels":
        start_btn.rect.y = 10000
        quit_btn.rect.y = 10000
        lvl_btn.rect.y = 10000
        help_btn.rect.y = 10000
        skins_btn.rect.y = 10000
        restart_btn.rect.y = 10000
        home_btn.rect.y = 10000
        exit_btn.rect.y = 10000
        restart2_btn.rect.y = 10000
        home2_btn.rect.y = 10000
        exit2_btn.rect.y = 10000
        lvl1_btn.rect.y = HEIGHT/2-100/2-60
        lvl2_btn.rect.y = HEIGHT/2-100/2+60
        menu_btn.rect.y = 20
        menu_btn.rect.x = WIDTH-220
        screen.blit(menu_bg, (0, 0))
        mus_btn.draw(screen)
        mus_btn.reset()
        menu_btn.draw(screen)
        lvl1_btn.draw(screen)
        lvl2_btn.draw(screen)
        move_skins()
    elif a == "lvl1":
        start_btn.rect.y = 10000
        quit_btn.rect.y = 10000
        lvl_btn.rect.y = 10000
        help_btn.rect.y = 10000
        skins_btn.rect.y = 10000
        lvl1_btn.rect.y = 10000
        lvl2_btn.rect.y = 10000
        restart2_btn.rect.y = 10000
        home2_btn.rect.y = 10000
        exit2_btn.rect.y = 10000
        move_skins()
        screen.blit(lvl1_bg, (x1, 0))
        screen.blit(lvl1_bg, (x2, 0))
        if not lose:
            txt_score = txt_font.render(f'Balance: {balance}', True, (0,0,0))
            screen.blit(txt_score, (20, HEIGHT-50))
            
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
                screen.blit(win_txt, (WIDTH/2-((96*4)/2), 200))
                if player.rect.x < WIDTH:
                    player.rect.x += player.speed 
                else:
                    a = "pause"
            else:
                player.rect.x = 50
                bg_speed = 2
                win = False
                scroll = True
                
            enemy_spawn_timer += clock.get_time()
            if scroll and enemy_spawn_timer >= next_spawn:
                enemy_spawn_timer = 0
                next_spawn = random.randint(1000, 1500)
                enemy = Enemy(WIDTH+10, random.randint(0, HEIGHT-200), 150, 150, "images/enemy.png")
                enemies.add(enemy)

            coin_spawn_timer += clock.get_time()
            if scroll and coin_spawn_timer >= next_coin_spawn:
                coin_spawn_timer = 0
                next_coin_spawn = random.randint(3000, 5000)
                coin = Enemy(WIDTH+10, random.randint(0, HEIGHT-200), 100, 100, "images/snitch.png", 3)
                coins.add(coin)
            
            player.reset()
            player.update()
            bullets.draw(screen)
            bullets.update()
            enemies.draw(screen)
            enemies.update()
            coins.draw(screen)
            coins.update()
            
            if sprite.groupcollide(bullets, enemies, True, True):
                hit.play()
            
            if sprite.spritecollide(player, coins, True):
                balance += 1
                coin_sound.play()

            if sprite.spritecollide(player, enemies, False):
                lose = True
                
        elif lose == True:
            restart_btn.rect.y = (HEIGHT/2-100/2)
            exit_btn.rect.y = (HEIGHT/2-100/2+180)
            home_btn.rect.y = (HEIGHT/2-100/2+90)
            draw.rect(screen, (47, 112, 175), (WIDTH/2 - 150, HEIGHT/2 - 250, 300, 500), 0, 20)
            restart_btn.draw(screen)
            home_btn.draw(screen)
            exit_btn.draw(screen)
            screen.blit(lose_txt, (WIDTH/2-85, HEIGHT/2 - 180))
    elif a == "lvl2":
        start_btn.rect.y = 10000
        quit_btn.rect.y = 10000
        lvl_btn.rect.y = 10000
        help_btn.rect.y = 10000
        skins_btn.rect.y = 10000
        lvl1_btn.rect.y = 10000
        lvl2_btn.rect.y = 10000
        restart_btn.rect.y = 10000
        home_btn.rect.y = 10000
        exit_btn.rect.y = 10000
        move_skins()
        screen.blit(lvl2_bg, (x1, 0))
        screen.blit(lvl2_bg, (x2, 0))
        win = False
        scroll = True
        coins.empty()
        enemies.empty()
        bullets.empty()
        if not lose2:
            txt_score2 = txt_font.render(f'Balance: {balance}', True, (0,0,0))
            screen.blit(txt_score2, (20, HEIGHT-50))
            
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
                screen.blit(win_txt, (WIDTH/2-((96*4)/2), 200))
                enemies2.empty()
                
                
                if player.rect.x < WIDTH:
                    player.rect.x += player.speed 
                else:
                    a = "menu"
            else:
                player.rect.x = 50    
                bg_speed = 2
                scroll = True
            
            enemy2_spawn_timer += clock.get_time()
            if scroll and enemy2_spawn_timer >= next_spawn2:
                enemy2_spawn_timer = 0
                next_spawn2 = random.randint(1000, 1500)
                enemy2 = Enemy(WIDTH+10, random.randint(0, HEIGHT-200), 150, 150, "images/enemy2.png")
                enemies2.add(enemy2)

            coin2_spawn_timer += clock.get_time()
            if scroll and coin2_spawn_timer >= next_coin_spawn2:
                coin2_spawn_timer = 0
                next_coin_spawn2 = random.randint(3000, 5000)
                coin2 = Enemy(WIDTH+10, random.randint(0, HEIGHT-200), 100, 100, "images/rock.png", 3)
                coins2.add(coin2)
            
            player.reset()
            player.update()
            bullets2.draw(screen)
            bullets2.update()
            enemies2.draw(screen)
            enemies2.update()
            coins2.draw(screen)
            coins2.update()
            
            if sprite.groupcollide(bullets2, enemies2, True, True):
                hit.play()
            
            if sprite.spritecollide(player, coins2, True):
                balance += 1
                coin_sound.play()

            if sprite.spritecollide(player, enemies2, False):
                lose2 = True
                
        elif lose2 == True:
            restart2_btn.rect.y = (HEIGHT/2-100/2)
            exit2_btn.rect.y = (HEIGHT/2-100/2+180)
            home2_btn.rect.y = (HEIGHT/2-100/2+90)
            draw.rect(screen, (47, 112, 175), (WIDTH/2 - 150, HEIGHT/2 - 250, 300, 500), 0, 20)
            restart2_btn.draw(screen)
            home2_btn.draw(screen)
            exit2_btn.draw(screen)
            screen.blit(lose_txt, (WIDTH/2-85, HEIGHT/2 - 180))
    
    elif a == "pause":
        screen.blit(menu_bg, (0, 0))
        mus_btn.draw(screen)
        menu_btn.draw(screen)
        lvl2_btn.draw(screen)
        skins_btn.draw(screen)
        menu_btn.rect.y = HEIGHT/2-100/2-45
        menu_btn.rect.x = WIDTH/2-200/2
        lvl2_btn.rect.y = HEIGHT/2-100/2+45
        skins_btn.rect.y = HEIGHT-100
        
    elif a == "help":
        screen.blit(menu_bg, (0,0))
        screen.blit(rules, (200, 25))
        menu_btn.rect.x = WIDTH-220
        menu_btn.rect.y = 20
        menu_btn.draw(screen)
        
            
    clock.tick(90)
    display.update()