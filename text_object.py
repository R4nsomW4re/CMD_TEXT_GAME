class text_object:
    cursor_pos = 0

    def __init__(self, text: str) -> None:
        self.text = text

    def get_character(self) -> str:
        return str(self.text[self.cursor_pos])

    def next_character(self) -> None:
        self.cursor_pos += 1

    def prev_character(self) -> None:
        self.cursor_pos -= 1

    def set_character(self, pos) -> None:
        self.cursor_pos = pos

    def reset_character(self) -> None:
        self.cursor_pos = 0