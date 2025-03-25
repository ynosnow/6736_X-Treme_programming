import tkinter as tk

def save(value):
    with open("todo.txt", "a") as f:
        f.write(f"{value}\n")

def del_button():
    button = tk.Button(del_button, text="DEL", width=5, height=1)
    button.pack(side=tk.RIGHT)
    return button

try:
    f = open("todo.txt", "r")
except:
    f = open("todo.txt", "w")

window = tk.Tk()

input = tk.Entry(window, font=("Arial", 20))

remind = tk.Button(
    text="Add to List",
    width=10,
    height=2,
    command=lambda: save(input.get()),
)

window.title("The ToDo list Program")

input.pack(pady=5)
remind.pack(pady=5)
button_frame = tk.Frame(window)
button_frame.pack()

with open("todo.txt", "r") as file:
    for line in file:
        button = del_button()
        list = tk.Label(text=line.strip())
        list.pack()

window.mainloop()
f.close()