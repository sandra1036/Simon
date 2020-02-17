from tkinter import *
from tkinter import ttk
from F2romero_orozco import Simon

root=Tk()
f=ttk.Frame(root)
f.pack()
simon=Simon(f,width=350,height=350)
simon.grid(column=0,row=0)

simon2=Simon(f,width=400,height=400)
simon2.grid(column=1,row=0)
root.mainloop()