#Importing Needed Stuff
from pygame import *

#framerate
clock = time.Clock()
FPS = 60

#Variables
running = True
paddle_width = 20
paddle_height = 80

#Game Window Set Up
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))

#Classes
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - paddle_height:
            self.rect.y += self.speed

#Creating All Sprites
player = Player("Paddle.png", 0, 0, paddle_width, paddle_height, 5)

#Game Loop
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    window.fill((37, 150, 190))

    player.update()
    player.reset()
    display.update()
    clock.tick(FPS)
