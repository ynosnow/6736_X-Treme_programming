import tkinter as tk

def save(value):
    with open("todo.txt", "a") as f:
        f.write(f"{value}\n")

def create_widget(parent, widget_type, **options):
    return widget_type(parent, **options)

def del_button(parent, item_frame):
    button = tk.Button(parent, text="DEL", width=5, height=1, command=lambda: item_frame.destroy())
    button.pack(side=tk.RIGHT)
    return button

def add_to_list():
    value = input.get()
    if value.strip(): 
        save(value)
        input.delete(0, tk.END) 
        create_list_item(value)

def create_list_item(value):
    item_frame = tk.Frame(button_frame)
    item_frame.pack(fill=tk.X, pady=2)

    list_label = tk.Label(item_frame, text=value)
    list_label.pack(side=tk.LEFT)

    del_button(item_frame, item_frame)

try:
    f = open("todo.txt", "r")
except FileNotFoundError:
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
    command=add_to_list,
)
remind.pack(side=tk.LEFT)

window.title("The ToDo list Program")

frame = create_widget(window, tk.Frame)

button_frame = tk.Frame(window)
button_frame.pack()
frame.pack()


with open("todo.txt", "r") as file:
    for line in file:
        create_list_item(line.strip())

window.mainloop()