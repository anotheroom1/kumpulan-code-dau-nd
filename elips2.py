import turtle
import math

#ini fungsi ambil tracer kemarin
globaln = 1
globaldelay=3
if hasattr(turtle, 'tracer'):
    set_tracer = turtle.tracer
    del turtle.tracer
else :
    set_tracer = None
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
    def elips(self, a, b, degrees=360, start_angle=0, steps=None):#tambahkan steps
        nval, dval = gettracer()
        target_degrees=degrees
        start_angle+=270
        degrees+=270
        #+270 digunakan agar menggambar dimulai dari bawah kayak circle
        settracer(0, 0)
        start_rad=math.radians(start_angle) 
        ox = a*math.cos(start_rad)
        oy = b*math.sin(start_rad)
      
        speed1 = self.speed()
        if speed1 == 0: speed2 = 500
        elif speed1 >= 10: speed2 = 10
        else: speed2 = speed1 if speed1 > 0 else 1
        pos_x, pos_y = self.pos()
        head_pen = math.radians(self.heading())
        for i in range(int(degrees*4 // speed2)+1):
            for j in range(speed2):
                # Sudut pergerakan 0.25 derajat per loop
                current_mv = (i*speed2+ j)/4
                if current_mv > target_degrees: break # berhenti kalau sudah satu putaran atau mencapai sudut yang diinginkan
                if steps is not None and steps>0:
                    #jika step didefinisikan/pergerakan memiliki sudut
                    stepsize = target_degrees/steps #jadi kalau 6 step, 60 derajat per step
                    #sekarang ada di segmen ke berapa
                    segment = current_mv // stepsize
                    # Tentukan sudut awal segmen dan sudut akhir segmen
                    startseg=segment*stepsize
                    endseg=(segment+1)*stepsize
                    #Hitung persentase posisi loop di dalam segmen ini
                    porsi = (current_mv-startseg)/stepsize
                    #Ambil koordinat elips asli di ujung sudut awal dan ujung sudut akhir
                    rad_start = math.radians(start_angle + startseg)
                    rad_end = math.radians(start_angle + endseg)
                    
                    lx_start = a * math.cos(rad_start) - ox
                    ly_start = b * math.sin(rad_start) - oy
                    lx_end = a * math.cos(rad_end) - ox
                    ly_end = b * math.sin(rad_end) - oy
                    # jalan lurus ke titik pos
                    lx = lx_start + (lx_end - lx_start) * porsi
                    ly = ly_start + (ly_end - ly_start) * porsi
                    #arah vektor =akhir-awal
                    vx = lx_end - lx_start
                    vy = ly_end - ly_start
                else:
                    # Jika steps None, jalan halus
                    radian_elips = math.radians(start_angle + current_mv)
                    lx = a * math.cos(radian_elips) - ox
                    ly = b * math.sin(radian_elips) - oy
                     # Rumus arah melengkung
                    vx = -a * math.sin(radian_elips)
                    vy = b * math.cos(radian_elips)
                nx = pos_x + (lx * math.cos(head_pen) - ly * math.sin(head_pen))
                ny = pos_y + (lx * math.sin(head_pen) + ly * math.cos(head_pen))
                self.goto(nx, ny)
                # Putar vektor kecepatan tersebut sesuai arah head_pen awal
                vx_rot = vx * math.cos(head_pen) - vy * math.sin(head_pen)
                vy_rot = vx * math.sin(head_pen) + vy * math.cos(head_pen)
                sudut_turunan = math.degrees(math.atan2(vy_rot, vx_rot))
                self.setheading(sudut_turunan)
            if (nval != 0 or dval != 0):
                update()#jika tracer 0, tidak diupdate
        settracer(nval, dval)#kembalikan nilai awal tracer
