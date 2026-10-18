import streamlit as st
import math

st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Scientific Calculator")
st.caption("Python + Streamlit")

if "display" not in st.session_state:
    st.session_state.display = ""

if "history" not in st.session_state:
    st.session_state.history = []


def add_to_display(value):
    st.session_state.display += value


def clear_display():
    st.session_state.display = ""


def backspace():
    st.session_state.display = st.session_state.display[:-1]


def calculate():
    try:
        original = st.session_state.display

        expression = original.replace("^", "**")
        expression = expression.replace("π", str(math.pi))

        result = eval(expression, {"__builtins__": {}}, {})

        st.session_state.display = str(result)
        st.session_state.history.append(
            f"{original} = {result}"
        )

    except:
        st.session_state.display = "Error"


def scientific_function(function_name):
    try:
        value = float(st.session_state.display)

        if function_name == "sqrt":
            if value < 0:
                raise ValueError
            result = math.sqrt(value)

        elif function_name == "square":
            result = value ** 2

        elif function_name == "sin":
            result = math.sin(math.radians(value))

        elif function_name == "cos":
            result = math.cos(math.radians(value))

        elif function_name == "tan":
            result = math.tan(math.radians(value))

        elif function_name == "percent":
            result = value / 100

        st.session_state.history.append(
            f"{function_name}({value}) = {result}"
        )

        st.session_state.display = str(result)

    except:
        st.session_state.display = "Error"


# Display
st.text_input(
    "Display",
    value=st.session_state.display,
    key="display_input",
    disabled=True
)

# Scientific buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("√", use_container_width=True):
        scientific_function("sqrt")

with col2:
    if st.button("x²", use_container_width=True):
        scientific_function("square")

with col3:
    if st.button("sin", use_container_width=True):
        scientific_function("sin")

with col4:
    if st.button("cos", use_container_width=True):
        scientific_function("cos")


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("tan", use_container_width=True):
        scientific_function("tan")

with col2:
    if st.button("π", use_container_width=True):
        add_to_display("π")

with col3:
    if st.button("^", use_container_width=True):
        add_to_display("^")

with col4:
    if st.button("%", use_container_width=True):
        scientific_function("percent")


# Calculator buttons
buttons = [
    ["C", "⌫", "(", ")"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "+/-", "+"]
]

for row in buttons:
    columns = st.columns(4)

    for index, button in enumerate(row):
        with columns[index]:

            if st.button(button, use_container_width=True):

                if button == "C":
                    clear_display()

                elif button == "⌫":
                    backspace()

                elif button == "+/-":
                    try:
                        value = float(st.session_state.display)
                        st.session_state.display = str(-value)
                    except:
                        st.session_state.display = "Error"

                else:
                    add_to_display(button)


if st.button("=", use_container_width=True):
    calculate()


# History
st.subheader("📜 Calculation History")

if st.session_state.history:

    for item in reversed(st.session_state.history):
        st.write("•", item)

    if st.button("CLEAR HISTORY"):
        st.session_state.history = []

else:
    st.write("No calculations yet.")