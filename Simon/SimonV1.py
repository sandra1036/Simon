from tkinter import ttk
from tkinter import *
import numpy as np

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)


def homogenize(coords: list):
    for i in range(len(coords)):
        coords[i].append(1)


def dehomogenize(coords: list):
    for i in range(len(coords)):
        coords[i][0] = coords[i][0] / coords[i][2]
        coords[i][1] = coords[i][1] / coords[i][2]
        del coords[i][2]

def gettranslation(tx:float, ty:float)->list:
    return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

def getrotation(deg:float)->list:
    rad = np.radians(deg)
    return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]

#Lo usa en una clase a parte donde lo llama desde ahi
def getscaled(self, xscl:float, yscl:float) -> list:
    return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]






root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack()
canvas.create_oval(150-140,150-140,350+140,350+140,fill="lightgrey")
canvas.create_oval(150-130,150-130,350+130,350+130,fill="black")
canvas.create_oval(150-10,150-10,350+10,350+10,fill="lightgrey")
point=[[126,56],[30,187],[30,240],[120,240],[120,213],[165,150],[177,136],[210,134],[210,55]]
canvas.create_polygon(point,fill="green")
canvas.create_oval(170-2,260-2,200+2,290+2,fill="black")
canvas.create_oval(170,260,200,290,fill="yellow")
canvas.create_text(250,190,fill="black",font="Arial 20 bold",text="SIMÓN")





canvas.bind("<Button-1>", lambda e:print(e.x,e.y))

root.mainloop()