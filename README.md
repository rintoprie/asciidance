# 🎭 ASCII Dancer

A playful terminal animation written in pure Python.

This little program makes an ASCII character dance across your terminal and randomly jump to new positions every few moves.

No external libraries required — just Python and your terminal.

---

## ✨ Features

- 🎬 Smooth ASCII animation
- 🎲 Random movement across the terminal
- 🧹 Clean screen redraw using ANSI escape codes
- 🐍 Pure Python (no dependencies)

---

## 🎥 Preview

```
            (>^_^)>  
ASCII dance (Ctrl+C to stop)
```

The dancer moves around your screen while switching poses!

---

## 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/random-ascii-dancer.git
cd random-ascii-dancer
```

### 2️⃣ Run the program

```bash
python3 dancer.py
```

Press **Ctrl + C** to stop.

---

## 🛠 Requirements

- Python 3.x
- A terminal that supports ANSI escape codes  
  (macOS, Linux, Windows Terminal, modern PowerShell)

---

## 🧠 How It Works

The animation uses:

- `itertools.cycle()` for looping frames
- ANSI escape sequences for:
  - Clearing the screen
  - Moving the cursor
- `shutil.get_terminal_size()` to stay within bounds
- Random positioning every few frames

---

## 🎨 Example Frames

```
(>^_^)>  
<(^_^<)  
^(^_^)^  
v(^_^)v  
```

---

## 🌟 Why This Project?

This project demonstrates:

- Terminal control using ANSI escape codes
- Real-time animation in CLI
- Clean stdout manipulation
- Lightweight Python scripting

Perfect as a beginner-friendly terminal graphics project.

---

## 📜 License

MIT License — free to use, modify, and share.

---

Made with ☕ and Python.
