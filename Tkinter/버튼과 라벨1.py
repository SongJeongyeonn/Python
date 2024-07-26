import tkinter as tk
root = tk.Tk()

def func():
    label.config(text='Pushed')

label= tk.Label(root,text='Push Button')
label.pack()

button = tk.Button(root,text='Push!',command=func)
button.pack()
root.mainloop()