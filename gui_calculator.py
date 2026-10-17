import tkinter as tk


# ---------------- WINDOW ----------------

window = tk.Tk()
window.title("My Calculator")
window.geometry("380x700")
window.resizable(False, False)
window.configure(bg="#202124")


# ---------------- DISPLAY ----------------

display = tk.Entry(
    window,
    font=("Arial", 28),
    bg="#303134",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)

display.pack(
    fill="both",
    padx=15,
    pady=20,
    ipady=15
)


# ---------------- HISTORY ----------------

history_label = tk.Label(
    window,
    text="Calculation History",
    font=("Arial", 14, "bold"),
    bg="#202124",
    fg="white"
)

history_label.pack()


history_box = tk.Listbox(
    window,
    height=5,
    font=("Arial", 12),
    bg="#303134",
    fg="white",
    bd=0
)

history_box.pack(
    fill="both",
    padx=15,
    pady=10
)


# ---------------- FUNCTIONS ----------------

def button_click(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)


def backspace():
    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)


def percentage():
    try:
        value = float(display.get())
        result = value / 100

        display.delete(0, tk.END)
        display.insert(0, result)

    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def plus_minus():
    try:
        value = float(display.get())
        result = -value

        display.delete(0, tk.END)
        display.insert(0, result)

    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def calculate():
    try:
        expression = display.get()

        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, result)

        # Add calculation to history
        history_box.insert(
            tk.END,
            f"{expression} = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def clear_history():
    history_box.delete(0, tk.END)


# ---------------- BUTTON FRAME ----------------

button_frame = tk.Frame(
    window,
    bg="#202124"
)

button_frame.pack()


# ---------------- SPECIAL BUTTONS ----------------

special_buttons = [
    ("C", clear_display, 0, 0),
    ("⌫", backspace, 0, 1),
    ("%", percentage, 0, 2),
    ("+/-", plus_minus, 0, 3)
]


for text, command, row, column in special_buttons:

    tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16, "bold"),
        width=5,
        height=2,
        bg="#5f6368",
        fg="white",
        activebackground="#80868b",
        activeforeground="white",
        bd=0,
        command=command
    ).grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# ---------------- NUMBER BUTTONS ----------------

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),

    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),

    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),

    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 2),
    ("=", 4, 3)
]


for text, row, column in buttons:

    if text == "=":
        command = calculate
    else:
        command = lambda value=text: button_click(value)

    tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18),
        width=5,
        height=2,
        bg="#3c4043",
        fg="white",
        activebackground="#5f6368",
        activeforeground="white",
        bd=0,
        command=command
    ).grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# ---------------- CLEAR HISTORY ----------------

tk.Button(
    window,
    text="CLEAR HISTORY",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    bg="#d93025",
    fg="white",
    bd=0,
    command=clear_history
).pack(pady=10)


# ---------------- KEYBOARD SUPPORT ----------------

def keyboard_input(event):

    if event.keysym == "Return":
        calculate()

    elif event.keysym == "Escape":
        clear_display()

    elif event.keysym == "BackSpace":
        backspace()


window.bind("<Key>", keyboard_input)


# ---------------- START ----------------

window.mainloop()