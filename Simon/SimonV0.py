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



point1=[[126,56],[30,187],[30,240],[120,240],[120,213],[165,150],[177,136],[210,134],[210,55]]
#point=[[-126,56],[-30,187],[-30,240],[-120,240],[-120,213],[-165,150],[-177,136],[-210,134],[-210,55],[-126,56]]

homogenize(point1)

to=gettranslation(-250,-250)
t=np.dot(point1, to).tolist()

color=["green","blue","red","yellow"]
cont=0
dehomogenize(t)
canvas.create_polygon(t,fill="green")
print(t)
homogenize(t)
for rot in range(0,360,90):
    tras=gettranslation(250,250)
    rotation =getrotation(rot)
    transform = np.dot(rotation, tras).tolist()
    temp = list()
    for i in range(len(point1)):
        temp.append(np.dot(t[i], transform).tolist())

    dehomogenize(temp)

    canvas.create_polygon(temp, fill=color[cont], width=4)
    cont+=1



canvas.create_oval(170-2,260-2,200+2,290+2,fill="black")
canvas.create_oval(170,260,200,290,fill="yellow")
canvas.create_text(185,250,fill="black",font="Arial 8 bold",text="new")
canvas.create_oval(230-2,260-2,260+2,290+2,fill="black")
canvas.create_text(248,250,fill="black",font="Arial 8 bold",text="prefs")
canvas.create_oval(230,260,260,290,fill="red")
canvas.create_oval(290-2,260-2,320+2,290+2,fill="black")
canvas.create_text(310,250,fill="black",font="Arial 8 bold",text="scores")
canvas.create_oval(290,260,320,290,fill="green")
canvas.create_text(250,190,fill="black",font="Arial 20 bold",text="SIMÓN")
root.mainloop()
