import tkinter as tk



def save(value):
    with open("todo.txt", "a") as f:
        f.write(f"{value}\n")

def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

def del_button(parent):
    button = tk.Button(parent, text="DEL", width=5, height=1)
    button.pack(side=tk.RIGHT)
    return button

try:
    f = open("todo.txt", "r")
except:
    f = open("todo.txt", "w")

window = tk.Tk()

input_frame = tk.Frame(window)
input_frame.pack(pady=5)

input = tk.Entry(input_frame, font=("Arial", 20))
input.pack(side=tk.LEFT)

remind = tk.Button(
    input_frame,
    text="Add to List",
    width=10,
    height=2,
    command=lambda: save(input.get()),
)
remind.pack(side=tk.LEFT)

window.title("The ToDo list Program")

frame = create_widget(window, tk.Frame)

button_frame = tk.Frame(window)
button_frame.pack()
frame.pack()

with open("todo.txt", "r") as file:
    for line in file:
        item_frame = tk.Frame(button_frame)
        item_frame.pack(fill=tk.X, pady=2)

        list_label = tk.Label(item_frame, text=line.strip())
        list_label.pack(side=tk.LEFT)

        button = del_button(item_frame)

window.mainloop()
f.close()