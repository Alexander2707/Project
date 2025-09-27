from pygame import*
from button import Button

init()

screen = display.set_mode((0,0), FULLSCREEN)
w,h = screen.get_size()
lvl1_bg = transform.scale(image.load("images/game_bg.jpg"), (w,h))
menu_bg = transform.scale(image.load("images/menu_bg.png"), (w,h))
start_btn = Button((w/2-200/2), (h/2-100/2-60), 200, 100, "images/start.png", "sounds/click.wav", "", "images/start2.png")
quit_btn = Button((w/2-200/2), (h/2-100/2+60), 200, 100, "images/exit.png", "sounds/click.wav", "", "images/exit2.png")
lvl_btn = Button(20, 20, 200, 75, "images/red_but.png", "sounds/click.wav", "LEVELS", "")
help_btn = Button(w-220, 20, 200, 75, "images/blue_but.png", "sounds/click.wav", "HELP", "")
mus_btn = Button(w-100, h-100, 75, 75, "images/musb.png", "sounds/click.wav", "", "images/musb2.png")

mixer.init()
mixer.music.load("sounds/menu.wav")
mixer.music.set_volume(0.4)
mixer.music.play(-1)

music = "on"
a = "menu"
run = True
while run:
    if a == "menu":
        screen.blit(menu_bg, (0, 0))
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    run = False
                    quit()
            elif e.type == MOUSEBUTTONDOWN:
                if start_btn.rect.collidepoint(e.pos):
                    start_btn.check_click(mouse.get_pos(), e)
                    a = "lvl1"
                if quit_btn.rect.collidepoint(e.pos):
                    quit_btn.check_click(mouse.get_pos(), e)
                    run = False
                if lvl_btn.rect.collidepoint(e.pos):
                    lvl_btn.check_click(mouse.get_pos(), e)
                if help_btn.rect.collidepoint(e.pos):
                    help_btn.check_click(mouse.get_pos(), e)
                if mus_btn.rect.collidepoint(e.pos):
                    mus_btn.check_click(mouse.get_pos(), e)
                    if music == "on":
                        mixer.music.pause()
                        music = "off"
                    else:
                        mixer.music.unpause()
                        music = "on"
        
        start_btn.draw(screen)
        quit_btn.draw(screen)
        lvl_btn.draw(screen)
        help_btn.draw(screen)
        mus_btn.draw(screen)
        quit_btn.reset()
        start_btn.reset()
        lvl_btn.reset()
        help_btn.reset()
        mus_btn.reset()
    elif a == "lvl1":
        screen.blit(lvl1_bg, (0, 0))
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    run = False
                    quit()
    display.update()