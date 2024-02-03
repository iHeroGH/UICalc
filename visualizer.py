from calculator import Calculator

import tkinter as tk
from tkinter import Tk
import tkinter.font as font

class Visualizer:

    # FRAMING
    HEIGHT = 736
    WIDTH = 414
    BUTTON_PAD = 10

    # FONTS
    FONT_NAME = "Helvetica Neue"
    DISPLAY_FONT_SIZE = 50
    BUTTON_FONT_SIZE = 30

    # COLORS
    DISPLAY = "black", "white"
    SPECIAL_FUNCTIONS = "#A5A5A5", "black"
    NUMBERS = "#333333", "white"
    OPERATORS = "#FF9F0A", "white"

    def __init__(self):
        self.calculator = Calculator()

        self.height = Visualizer.HEIGHT
        self.width = Visualizer.WIDTH

        self._initialize_window()
        self._initialize_fonts()
        self._initialize_frame()
        self._begin()

    def _initialize_window(self) -> None:
        self.window = Tk("Calculator")
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.configure(background=Visualizer.DISPLAY[0])

    def _initialize_fonts(self) -> None:
        self.button_font = font.Font(
            family=Visualizer.FONT_NAME, size=Visualizer.BUTTON_FONT_SIZE
        )
        self.display_font = font.Font(
            family=Visualizer.FONT_NAME, size=Visualizer.DISPLAY_FONT_SIZE
        )

    def _initialize_frame(self) -> None:
        self.main_frame = tk.Frame(
            self.window,
            height=self.height,
            background=Visualizer.DISPLAY[0]
        )
        self.main_frame.grid()
        self.main_frame.pack(anchor="s", expand=True, ipady=Visualizer.BUTTON_PAD)

        self.input_label = tk.Label(
                self.main_frame,
                text=str(self.calculator),
                font=self.display_font,
                bg=Visualizer.DISPLAY[0],
                fg=Visualizer.DISPLAY[1]
            )
        self.input_label.grid(
            column=0, row=0, sticky='e', ipadx=Visualizer.BUTTON_PAD
        )

        self._initialize_buttons()

    def _initialize_buttons(self):
        self.button_frame = tk.Frame(
            self.main_frame,
            bg=Visualizer.DISPLAY[0]
        )
        self.button_frame.grid(column=0, row=1)

        button_labels = [
            ["AC", "+/-", "%", "/"],
            ["7", "8", "9", "X"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0 ", ".", "="]
        ]

        curr_row = 0
        curr_col = 0
        for label_group in button_labels:
            for label in label_group:
                spaces = label.count(" ") + 1

                used_colors = Visualizer.NUMBERS
                if not curr_row and curr_col <= len(button_labels[0]) - 2:
                    used_colors = Visualizer.SPECIAL_FUNCTIONS
                if curr_col == len(button_labels[0]) - 1:
                    used_colors = Visualizer.OPERATORS

                tk.Button(
                    self.button_frame,
                    text=label,
                    font=self.button_font,
                    anchor='w' if spaces > 1 else "center",
                    # Screen Edge -> Button Edge -> Text Edge
                    padx=Visualizer.BUTTON_PAD*3 if spaces > 1 else 0,
                    bg=used_colors[0],
                    fg=used_colors[1],
                    command=lambda label=label: self._process_button(label)
                ).grid(
                    row=curr_row, column=curr_col,
                    columnspan=label.count(" ") + 1,
                    padx=Visualizer.BUTTON_PAD, pady=Visualizer.BUTTON_PAD,
                    sticky="ew"
                )
                curr_col += spaces

            curr_row += 1
            curr_col = 0

    def _process_button(self, button_label: str) -> None:

        if button_label.lower().strip().isdigit():
            self.calculator.append_digit(button_label)
        else:
            self.calculator.symbol_to_operation(button_label)

        self.input_label.configure(text=str(self.calculator))

    def _begin(self) -> None:
        self.window.mainloop()

if __name__ == "__main__":
    vis = Visualizer()

