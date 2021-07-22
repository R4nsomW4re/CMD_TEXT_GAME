import curses
from text_object import text_object

class screen:
    stdscr = curses.initscr()
    h, w = stdscr.getmaxyx()
    middleX = w // 2
    middleY = h // 2

    def __init__(self):
        curses.curs_set(0)
        self.stdscr.nodelay(1)

    def draw_text(self, x: int, y: int, text, mode = None):
        if not mode:
            self.stdscr.addstr(y, x, text)
        else:
            self.stdscr.addstr(y, x, text, mode)

    def draw_char_from_text_object(self, x: int, y: int, text_object: text_object, mode = None):
        print(text_object.get_character())
        if not mode:
            self.stdscr.addstr(y, x, text_object.get_character())
        else:
            self.stdscr.addstr(y, x, text_object.get_character(), mode)

    def attron(self, attribute):
        self.stdscr.attron(attribute)

    def attroff(self, attribute):
        self.stdscr.attroff(attribute)
    
    def getch(self):
        self.stdscr.getch()

    def start_draw(self):
        self.stdscr.clear()

    def end_draw(self):
        self.stdscr.refresh()

