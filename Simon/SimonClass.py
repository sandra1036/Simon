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
        num=0




    def __init__(self, master=None, **options):
        super().__init__(master, options)
        self.w0=500
        self.h0=500

        self.w = int(self.cget('width'))
        self.h = int(self.cget('height'))

        self.xscl = self.w / self.w0
        self.yscl = self.h / self.h0

        self.scale = self.getscaled(self.xscl, self.yscl)


        self.create_oval(150-140,150-140,350+140,350+140,fill="lightgrey")
        self.create_oval(150-130,150-130,350+130,350+130,fill="black")
        self.create_oval(150-10,150-10,350+10,350+10,fill="lightgrey")



        # point1=[[126,56],[30,187],[30,240],[120,240],[120,213],[165,150],[177,136],[210,134],[210,55]]
        # canvas.create_polygon(point1,fill="green")
        point=[[-126,56],[-30,187],[-30,240],[-120,240],[-120,213],[-165,150],[-177,136],[-210,134],[-210,55],[-126,56]]

        self.homogenize(point)
        to=self.gettranslation(250,250)

        #color={"green":"#039E03","blue":"#0564BD","red":"#BD0B05","yellow":"#D8CC09"}
        color=["yellow","green","blue","red"]
        cont=0
        for rot in range(0,360,90):
            rotation =self.getrotation(rot)
            transform = np.dot(rotation, to)
            temp = list()
            for i in range(len(point)):
                temp.append(np.dot(point[i], transform).tolist())

            self.dehomogenize(temp)
            self.figu=self.create_polygon(temp, fill=color[cont], width=4)
            cont+=1



        self.create_oval(170-2,260-2,200+2,290+2,fill="black")
        self.create_oval(170,260,200,290,fill="yellow")
        # Yvar=IntVar()
        # labelY=ttk.Label(master,text="new",textvariable=Yvar)
        # labelY.pack()
        # self.create_window(temp,window=labelY)
        self.create_text(185,250,fill="black",font="Arial 8 bold",text="new")
        self.create_oval(230-2,260-2,260+2,290+2,fill="black")
        self.create_text(248,250,fill="black",font="Arial 8 bold",text="prefs")
        self.create_oval(230,260,260,290,fill="red")
        self.create_oval(290-2,260-2,320+2,290+2,fill="black")
        self.create_text(310,250,fill="black",font="Arial 8 bold",text="scores")
        self.create_oval(290,260,320,290,fill="green")
        self.create_text(250,190,fill="black",font="Arial 20 bold",text="SIMÓN")

        # style=ttk.Style()
        # style.map('MyEntry.TEntry',
        #       background=[('disabled', '#d9d9d9'), ('active', '#ececec')],
        #       foreground=[('disabled', '#a3a3a3'), ('active', '#0000cc')],
        #       relief=[('active', '!disabled', 'sunken')])
        # style.configure('MyEntry.TEntry', font="Arial 57")
        temp = [[250, 320]]
        pon=IntVar()
        cont=10
        entry=ttk.Entry(master,textvariable=pon)
        entry.bind("<Return>", lambda e:print(cont))
        self.create_window(temp,window=entry)





        self.bind("<Button-1>", lambda e:print(e.x,e.y))
