import tkinter as tk
from tkinter import Frame, Entry, Button, Label


class ToDoApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("The ToDo list Program")

        self.input_frame: Frame = Frame(self.root)
        self.input_frame.pack(pady=5)

        self.input: Entry = Entry(self.input_frame, font=("Arial", 20))
        self.input.pack(side=tk.LEFT)

        self.add_button: Button = Button(
            self.input_frame,
            text="Add to List",
            width=10,
            height=2,
            command=self.add_to_list,
        )
        self.add_button.pack(side=tk.LEFT)

        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        self.load_items()

    def save(self, value: str) -> None:
        with open("todo.txt", "a") as f:
            f.write(f"{value}\n")

    def delete_from_file(self, value: str) -> None:
        with open("todo.txt", "r") as f:
            lines = f.readlines()
        with open("todo.txt", "w") as f:
            for line in lines:
                if line.strip() != value:
                    f.write(line)

    def add_to_list(self) -> None:
        value: str = self.input.get()
        if value.strip():
            self.save(value)
            self.input.delete(0, tk.END)
            self.create_list_item(value)

    def create_list_item(self, value: str) -> None:
        item_frame: Frame = Frame(self.button_frame)
        item_frame.pack(fill=tk.X, pady=2)

        list_label: Label = Label(item_frame, text=value)
        list_label.pack(side=tk.LEFT)

        del_button: Button = Button(
            item_frame,
            text="DEL",
            width=5,
            height=1,
            command=lambda: [item_frame.destroy(), self.delete_from_file(value)],
        )
        del_button.pack(side=tk.RIGHT)

    def load_items(self) -> None:
        try:
            with open("todo.txt", "r") as file:
                for line in file:
                    self.create_list_item(line.strip())
        except FileNotFoundError:
            with open("todo.txt", "w"):
                pass


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()