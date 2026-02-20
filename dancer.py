# import itertools, sys, time

# frames = ["(>^_^)>", "<(^_^<)", "^(^_^)^", "v(^_^)v"]
# for f in itertools.cycle(frames):
#     # Clear screen + move cursor to top-left (ANSI escape codes)
#     sys.stdout.write("\033[2J\033[H")

#     sys.stdout.write(f)
#     sys.stdout.flush()
#     time.sleep(0.15)

import itertools
import random
import shutil
import sys
import time

frames = ["(>^_^)>", "<(^_^<)", "^(^_^)^", "v(^_^)v"]

MOVE_EVERY = 8      # change position every 8 frames
DELAY = 0.15

def move_cursor(row: int, col: int) -> str:
    # ANSI cursor positioning is 1-based: \033[{row};{col}H
    return f"\033[{row};{col}H"

def clear_screen() -> str:
    # Clear screen + move cursor to top-left
    return "\033[2J\033[H"

def clamp(n, lo, hi):
    return max(lo, min(hi, n))

# initial position
term = shutil.get_terminal_size(fallback=(80, 24))
row, col = 1, 1
frame_count = 0

try:
    for f in itertools.cycle(frames):
        term = shutil.get_terminal_size(fallback=(80, 24))
        cols, rows = term.columns, term.lines

        # pick new random position every few frames
        if frame_count % MOVE_EVERY == 0:
            # keep within bounds (leave room for the frame text)
            max_col = max(1, cols - len(f) - 1)
            max_row = max(1, rows - 2)
            col = random.randint(1, max_col)
            row = random.randint(1, max_row)

        sys.stdout.write(clear_screen())
        sys.stdout.write(move_cursor(row, col))
        sys.stdout.write(f)
        sys.stdout.write(move_cursor(rows, 1))
        sys.stdout.write("github.com/rintoprie/asciidance")
        sys.stdout.flush()

        time.sleep(DELAY)
        frame_count += 1

except KeyboardInterrupt:
    # reset formatting & move cursor nicely
    sys.stdout.write("\033[0m\n")