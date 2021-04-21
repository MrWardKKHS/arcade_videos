import arcade
import random

WIDTH = 800
HEIGHT = 800
TITLE = "Sprites"

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)
        self.player_list = None
        self.coin_list = None
        self.score = None
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)
        self.set_mouse_visible(False)

    def setup(self):
        self.score = 0
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.player = arcade.Sprite("character_idle.png", 0.7)
        self.player.center_x = 200
        self.player.center_y = 100
        self.player_list.append(self.player)
        for i in range(50):
            coin = arcade.Sprite('coin.png', 0.4)
            coin.center_x = random.randint(0, WIDTH)
            coin.center_y = random.randint(0, HEIGHT)
            self.coin_list.append(coin)
    
    def update(self, delta_time):
        self.player_list.update()
        self.coin_list.update()
        coins_touching = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coins_touching:
            self.score += 1
            coin.kill()
        if len(self.coin_list) == 0:
            self.setup()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.score), WIDTH/2, HEIGHT/2, arcade.color.BLACK, 70)
        self.player_list.draw()
        self.coin_list.draw()

    
    def on_mouse_motion(self, x, y, dx, dy):
        self.player.center_x = x
        self.player.center_y = y

my_game = Game()
my_game.setup()
arcade.run()