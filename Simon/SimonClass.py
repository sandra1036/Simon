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

        ponint=[[150 - 140, 150 - 140],[350 + 140, 350 + 140]]
        self.homogenize(ponint)
        needle = np.dot(ponint, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_oval(needle,fill="lightgrey")

        ponint=[[150-130,150-130],[350+130,350+130]]
        self.homogenize(ponint)
        needle = np.dot(ponint, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_oval(needle,fill="black")


        ponint=[[150-10,150-10],[350+10,350+10]]
        self.homogenize(ponint)
        needle = np.dot(ponint, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_oval(needle,fill="lightgrey")



        point1=[[126,56],[30,187],[30,240],[120,240],[120,213],[165,150],[177,136],[210,134],[210,55]]
        self.homogenize(point1)
        needle = np.dot(point1, self.scale).tolist()
        self.dehomogenize(needle)
        idg=self.create_polygon(needle,fill="green",activefill="lightgreen")
        #point=[[-126,56],[-30,187],[-30,240],[-120,240],[-120,213],[-165,150],[-177,136],[-210,134],[-210,55],[-126,56]]
        self.tag_bind(idg,"<Enter>",lambda e: self.point(int(self.pon.get())))


        point2 = [[126, 56], [30, 187], [30, 240], [120, 240], [120, 213], [165, 150], [177, 136], [210, 134],[210, 55]]
        self.homogenize(point2)
        to=self.gettranslation(505,10)
        rotation = self.getrotation(90)
        transform = np.dot(rotation, to)
        needle = np.dot(point2, transform).tolist()
        needle = np.dot(needle, self.scale).tolist()
        self.dehomogenize(needle)
        idb=self.create_polygon(needle,fill="blue",activefill="lightblue")
        self.tag_bind(idb, "<Enter>", lambda e: self.point(int(self.pon.get())))

        point3 = [[126, 56], [30, 187], [30, 240], [120, 240], [120, 213], [165, 150], [177, 136], [210, 134],[210, 55]]
        self.homogenize(point3)
        to=self.gettranslation(500,500)
        rotation = self.getrotation(180)
        transform = np.dot(rotation, to)
        needle = np.dot(point3, transform).tolist()
        needle = np.dot(needle, self.scale).tolist()
        self.dehomogenize(needle)
        idr=self.create_polygon(needle,fill="red",activefill="pink")
        self.tag_bind(idr, "<Enter>", lambda e: self.point(int(self.pon.get())))

        point4 = [[126, 56], [30, 187], [30, 240], [120, 240], [120, 213], [165, 150], [177, 136], [210, 134],[210, 55]]
        self.homogenize(point4)
        to=self.gettranslation(0,500)
        rotation = self.getrotation(270)
        transform = np.dot(rotation, to)
        needle = np.dot(point4, transform).tolist()
        needle = np.dot(needle, self.scale).tolist()
        self.dehomogenize(needle)
        idy=self.create_polygon(needle,fill="yellow",activefill="lightyellow")
        self.tag_bind(idy, "<Enter>", lambda e: self.point(int(self.pon.get())))


        #color={"green":"#039E03","blue":"#0564BD","red":"#BD0B05","yellow":"#D8CC09"}
        # color=["yellow","green","blue","red"]
        # cont=0
        # for rot in range(0,360,90):
        #     rotation =self.getrotation(rot)
        #     transform = np.dot(rotation, to)
        #     temp = list()
        #     for i in range(len(point)):
        #         temp.append(np.dot(point[i], transform).tolist())
        #
        #     self.dehomogenize(temp)
        #     self.figu=self.create_polygon(temp, fill=color[cont], width=4)
        #     cont+=1
        #
        #
        point= [[170-2,260-2],[200+2,290+2]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_oval(needle,fill="black")

        point = [[170,260],[200,290]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        idc=self.create_oval(needle,fill="yellow")
        self.tag_bind(idc,"<Button-1>",lambda e:self.defaul())

        point=[[185,250]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_text(needle,fill="black",font="Arial 8 bold",text="new")

        point=[[230-2,260-2],[260+2,290+2]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_oval(needle,fill="black")

        point=[[248,250]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_text(needle,fill="black",font="Arial 8 bold",text="prefs")

        point=[[230,260],[260,290]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_oval(needle,fill="red")

        point=[[290-2,260-2],[320+2,290+2]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_oval(needle,fill="black")
        point=[[310,250]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_text(needle,fill="black",font="Arial 8 bold",text="scores")

        point=[[290,260],[320,290]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_oval(needle,fill="green")

        point=[[250,190]]
        self.homogenize(point)
        needle = np.dot(point, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_text(needle,fill="black",font="Arial 20 bold",text="SIMÓN")

        # style=ttk.Style()
        # style.map('MyEntry.TEntry',
        #       background=[('disabled', '#d9d9d9'), ('active', '#ececec')],
        #       foreground=[('disabled', '#a3a3a3'), ('active', '#0000cc')],
        #       relief=[('active', '!disabled', 'sunken')])
        # style.configure('MyEntry.TEntry', font="Arial 57")



        temp = [[250, 320]]
        self.pon=IntVar()
        self.pon.set(0)
        cont=10

        # entry=ttk.Entry(master,textvariable=pon)
        # entry.bind("<Return>", lambda e:print(cont))
        # self.create_window(temp,window=entry)

        label=Label(master,textvariable=self.pon,width=5,background="black",foreground="red",anchor ="e")
        self.homogenize(temp)
        needle = np.dot(temp, self.scale).tolist()
        self.dehomogenize(needle)
        self.create_window(needle,window=label)




        self.bind("<Button-1>", lambda e:print(e.x,e.y))
