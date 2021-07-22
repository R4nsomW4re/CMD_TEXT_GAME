from gui_class import screen

game_screen = screen()
playing = 1

w = game_screen.w
h = game_screen.h

while playing == 1:
    game_screen.start_draw()


    game_screen.draw_text(w//2, h//2, "Hello World!")


    game_screen.end_draw()