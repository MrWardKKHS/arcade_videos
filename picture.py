import arcade

WIDTH = 600
HEIGHT = 600
snowman_x = WIDTH/2
snowman_y = HEIGHT/3
snowman_size = 1

def snowman(x, y, size=1):
    arcade.draw_circle_filled(x, y, 90*size, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y+(70*size), 60*size, arcade.color.WHITE)
    arcade.draw_circle_filled(x, y+130*size, 40*size, arcade.color.WHITE)
    arcade.draw_point(x + 20*size, y+140*size, (0,0,0), 5*size)
    arcade.draw_point(x - 20*size, y+140*size, (0,0,0), 5*size)
    arcade.draw_line(x - 20*size, y+130*size, x + 20*size, y+130*size, (0,0,0), 5*size)

arcade.open_window(WIDTH, HEIGHT, "My picture")

arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

def on_draw(delta_time):
    global snowman_x
    global snowman_y
    global snowman_size
    arcade.start_render()
    snowman(snowman_x, snowman_y, snowman_size)
    arcade.finish_render()
    snowman_x += 1
    snowman_y += 2
    snowman_size *= 0.99

arcade.schedule(on_draw, 1/60)
arcade.run()