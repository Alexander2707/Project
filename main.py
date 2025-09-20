from pygame import*

init()

menu = display.set_mode((0,0), FULLSCREEN)
w,h = menu.get_size()
menu_bg = transform.scale(image.load("images/menu_bg.png"), (w,h))

run = True
while True:
    menu.blit(menu_bg, (0, 0))
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
                quit()

    display.update()