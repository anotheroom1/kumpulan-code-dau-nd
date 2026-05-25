import turtle
import math

#ini fungsi ambil tracer kemarin
globaln = 1
globaldelay=3
if hasattr(turtle, 'tracer'):
    set_tracer = turtle.tracer
    del turtle.tracer
else :
    self.set_tracer = None
def settracer(n, delay):
        global globaln, globaldelay
        globaln = n
        globaldelay = delay
        set_tracer(n, delay)
def gettracer():
        return globaln, globaldelay
def update():
        turtle.update()
#ini fungsi elips
class Turtle(turtle.Turtle):
    def elips(self, a, b, degrees=360, start_angle=0):#ambil sumbu horizontal, vertikal, sudut putaran dan sudut awal
    #ambil nilai tracer
        nval, dval = gettracer()
        settracer(0, 0)
        start_rad=math.radians(start_angle) #mengambil nilai rad dari sudut awal
        #dari sudut awal, kita tahu posisi awal, kedudukannya dengan titik pusat
        ox = a*math.cos(start_rad)
        oy = b*math.sin(start_rad)
      #atur speed jika 0 tercepat, jika lebih dari 10, nilainya 10
        speed1 = self.speed()
        if speed1 == 0: speed2 = 20
        elif speed1 >= 10: speed2 = 10
        else: speed2 = speed1 if speed1 > 0 else 1
        #atur posisi x y dan sudut head pen
        pos_x, pos_y = self.pos()
        head_pen = math.radians(self.heading())
        #Proses membuat oval nya
        '''Menggunakan nested loop untuk mengatur kecepatan menggambar oval, lebih tepatnya untuk mengatur kapan turtle.update nya dipanggil. 
        Perkalian dengan 4 sendiri dirasa cukup akurat untuk kecepatan. Ini dapat dari coba²
        Loop harus berjumlah 361 atau sudut yang diinginkan + 1. lalu dibagi menjadi dua loop. Itu sendiri aku tidak tau kenapa, coba²'''
        for i in range(int(degrees*4 // speed2)+1):
            for j in range(speed2):
                radian_elips = math.radians(start_angle+(i* speed2+j) / 4) #sudut awal + pergerakan
                if math.degrees(radian_elips) > degrees: break # berhenti kalau sudah satu putaran atau mencapai sudut yang diinginkan
                lx = a * math.cos(radian_elips) - ox
                ly = b * math.sin(radian_elips) -oy
                nx = pos_x + (lx * math.cos(head_pen) - ly * math.sin(head_pen))
                ny = pos_y + (lx * math.sin(head_pen) + ly * math.cos(head_pen))
                self.goto(nx, ny)
            if (nval != 0 or dval != 0):
                update()#jika tracer 0, tidak diupdate
        settracer(nval, dval)#kembalikan nilai awal tracer
        
        
a= Turtle()

a.penup()
a.forward(250)
a.pendown()

a.elips(250,50)
a.penup()
a.left(90)
a.forward(100)
a.right(90)
a.pendown()
a.speed(10)
a.elips(250,50)
a.penup()
a.left(90)
a.forward(100)
a.right(90)
a.pendown()
p,q = gettracer()
settracer(0,0)
a.elips(250,50)
a.penup()
a.left(90)
a.forward(100)
a.right(90)
a.pendown()
settracer(p,q)
a.elips(50,250)
settracer(0,0)
