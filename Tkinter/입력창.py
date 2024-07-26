import tkinter as tk
root = tk.Tk()

lbl = tk.Label(root,text="EduCoding",underline = 3)
lbl.pack()

txt = tk.Entry(root)
txt.pack()

btn = tk.Button(root, text="OK",activebackground="red",width=5)
btn.pack()

root.mainloop()