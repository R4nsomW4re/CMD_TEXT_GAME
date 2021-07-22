from text_object import text_object
from gui_class import screen
import time
import curses

game_screen = screen()
playing = 1

w = game_screen.w
h = game_screen.h

def main(screen):

    total_difference = 0
    text = text_object("Hello world!")
    word = []

    while playing == 1:

        t1_start = time.perf_counter_ns()

        key = game_screen.stdscr.getch()

        if key == 119:
            word.append(text.get_character())
            text.next_character()
        elif key == 115:
            text.prev_character()
        elif key == 113:
            exit()

        game_screen.start_draw()

        for i in range(len(word)):
            game_screen.draw_text(w//2 + i - len(word) , h//2, word[i])
        

        game_screen.draw_text(3, h - 1, f"te:  {round(total_difference * .000000001, 10)}")

        game_screen.end_draw()

        t1_stop = time.perf_counter_ns()
        difference = t1_stop - t1_start
        total_difference += difference

curses.wrapper(main)