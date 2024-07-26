import tkinter as tk
root=tk.Tk()
def func():
    label.config(text='Pushed')
def func_event(ev):
    label.config(text='Leave')
def func_event1(ev):
    label.config(text='Enter')

label=tk.Label(root,text="PushButton")
label.pack()
button=tk.Button(root,text='Push',command=func)
button.pack()

button.bind('<Leave>',func_event)
button.bind('<Enter>',func_event1)
root.mainloop()