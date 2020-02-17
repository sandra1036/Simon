from tkinter import *
import numpy as np

class Simon(Canvas):

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

    def getscaled(self, xscl: float, yscl: float) -> list:
        return [[xscl, 0, 0], [0, yscl, 0], [0, 0, 1]]


    def point(self, num: int):
        num = num + 10
        self.labelvar.set(num)

    def defaul(self):
        self.labelvar.set(0)

    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.w0=500
        self.h0=500

        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.xscl = self.w / self.w0
        self.yscl = self.h / self.h0

        self.scale = self.getscaled(self.xscl, self.yscl)

        point = [[5, 5], [345, 345]]
        self.homogenize(point)
        sc=np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_oval(sc, fill="grey")

        point = [[10, 10], [340, 340]]
        self.homogenize(point)
        sc = np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_oval(sc, fill="black")

        point = [[110, 110], [240, 240]]
        self.homogenize(point)
        sc = np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_oval(sc, fill="silver")

        point = [[165, 180], [185, 200]]
        self.homogenize(point)
        sc = np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_oval(sc, fill="black")

        point = [[167, 182], [183, 198]]
        self.homogenize(point)
        sc = np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        idp = self.create_oval(sc, fill="red")
        self.tag_bind(idp, "<Button-1>", lambda e: self.defaul())

        point = [[130, 180], [150, 200]]
        self.homogenize(point)
        sc = np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_oval(sc, fill="black")

        point = [[132, 182], [148, 198]]
        self.homogenize(point)
        sc = np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_oval(sc, fill="yellow")

        point = [[200, 180], [220, 200]]
        self.homogenize(point)
        sc = np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_oval(sc, fill="black")

        point = [[202, 182], [218, 198]]
        self.homogenize(point)
        sc = np.dot(point, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_oval(sc, fill="cyan")

        pointt = [[175, 150]]
        self.homogenize(pointt)
        sc = np.dot(pointt, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_text(sc, font="Arial 23 bold", text="SIMÓN")

        pointt = [[175, 175]]
        self.homogenize(pointt)
        sc = np.dot(pointt, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_text(sc, font="Arial 7 bold", text="prefs")

        pointt = [[140, 175]]
        self.homogenize(pointt)
        sc = np.dot(pointt, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_text(sc, font="Arial 7 bold", text="new")

        pointt = [[210, 175]]
        self.homogenize(pointt)
        sc = np.dot(pointt, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_text(sc, font="Arial 7 bold", text="scores")

        pointpol = [[-70, -10], [-150, -10], [-150, -60], [-60, -150], [-10, -150], [-10, -70], [-30, -70], [-70, -30]]
        colors = (('green4', 'green3'), ('cyan4', 'cyan3'), ('red4', 'red3'), ('yellow4', 'yellow3'))
        self.homogenize(pointpol)
        tras = self.gettranslation(175, 175)
        cont = 0
        for rot in range(0, 360, 90):
            rotation = self.getrotation(rot)
            trasform = np.dot(rotation, tras).tolist()
            trasform=np.dot(trasform, self.scale).tolist()
            temp = list()
            for i in range(len(pointpol)):
                temp.append(np.dot(pointpol[i], trasform).tolist())

            self.dehomogenize(temp)

            id = self.create_polygon(temp, fill=colors[cont][0], activefill=colors[cont][1], width=4)
            self.tag_bind(id, "<Enter>", lambda e: self.point(int(self.labelvar.get())))
            cont = cont + 1

        window = [[175, 220]]
        self.labelvar = IntVar()
        self.labelvar.set(0)
        label = Label(self, relief='groove', background='black', foreground='red', anchor='e', textvariable=self.labelvar)
        self.homogenize(window)
        sc = np.dot(window, self.scale).tolist()
        self.dehomogenize(sc)
        self.create_window(sc, width=60, height=20, window=label)



