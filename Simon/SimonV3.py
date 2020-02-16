from tkinter import *
from tkinter import ttk
import numpy as np
from SimonClass import SimonClass
root=Tk()
f=ttk.Frame(root)
f.pack()
simon=SimonClass(f,width=500,height=500)
simon.grid(column=0,row=0)


root.mainloop()
