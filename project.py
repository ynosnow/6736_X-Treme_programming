import tkinter as tk

def save(value, second):
    with open("todo.txt", "a") as f:
        f.write(f"{second}, {value}\n")

try:
    f = open("todo.txt", "r")
except:
    f = open("todo.txt", "w")

window = tk.Tk()

input = tk.Entry(window, font=("Arial", 20))

remind = tk.Button(
    text="Add to List",
    width=20,
    height=5,
    command=lambda: 
)

thelist = tk.Label(text="")

window.title("The ToDo list Program")

input.pack(pady=5)
thelist.pack()

with open("todo.txt", "r") as file:
    for line in file:
        c = tk.Label(text=line.strip())
        c.pack()

window.mainloop()
f.close()