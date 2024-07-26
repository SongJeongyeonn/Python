import tkinter as tk
root = tk.Tk()
def func(ev):
    label.config(text=e.get())
label = tk.Label(root, text = 'Input Text')
label.pack()

e = tk.Entry(root)
e.pack()

button = tk.Button(root, text='Push', command = func)
button.pack()
button.bind('<Button-1>', func)

root.mainloop()