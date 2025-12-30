import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for char in row:
        if char == '=':
            btn = tk.Button(row_frame, text=char, font=("Arial", 18),
                            command=calculate)
        else:
            btn = tk.Button(row_frame, text=char, font=("Arial", 18),
                            command=lambda c=char: press(c))
        btn.pack(side="left", expand=True, fill="both")

clear_btn = tk.Button(root, text="C", font=("Arial", 18), command=clear)
clear_btn.pack(fill="both", padx=10, pady=5)

root.mainloop()
