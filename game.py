from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, width, height, speed = 0):
        super().__init__()
        self.image = image.load(filename)
        self.image = transform.scale(self.image, (width, height))
        self.rect = Rect(x, y, width, height)
        self.speed = speed
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class RectSprite(sprite.Sprite):
    def __init__(self, color, x, y, width, height, speed = 0):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = Rect(x, y, width, height)
        self.speed = speed
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class Player(RectSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

_WIDTH = 800
_HEIGHT = 640

window = display.set_mode((_WIDTH, _HEIGHT))
clock = time.Clock()

ball = GameSprite("ball.png", 500, 300, 50, 50, 5)
player = Player("red", _WIDTH/2, 300, 30, 120, speed=10)

game_is_running = True
while game_is_running:
    for e in event.get():
        if e.type == QUIT:
            game_is_running = False
    window.fill((210, 222, 255))

    player.update()
    player.draw(window)

    display.update()
    clock.tick(60)