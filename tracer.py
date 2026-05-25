import turtle
globaln = 1
globaldelay=3
if hasattr(turtle, 'tracer'):
    set_tracer = turtle.tracer
    del turtle.tracer
#menghapus perintah tracer asli
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
        
        
t = turtle.Turtle()
t.speed(1)
t.forward(200)
a, b = gettracer()
t.left(90)
settracer(0, 0)
t.forward(200)
update()
settracer(a,b)
t.left(90)
t.forward(200)
