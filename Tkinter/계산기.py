import tkinter as tk
root = tk.Tk()

def func():
    n1 = int(e1.get())
    n2 = int(e2.get())
    operation = sel1.get()
        
    if operation == 1:
        result = n1 + n2
    elif operation == 2:
         result = n1 - n2
    elif operation == 3:
         result = n1 * n2
    elif operation == 4:
        if n2 != 0 or n1 != 0:
            result = n1 / n2
    label.config(text = result)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.pack()
e2.pack()

sel1 = tk.IntVar()
sel1.set(1)

rb1 = tk.Radiobutton(root,text='➕',variable=sel1,value=1)
rb1.pack()
rb2 = tk.Radiobutton(root,text='➖',variable=sel1,value=2)
rb2.pack()
rb3 = tk.Radiobutton(root,text='✖️',variable=sel1,value=3)
rb3.pack()
rb4 = tk.Radiobutton(root,text='➗',variable=sel1,value=4)
rb4.pack()

button = tk.Button(root,text='계산',command=func)
button.pack()

label=tk.Label(root,text="결과 : ")
label.pack()
root.mainloop()