import tkinter as tk
import math


# ================= WINDOW =================

window = tk.Tk()
window.title("Scientific Calculator")
window.geometry("400x760")
window.resizable(False, False)
window.configure(bg="#202124")


# ================= DISPLAY =================

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


# ================= HISTORY =================

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
    font=("Arial", 11),
    bg="#303134",
    fg="white",
    bd=0
)

history_box.pack(
    fill="both",
    padx=15,
    pady=10
)


# ================= BASIC FUNCTIONS =================

def button_click(value):
    display.insert(tk.END, value)


def clear_display():
    display.delete(0, tk.END)


def backspace():
    current = display.get()

    if current:
        display.delete(len(current) - 1, tk.END)


# ================= CALCULATE =================

def calculate():
    try:
        original_expression = display.get()

        expression = original_expression.replace("^", "**")
        expression = expression.replace("π", str(math.pi))

        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, result)

        history_box.insert(
            tk.END,
            f"{original_expression} = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# ================= SCIENTIFIC FUNCTIONS =================

def square_root():
    try:
        expression = display.get()
        value = float(expression)

        if value < 0:
            raise ValueError

        result = math.sqrt(value)

        display.delete(0, tk.END)
        display.insert(0, result)

        history_box.insert(
            tk.END,
            f"√{value} = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def square():
    try:
        expression = display.get()
        value = float(expression)

        result = value ** 2

        display.delete(0, tk.END)
        display.insert(0, result)

        history_box.insert(
            tk.END,
            f"{value}² = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def sine():
    try:
        value = float(display.get())

        result = math.sin(math.radians(value))

        display.delete(0, tk.END)
        display.insert(0, result)

        history_box.insert(
            tk.END,
            f"sin({value}) = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def cosine():
    try:
        value = float(display.get())

        result = math.cos(math.radians(value))

        display.delete(0, tk.END)
        display.insert(0, result)

        history_box.insert(
            tk.END,
            f"cos({value}) = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def tangent():
    try:
        value = float(display.get())

        result = math.tan(math.radians(value))

        display.delete(0, tk.END)
        display.insert(0, result)

        history_box.insert(
            tk.END,
            f"tan({value}) = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def percentage():
    try:
        value = float(display.get())

        result = value / 100

        display.delete(0, tk.END)
        display.insert(0, result)

        history_box.insert(
            tk.END,
            f"{value}% = {result}"
        )

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


def plus_minus():
    try:
        value = float(display.get())

        result = -value

        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# ================= HISTORY =================

def clear_history():
    history_box.delete(0, tk.END)


# ================= SCIENTIFIC BUTTONS =================

scientific_buttons = [
    ("√", square_root, 0, 0),
    ("x²", square, 0, 1),
    ("sin", sine, 0, 2),
    ("cos", cosine, 0, 3),

    ("tan", tangent, 1, 0),
    ("π", lambda: button_click("π"), 1, 1),
    ("^", lambda: button_click("^"), 1, 2),
    ("%", percentage, 1, 3)
]


button_frame = tk.Frame(
    window,
    bg="#202124"
)

button_frame.pack()


for text, command, row, column in scientific_buttons:

    tk.Button(
        button_frame,
        text=text,
        font=("Arial", 14, "bold"),
        width=5,
        height=2,
        bg="#5f6368",
        fg="white",
        activebackground="#80868b",
        bd=0,
        command=command
    ).grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# ================= BASIC BUTTONS =================

buttons = [
    ("C", clear_display, 2, 0),
    ("⌫", backspace, 2, 1),
    ("(", lambda: button_click("("), 2, 2),
    (")", lambda: button_click(")"), 2, 3),

    ("7", lambda: button_click("7"), 3, 0),
    ("8", lambda: button_click("8"), 3, 1),
    ("9", lambda: button_click("9"), 3, 2),
    ("/", lambda: button_click("/"), 3, 3),

    ("4", lambda: button_click("4"), 4, 0),
    ("5", lambda: button_click("5"), 4, 1),
    ("6", lambda: button_click("6"), 4, 2),
    ("*", lambda: button_click("*"), 4, 3),

    ("1", lambda: button_click("1"), 5, 0),
    ("2", lambda: button_click("2"), 5, 1),
    ("3", lambda: button_click("3"), 5, 2),
    ("-", lambda: button_click("-"), 5, 3),

    ("0", lambda: button_click("0"), 6, 0),
    (".", lambda: button_click("."), 6, 1),
    ("+/-", plus_minus, 6, 2),
    ("+", lambda: button_click("+"), 6, 3)
]


for text, command, row, column in buttons:

    tk.Button(
        button_frame,
        text=text,
        font=("Arial", 17, "bold"),
        width=5,
        height=2,
        bg="#3c4043",
        fg="white",
        activebackground="#5f6368",
        bd=0,
        command=command
    ).grid(
        row=row,
        column=column,
        padx=5,
        pady=5
    )


# ================= EQUAL BUTTON =================

tk.Button(
    button_frame,
    text="=",
    font=("Arial", 18, "bold"),
    width=23,
    height=2,
    bg="#3c4043",
    fg="white",
    activebackground="#5f6368",
    bd=0,
    command=calculate
).grid(
    row=7,
    column=0,
    columnspan=4,
    padx=5,
    pady=5
)


# ================= CLEAR HISTORY =================

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


# ================= KEYBOARD SUPPORT =================

def keyboard_input(event):

    if event.keysym == "Return":
        calculate()

    elif event.keysym == "Escape":
        clear_display()

    elif event.keysym == "BackSpace":
        backspace()


window.bind("<Key>", keyboard_input)


# ================= START =================

window.mainloop()