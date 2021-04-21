import arcade
from math import cos, sin

WIDTH = 800
HEIGHT = 800
TITLE = "Circles"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        self.set_mouse_visible(False)
        self.angle = 0
        self.moon_angle = 0

    def setup(self):
        self.coin = arcade.Sprite('coin.png', 0.4)
        self.moon = arcade.Sprite('coin.png', 0.2)
        self.coin.center_x = WIDTH/2 + 300
        self.coin.center_y = HEIGHT/2 + 0
        self.moon.center_x = self.coin.center_x + 100
        self.moon.center_y = self.coin.center_y + 100
    
    def update(self, delta_time):
        self.coin.center_x = WIDTH/2 + 300 * cos(self.angle)
        self.coin.center_y = HEIGHT/2 + 300 * sin(self.angle)
        self.angle -= 0.005

        self.moon.center_x = self.coin.center_x + 100 * cos(self.moon_angle)
        self.moon.center_y = self.coin.center_y + 100 * sin(self.moon_angle)
        self.moon_angle += 0.02111

    def on_draw(self):
        # arcade.start_render()
        self.coin.draw()
        self.moon.draw()
        arcade.draw_circle_filled(WIDTH/2, HEIGHT/2, 10, (0,0,0))

my_game = Game()
my_game.setup()
arcade.run()