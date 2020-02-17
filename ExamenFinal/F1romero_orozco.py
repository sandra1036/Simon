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

def pointm(num:int):
    num=num+10
    labelvar.set(num)

def defaul():
    labelvar.set(0)

root=Tk()
canvas=Canvas(root,width=350,height=350)
canvas.pack()

point=[[5, 5], [345, 345]]
canvas.create_oval(point,fill="grey")

point=[[10, 10], [340, 340]]
canvas.create_oval(point,fill="black")

point=[[110, 110], [240, 240]]
canvas.create_oval(point,fill="silver")

point=[[165, 180], [185, 200]]
canvas.create_oval(point,fill="black")

point=[[167, 182], [183, 198]]
idp=canvas.create_oval(point,fill="red")
canvas.tag_bind(idp,"<Button-1>",lambda e: defaul())

point=[[130, 180], [150, 200]]
canvas.create_oval(point,fill="black")

point=[[132, 182], [148, 198]]
canvas.create_oval(point,fill="yellow")

point=[[200, 180], [220, 200]]
canvas.create_oval(point,fill="black")

point=[[202, 182], [218, 198]]
canvas.create_oval(point,fill="cyan")

pointt=[[175, 150]]
canvas.create_text(pointt,font="Arial 23 bold",text="SIMÓN")

pointt=[[175, 175]]
canvas.create_text(pointt,font="Arial 7 bold",text="prefs")

pointt=[[140, 175]]
canvas.create_text(pointt,font="Arial 7 bold",text="new")

pointt=[[210, 175]]
canvas.create_text(pointt,font="Arial 7 bold",text="scores")

pointpol=[[-70, -10], [-150, -10], [-150, -60], [-60, -150], [-10, -150], [-10, -70], [-30, -70], [-70, -30]]
colors=(('green4', 'green3'), ('cyan4', 'cyan3'), ('red4', 'red3'), ('yellow4', 'yellow3'))
homogenize(pointpol)
tras = gettranslation(175, 175)
cont=0
for rot in range(0,360,90):

    rotation =getrotation(rot)
    transform = np.dot(rotation, tras).tolist()
    temp = list()
    for i in range(len(pointpol)):
        temp.append(np.dot(pointpol[i], transform).tolist())

    dehomogenize(temp)

    id=canvas.create_polygon(temp, fill=colors[cont][0],activefill=colors[cont][1], width=4)
    canvas.tag_bind(id,"<Enter>", lambda e: pointm((labelvar.get())))
    cont=cont+1

window= [[175, 220]]
labelvar=IntVar()
labelvar.set(0)
label=Label(canvas,relief='groove', background='black', foreground='red', anchor='e',textvariable=labelvar)
canvas.create_window(window,width=60, height=20,window=label)





root.mainloop()