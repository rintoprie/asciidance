import itertools
import os
import shutil
import sys
import time

# Enable ANSI on Windows (safe on Linux/macOS)
if os.name == "nt":
    os.system("")

frames = ["(>^_^)>", "<(^_^<)", "^(^_^)^", "v(^_^)v"]

DELAY = 0.25   # smaller = smoother
VX = 1         # horizontal speed (columns per frame)
VY = 1         # vertical speed (rows per frame)

def clear():
    return "\033[2J\033[H"

def move(row, col):
    # 1-based coordinates for ANSI cursor positioning
    return f"\033[{row};{col}H"

def hide_cursor():
    return "\033[?25l"

def show_cursor():
    return "\033[?25h"

# Position is stored as 0-based for math, converted to 1-based when printing.
x, y = 0, 0
vx, vy = VX, VY

try:
    sys.stdout.write(hide_cursor())
    sys.stdout.flush()

    for frame in itertools.cycle(frames):
        cols, rows = shutil.get_terminal_size((80, 24))

        # playable area (keep last row for status text)
        max_x = max(0, cols - len(frame) - 1)
        max_y = max(0, rows - 2)

        # Clamp position if terminal shrinks
        x = min(max(x, 0), max_x)
        y = min(max(y, 0), max_y)

        # Advance
        x_next = x + vx
        y_next = y + vy

        # Bounce on walls (reflect velocity)
        if x_next < 0:
            x_next = 0
            vx = -vx
        elif x_next > max_x:
            x_next = max_x
            vx = -vx

        if y_next < 0:
            y_next = 0
            vy = -vy
        elif y_next > max_y:
            y_next = max_y
            vy = -vy

        x, y = x_next, y_next

        # Draw
        sys.stdout.write(clear())
        sys.stdout.write(move(y + 1, x + 1))
        sys.stdout.write(frame)
        sys.stdout.write(move(rows, 1))
        sys.stdout.write("github.com/rintoprie/asciidance")
        sys.stdout.flush()

        time.sleep(DELAY)

except KeyboardInterrupt:
    pass
finally:
    sys.stdout.write(show_cursor() + "\033[0m\n")

    sys.stdout.flush()
