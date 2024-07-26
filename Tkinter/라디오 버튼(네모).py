import tkinter as tk
def Action1():
    lbl.config(text="Option1")
def Action2():
    lbl.config(text="Option2")

root = tk.Tk()

lbl = tk.Label(root, text="EduCoding", underline=3)
lbl.pack()

rbvar=""
rb1 = tk.Radiobutton(root,text="Option1", variable=rbvar,value='a',indicatoron=0,command=Action1)

rb1.pack()
rb2 = tk.Radiobutton(root,text="Option2", variable=rbvar,value='b',indicatoron=0,command=Action2)

rb2.pack()
root.mainloop()