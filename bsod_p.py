import tkinter as tk

BLUE = "#0078D7"
WHITE = "#FFFFFF"

root = tk.Tk()
root.configure(bg=BLUE)
root.title("")

# Full-screen visual simulation
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.configure(cursor="none")

# Emergency exit remains available, but isn't displayed.
root.bind("<Escape>", lambda event: root.destroy())

# Main BSOD content
content = tk.Frame(root, bg=BLUE)
content.place(relx=0.5, rely=0.5, anchor="center",
              relwidth=0.72, relheight=0.82)

sad_face = tk.Label(
    content,
    text=":(",
    bg=BLUE,
    fg=WHITE,
    font=("Segoe UI Light", 76),
    anchor="w"
)
sad_face.pack(fill="x", pady=(0, 22))

message = tk.Label(
    content,
    text=(
        "Your device ran into a problem and needs to restart.\n"
        "We're just collecting some error info, and then we'll restart for you."
    ),
    bg=BLUE,
    fg=WHITE,
    font=("Segoe UI", 19),
    justify="left",
    anchor="w",
    wraplength=900
)
message.pack(fill="x", pady=(0, 24))

progress = tk.Label(
    content,
    text="0% complete",
    bg=BLUE,
    fg=WHITE,
    font=("Segoe UI", 17),
    anchor="w"
)
progress.pack(fill="x", pady=(0, 36))

stop_code = tk.Label(
    content,
    text=(
        "Stop code: CRITICAL_PROCESS_DIED\n"
        "\n"
        "This is a simulated blue screen."
    ),
    bg=BLUE,
    fg=WHITE,
    font=("Segoe UI", 11),
    justify="left",
    anchor="w"
)
stop_code.pack(fill="x")

# Animate the displayed percentage only.
percentage = 0


def update_progress():
    global percentage

    if not root.winfo_exists():
        return

    percentage = min(percentage + 1, 100)
    progress.config(text=f"{percentage}% complete")

    if percentage < 100:
        root.after(1800, update_progress)


root.after(1500, update_progress)
root.mainloop()