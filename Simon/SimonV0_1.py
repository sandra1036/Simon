from tkinter import *
import numpy as np
from SimonV0Class import SimonClass
from tkinter import ttk

root=Tk()
f=ttk.Frame(root)
f.pack()
simon=SimonClass(f,width=500,height=500)
simon.grid(column=0,row=0)
root.mainloop()
