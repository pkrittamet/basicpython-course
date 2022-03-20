import turtle
tao = turtle.Pen()
tao.shape('turtle')
def tri():
    for i in range(3):
        tao.forward(100)
        tao.left(120)
        

def box():
    for i in range(4):
        tao.forward(100)
        tao.left(90)


def hexagonal():
    tao.left(30)
    for i in range(6):
        tao.forward(100)
        tao.left(60)


def octagon():
    for i in range(8):
        tao.forward(75)
        tao.left(45)


def cir():
    for i in range(10):
        tao.circle(35)
        tao.left(36)


def go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


go(200,200)
tri()
go(-200,200)
box()
go(-200,-200)
hexagonal()
go(200,-200)
octagon()
go(0,0)
cir()



