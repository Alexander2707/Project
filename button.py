from pygame import*
class Button:
    def __init__(self, x, y, width, height, im, sound, text, im_pressed=None):
        self.sound = mixer.Sound(sound)
        self.width = width
        self.height = height
        self.text = text
        self.image_norm = transform.scale(image.load(im), (self.width, self.height))
        if im_pressed:
            self.image_pressed = transform.scale(image.load(im_pressed), (self.width, self.height))
        else:
            self.image_pressed = self.image_norm
        self.image = self.image_norm
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_clicked = False
        
    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))
        font1 = font.Font(None, 40)
        text_surface = font1.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center = self.rect.center)
        scr.blit(text_surface, text_rect)
        
    def check_click(self, mouse_pos, event):
        self.is_clicked = self.rect.collidepoint(mouse_pos)
        if self.is_clicked and event.type == MOUSEBUTTONDOWN:
            self.sound.play()
            self.image = self.image_pressed
            return True
    
    def reset(self):
        self.image = self.image_norm