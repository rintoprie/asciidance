# 🎭 ASCII Dancer

A playful terminal animation written in pure Python.

This little program makes an ASCII character dance across your terminal and randomly jump to new positions every few moves.

No external libraries required — just Python and your terminal.


## ✨ Features

- 🎬 Smooth ASCII animation
- 🎲 Random movement across the terminal
- 🧹 Clean screen redraw using ANSI escape codes
- 🐍 Pure Python (no dependencies)


## 🎨 Example Frames

```
(>^_^)>  
<(^_^<)  
^(^_^)^  
v(^_^)v  
```


## 🎥 Preview

```
            (>^_^)>
  
ASCII dance (Ctrl+C to stop)
```

The dancer moves around your screen while switching poses!


## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/rintoprie/asciidance.git
cd asciidance
```

### 2️⃣ Run the program

```bash
python3 dancer.py
```

Press **Ctrl + C** to stop.


## 🛠 Requirements

- Python 3.x
- A terminal that supports ANSI escape codes  
  (macOS, Linux, Windows Terminal, modern PowerShell)


## 🧠 How It Works

The animation uses:

- `itertools.cycle()` for looping frames
- ANSI escape sequences for:
  - Clearing the screen
  - Moving the cursor
- `shutil.get_terminal_size()` to stay within bounds
- Random positioning every few frames


## 🌟 Why This Project?

This project demonstrates how powerful terminal control really is.

Animation using nothing but:
- Characters
- Coordinates
- Escape sequences
- Timing

Also
- Terminal control using ANSI escape codes
- Real-time animation in CLI
- Clean stdout manipulation
- Lightweight Python scripting

Perfect as a beginner-friendly terminal graphics project.
  
  
---

## 🧠 How It Works (Deep Dive)

This project animates text by directly controlling the terminal using **ANSI escape codes**.

The terminal is not magic — it’s just a 2D grid of character cells.

Think of it like this:

```
(1,1) ----------------------> columns →
   |
   |
   |
   v
 rows ↓
```

More concretely:

```
(1,1)  (1,2)  (1,3)  (1,4) ...
(2,1)  (2,2)  (2,3)  (2,4) ...
(3,1)  (3,2)  (3,3)  (3,4) ...
...
```

Each position is a coordinate:
```
(row, column)
```

⚠️ Terminal coordinates are **1-based**, not 0-based.  
Top-left corner = `(1,1)`


## 🎯 Controlling the Terminal with ANSI Escape Codes

ANSI escape codes are special sequences that begin with the **ESC character**:

```
\033[
```

(`\033` is the escape character in Python)

We use the following key codes:

### 🧹 Clear the Screen

```
\033[2J
```

Clears the entire visible screen.


### 🏠 Move Cursor to Home (Top-Left)

```
\033[H
```

Moves the cursor to position `(1,1)`.


### 📍 Move Cursor to a Specific Coordinate

```
\033[{row};{col}H
```

Example in Python:

```python
def move(row, col):
    return f"\033[{row};{col}H"
```

If you call:

```python
move(10, 20)
```

The cursor jumps to row 10, column 20.

That’s how the dancer “teleports” around the screen.


## 📐 Getting the Window Size

To keep the dancer inside the visible area, we must know the terminal dimensions.

We use:

```python
import shutil

cols, rows = shutil.get_terminal_size((80, 24))
```

This returns:

- `cols` → number of columns (width)
- `rows` → number of rows (height)

We then calculate safe bounds:

```python
max_col = cols - len(frame) - 1
max_row = rows - 2
```

This prevents the ASCII dancer from overflowing off-screen.


## 👁 Hiding and Restoring the Cursor

During animation, the blinking cursor is distracting.

So we hide it using:

```
\033[?25l
```

To restore it:

```
\033[?25h
```

In Python:

```python
def hide_cursor():
    return "\033[?25l"

def show_cursor():
    return "\033[?25h"
```

We restore the cursor inside a `finally` block to ensure the terminal isn’t left in a weird state.


## 🔁 The Animation Loop

The illusion of motion is created by:

```python
itertools.cycle(frames)
```

Each frame:

1. Optionally choose a new random `(row, col)`
2. Clear the screen
3. Move cursor
4. Print ASCII frame
5. Sleep briefly
6. Repeat

Because this happens ~6–10 times per second, your brain interprets it as animation.


## 🖥 What’s Really Happening?

The terminal is just:

- A character buffer
- A movable cursor
- A grid of printable cells

By controlling:
- Where the cursor goes
- What gets printed
- When the screen clears

We simulate graphics using pure text.

No graphics engine.
No GUI framework.
No game library.

Just control sequences and timing.


## 🪟 Windows Compatibility

Modern terminals support ANSI escape codes:

- Linux terminals ✅
- macOS Terminal ✅
- Windows Terminal ✅
- PowerShell (modern Windows 10/11) ✅

For Windows, ANSI is enabled with:

```python
if os.name == "nt":
    os.system("")
```
  
  
---
   
  
## 📜 License

MIT License — free to use, modify, and share.


