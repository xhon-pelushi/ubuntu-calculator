import tkinter as tk
from tkinter import messagebox

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        op = operation.get()
        if op == "Add":
            result = add(a, b)
        elif op == "Subtract":
            result = subtract(a, b)
        elif op == "Multiply":
            result = multiply(a, b)
        elif op == "Divide":
            result = divide(a, b)
        else:
            result = "Invalid operation"
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Ubuntu Calculator (GUI)")

entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

label_a = tk.Label(root, text="First number:")
label_a.grid(row=0, column=0)
label_b = tk.Label(root, text="Second number:")
label_b.grid(row=1, column=0)

operation = tk.StringVar(root)
operation.set("Add")
operations_menu = tk.OptionMenu(root, operation, "Add", "Subtract", "Multiply", "Divide")
operations_menu.grid(row=2, column=1)

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=1)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=1)

root.mainloop()
