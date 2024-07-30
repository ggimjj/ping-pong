from pygame import *

WIN_W = 700
WIN_H = 500
PLATFORM_SPEED = 3
BALL_SPEED = 3
GRAY = (34, 34, 34)

class Ball(GameSprite):
    def __init__(self, img, x, y, speed, size = (65, 65)):
        super().__init__(img, x, y, speed, size)
        self.speed_x = speed
        self.speed_y = speed

    def update(self, stop_value=50):
        if self.rect.y < 0 or self.rect_y > WIN_H - BALL_SIZE:
            self.speed_y *= -1

        if self.rect.X > WIN_W - stop_value or self.rect_x < 0:
            self.speed_x *= -1  

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

class Player(GameSprite):
    def __init__(self, img, x, y, speed, size = (65, 65)):
        super().__init__(img, x, y, speed, size)

    def update(self, up, down, stop_value=50):
        keys = key.get_pressed()
        if keys[up] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[down] and self.rect.y < WIN_H - stop_value:
            self.rect.y += self.speed
