import arcade
import random

WIDTH = 800
HEIGHT = 800
TITLE = "The Bouncing Ball"

class Ball():
    def __init__(self, x, y, vel_x, vel_y, size, color):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.size = size
        self.color = color

    def update(self):
        if self.x > WIDTH - self.size:
            self.vel_x = - abs(self.vel_x)
        if self.y > HEIGHT - self.size:
            self.vel_y = - abs(self.vel_y)
        if self.x < self.size:
            self.vel_x = abs(self.vel_x)
        if self.y < self.size:
            self.vel_y = abs(self.vel_y)
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

class Game(arcade.Window):
    def __init__(self, WIDTH, HEIGHT, TITLE):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.shapes = []
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)
        for i in range(50):
            b = Ball(
                random.randint(0, WIDTH), 
                random.randint(0, HEIGHT), 
                random.randint(-10, 10), 
                random.randint(-10, 10),
                random.randint(10, 100),
                (random.randint(0,255),random.randint(0,255), random.randint(0,255))
                )
            self.shapes.append(b)
        self.player = Ball(100, 100, 0, 0, 50, (0, 255, 100))

    def update(self, delta_time):
        for b in self.shapes:
            b.update()
        self.player.update()

    def on_draw(self):
        arcade.start_render()
        for shape in self.shapes:
            shape.draw()
        self.player.draw()
        arcade.finish_render()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.player.vel_x = 10
        if key == arcade.key.LEFT:
            self.player.vel_x = -10
        if key == arcade.key.UP:
            self.player.vel_y = 10
        if key == arcade.key.DOWN:
            self.player.vel_y = -10
        if key == arcade.key.ENTER:
            b = Ball(
                random.randint(0, WIDTH), 
                random.randint(0, HEIGHT), 
                random.randint(-10, 10), 
                random.randint(-10, 10),
                random.randint(10, 100),
                (random.randint(0,255),random.randint(0,255), random.randint(0,255))
                )
            self.shapes.append(b)
        if key == arcade.key.PLUS:
            self.player.size += 5


    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.player.vel_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.vel_y = 0
        



window = Game(WIDTH, HEIGHT, TITLE)

arcade.run()