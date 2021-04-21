import arcade

arcade.open_window(600, 600, "Drawing Shapes")

arcade.set_background_color((75, 167, 209))
arcade.start_render()

arcade.draw_circle_filled(300, 300, 25, (255, 150, 150))

arcade.finish_render()

arcade.run()