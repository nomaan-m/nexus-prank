import tkinter as tk
from tkinter import font
from datetime import datetime

# SIMULATION ONLY: no files, network, or system settings are accessed.

BG = "#050807"
GREEN = "#39ff88"
DIM_GREEN = "#168c52"
RED = "#ff4d5a"
WHITE = "#d7ffe5"

root = tk.Tk()
root.title("")
root.configure(bg=BG)

# Full-screen presentation: no title bar or visible taskbar.
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(cursor="none")

mono = font.Font(family="Consolas", size=11)
bold = font.Font(family="Consolas", size=12, weight="bold")

header = tk.Label(
    root,
    text="NEXUS // SYSTEM DIAGNOSTICS",
    bg=BG,
    fg=GREEN,
    font=bold,
    anchor="w",
    padx=24,
    pady=20
)
header.pack(fill="x")

subtitle = tk.Label(
    root,
    text="",
    bg=BG,
    fg=DIM_GREEN,
    font=("Consolas", 9),
    anchor="w",
    padx=24
)
subtitle.pack(fill="x")

output = tk.Text(
    root,
    bg=BG,
    fg=GREEN,
    insertbackground=GREEN,
    font=mono,
    wrap="word",
    relief="flat",
    padx=24,
    pady=24,
    state="disabled",
    cursor="arrow",
    borderwidth=0,
    highlightthickness=0
)
output.pack(fill="both", expand=True)

output.tag_config("normal", foreground=GREEN)
output.tag_config("dim", foreground=DIM_GREEN)
output.tag_config("warning", foreground=RED)
output.tag_config("joke", foreground=WHITE)

# No visible exit instructions during the animation.
footer = tk.Label(
    root,
    text="",
    bg=BG,
    fg=DIM_GREEN,
    font=("Consolas", 10),
    pady=16
)
footer.pack(fill="x")


def write_line(message, tag="normal"):
    output.configure(state="normal")
    timestamp = datetime.now().strftime("%H:%M:%S")
    output.insert("end", f"[{timestamp}] {message}\n", tag)
    output.see("end")
    output.configure(state="disabled")


def exit_program(event=None):
    root.destroy()


# Emergency exit works at all times.
root.bind("<Escape>", exit_program)


events = [
    (500, "Initializing diagnostic environment...", "dim"),
    (700, "Loading fictional security modules...", "normal"),
    (700, "Checking simulated system status...", "normal"),
    (800, "Analyzing imaginary threat signatures...", "normal"),
    (700, "Scanning files: SIMULATION ONLY", "dim"),
    (500, "Progress: [##........] 20%", "normal"),
    (400, "Progress: [####......] 40%", "normal"),
    (400, "Progress: [######....] 60%", "normal"),
    (500, "Progress: [########..] 80%", "normal"),
    (500, "Progress: [##########] 100%", "normal"),
    (700, "WARNING: suspicious user activity detected!", "warning"),
    (1000, "Investigating source of suspicious activity...", "dim"),
    (1000, "Checking keyboard interaction patterns...", "normal"),
    (1000, "Analyzing repeated button clicks...", "normal"),
    (1000, "THREAT IDENTIFIED.", "warning"),
    (1000, "Threat source: THE USER.", "warning"),
    (1200, "Calculating recommended response...", "dim"),
    (1000, "Recommendation: remain calm.", "normal"),
    (1200, "Additional finding: user clicked Retry repeatedly.", "joke"),
    (1200, "Estimated technical expertise: confidently curious.", "joke"),
    (1200, "Cybersecurity status: watching too many movies.", "joke"),
    (1500, "", "normal"),
    (500, "FINAL REPORT", "joke"),
    (700, "No files were scanned or modified.", "joke"),
    (700, "No hacker was found in your computer.", "joke"),
    (900, "Your computer is fine. Your curiosity is not.", "joke"),
    (1000, "PRANK COMPLETE.", "joke"),
    (700, "YOU ARE A CERTIFIED IDIOT.", "warning"),
]

index = 0


def run_next():
    global index

    if not root.winfo_exists():
        return

    if index >= len(events):
        footer.config(
            text="PRESS ESC TO EXIT",
            fg=WHITE
        )
        return

    delay, message, tag = events[index]
    index += 1

    if message:
        write_line(message, tag)

    root.after(delay, run_next)


write_line("NEXUS DIAGNOSTICS v1.0", "joke")
write_line("Initializing secure environment...", "dim")
write_line("Starting sequence...", "dim")

root.after(900, run_next)
root.mainloop()