from gui_class import screen
import time
import curses

game_screen = screen()
playing = 1

w = game_screen.w
h = game_screen.h


def main(screen):

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    commands = ["echo", "help"]
    MAX_LENGTH = 108
    left_command_list = ["Hello", "How's it goin'"]
    total_difference = 0

    while playing == 1:

        t1_start = time.perf_counter_ns()

        key = game_screen.stdscr.getch()

        if key == curses.KEY_ENTER or key in [10, 13]:
            if left_command_list[0]:
                left_command_list.insert(0, "")
        elif key == curses.KEY_END:
            exit()
        elif key == curses.KEY_DOWN:
            left_command_list[0] = left_command_list[0][:-1]
        elif key != -1:
            if len(left_command_list[0]) < MAX_LENGTH:
                left_command_list[0] = left_command_list[0] + chr(key)

        game_screen.start_draw()

        if left_command_list:
            for index, command in enumerate(left_command_list):
                if command.split(" ")[0] in commands:
                    game_screen.draw_text(3, h - 3 - index, ">> " + command, mode=curses.color_pair(1))
                else:
                    game_screen.draw_text(3, h - 3 - index, ">> " + command)
                game_screen.draw_text(w - 10, h - 3 - index, command.split(" ")[0])

        game_screen.end_draw()

    #Timer Stuff
        game_screen.draw_text(3, h - 1, f"te:  {round(total_difference * .000000001, 10)}")
        t1_stop = time.perf_counter_ns()
        difference = t1_stop - t1_start
        total_difference += difference

curses.wrapper(main)