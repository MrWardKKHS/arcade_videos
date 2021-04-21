import arcade
from math import atan2, degrees, sin, cos

WIDTH = 800
HEIGHT = 800
TITLE = "Sprites"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def setup(self):
        self.score = 0
        self.player = arcade.Sprite("character_idle.png", 0.7)
        self.player.center_x = 200
        self.player.center_y = 100
        self.coin = arcade.Sprite('coin.png', 0.4)
    
    def update(self, delta_time):
        diff_x = self.coin.center_x - self.player.center_x
        diff_y = self.coin.center_y - self.player.center_y
        angle = atan2(diff_y, diff_x)
        self.player.angle = degrees(angle)
        self.player.center_x += 10 * cos(angle)
        self.player.center_y += 10 * sin(angle)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.coin.draw()

    
    def on_mouse_motion(self, x, y, dx, dy):
        self.coin.center_x = x
        self.coin.center_y = y

my_game = Game()
my_game.setup()
arcade.run()