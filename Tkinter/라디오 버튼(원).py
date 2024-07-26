import tkinter as tk
root = tk.Tk()
sel1 = tk.IntVar()
sel1.set(1)

sel2 = tk.IntVar()
sel2.set(1)

rb1 = tk.Radiobutton(root,text='A',variable=sel1,value=1)
rb1.pack()
rb2 = tk.Radiobutton(root,text='B',variable=sel1,value=2)
rb2.pack()
rb3 = tk.Radiobutton(root,text='X',variable=sel2,value=1)
rb3.pack()
rb4 = tk.Radiobutton(root,text='Y',variable=sel2,value=2)
rb4.pack()
root.mainloop()