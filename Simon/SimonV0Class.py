from tkinter import *
from tkinter import ttk
import numpy as np
class SimonClass(Canvas):

    def xy(self,event):
        global lastx, lasty
        lastx, lasty = self.canvasx(event.x), self.canvasy(event.y)

    def homogenize(self,coords: list):
        for i in range(len(coords)):
            coords[i].append(1)

    def dehomogenize(self,coords: list):
        for i in range(len(coords)):
            coords[i][0] = coords[i][0] / coords[i][2]
            coords[i][1] = coords[i][1] / coords[i][2]
            del coords[i][2]

    def gettranslation(self,tx: float, ty: float) -> list:
        return [[1, 0, 0], [0, 1, 0], [tx, ty, 1]]

    def getrotation(self,deg: float) -> list:
        rad = np.radians(deg)
        return [[np.cos(rad), np.sin(rad), 0], [-np.sin(rad), np.cos(rad), 0], [0, 0, 1]]

    # Lo usa en una clase a parte donde lo llama desde ahi
    def getscaled(self, xscl: float, yscl: float) -> list:
        return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]

    def point(self,num:int):
        num=num+10
        self.pon.set(num)


    def defaul(self):
        self.pon.set(0)

    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.w0=500
        self.h0=500

        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.xscl = self.w / self.w0
        self.yscl = self.h / self.h0

        self.scale = self.getscaled(self.xscl, self.yscl)

        self.create_oval(150 - 140, 150 - 140, 350 + 140, 350 + 140, fill="lightgrey")
        self.create_oval(150 - 130, 150 - 130, 350 + 130, 350 + 130, fill="black")
        self.create_oval(150 - 10, 150 - 10, 350 + 10, 350 + 10, fill="lightgrey")

        point1 = [[126, 56], [30, 187], [30, 240], [120, 240], [120, 213], [165, 150], [177, 136], [210, 134],
                  [210, 55]]
        # point=[[-126,56],[-30,187],[-30,240],[-120,240],[-120,213],[-165,150],[-177,136],[-210,134],[-210,55],[-126,56]]

        self.homogenize(point1)

        to = self.gettranslation(-250, -250)
        t = np.dot(point1, to).tolist()

        color = ["green", "blue", "red", "yellow"]
        colorlight=["lightgreen","lightblue","pink","lightyellow"]
        cont = 0
        self.dehomogenize(t)
        self.create_polygon(t, fill="green")
        print(t)
        self.homogenize(t)
        for rot in range(0, 360, 90):
            tras = self.gettranslation(250, 250)
            rotation = self.getrotation(rot)
            transform = np.dot(rotation, tras).tolist()
            temp = list()
            for i in range(len(point1)):
                temp.append(np.dot(t[i], transform).tolist())

            self.dehomogenize(temp)

            idf=self.create_polygon(temp, fill=color[cont], width=4,activefill=colorlight[cont])
            self.tag_bind(idf, "<Enter>", lambda e: self.point(int(self.pon.get())))
            cont += 1

        self.create_oval(170 - 2, 260 - 2, 200 + 2, 290 + 2, fill="black")
        idc=self.create_oval(170, 260, 200, 290, fill="yellow")
        self.tag_bind(idc,"<Button-1>",lambda e:self.defaul())
        self.create_text(185, 250, fill="black", font="Arial 8 bold", text="new")
        self.create_oval(230 - 2, 260 - 2, 260 + 2, 290 + 2, fill="black")
        self.create_text(248, 250, fill="black", font="Arial 8 bold", text="prefs")
        self.create_oval(230, 260, 260, 290, fill="red")
        self.create_oval(290 - 2, 260 - 2, 320 + 2, 290 + 2, fill="black")
        self.create_text(310, 250, fill="black", font="Arial 8 bold", text="scores")
        self.create_oval(290, 260, 320, 290, fill="green")
        self.create_text(250, 190, fill="black", font="Arial 20 bold", text="SIMÓN")


        temp = [[250, 320]]
        self.pon=IntVar()
        self.pon.set(0)
        cont=10
        label=Label(master,textvariable=self.pon,width=5,background="black",foreground="red",anchor ="e")
        self.homogenize(temp)
        needle = np.dot(temp, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_window(needle,window=label)


        self.bind("<Button-1>", lambda e:print(e.x,e.y))
