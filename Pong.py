#Importing Needed Stuff
from pygame import *

#framerate
clock = time.Clock()
FPS = 60

#Variables
running = True

#Game Window Set Up
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((37, 150, 190))

#Classes
# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
#         super().__init__()
#         self.image = transform.scale(image.load(player_image), (size_x, size_y))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# class Player(GameSprite):
#     def update(self):
#         keys = key.get_pressed()
#         if keys[W] and self.rect.x > 0:
#             self.rect.x -= self.speed
#         if keys[S] and self.rect.x < win_width - 80:
#             self.rect.x += self.speed

#Game Loop
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False


    window.blit(background,(0, 0))

    display.update()
    clock.tick(FPS)