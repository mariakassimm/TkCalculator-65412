import tkinter as tk
import math

def add():
    result.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result.set("Error")

def square():
    result.set(float(entry1.get()) ** 2)

def square_root():
    try:
        result.set(math.sqrt(float(entry1.get())))
    except ValueError:
        result.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

result = tk.StringVar()

tk.Label(root, text="Number 1").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Number 2").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Add", command=add).grid(row=2, column=0)
tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0)
tk.Button(root, text="Divide", command=divide).grid(row=3, column=1)
tk.Button(root, text="Square", command=square).grid(row=4, column=0)
tk.Button(root, text="Square Root", command=square_root).grid(row=4, column=1)

tk.Label(root, text="Result").grid(row=5, column=0)
tk.Entry(root, textvariable=result, state='readonly').grid(row=5, column=1)

root.mainloop()
