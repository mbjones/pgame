# Drawing functions for tic-tac-toe
# Matt Jones 2013

import turtle

def drawgrid():
    """Draw a 400x400 grid on the screen, label axes, and return the Turtle used to draw the grid."""

    turtle.setup(width=900, height=900, startx=0, starty=0)
    t = turtle.Turtle()
    s = t.getscreen()
    s.clearscreen()
    #s.screensize(420,420)
    t.hideturtle()
    t.clear()
    delay = s.delay()
    tracer = s.tracer()
    s.delay(0)
    s.tracer(0)
    t.speed(0)
    maxc = 400
    for x in range(-1*maxc,maxc+10,10):
        t.penup()
        t.goto(x,maxc)
        t.pendown()
        if (x % 100 == 0):
            t.pensize(3)
        else:
            t.pensize(1)
        if (x == 0):
            t.pencolor('red')
        else:
            t.pencolor('black')
        t.goto(x,-1*maxc)
    for y in range(maxc,-1*maxc-10,-10):
        t.penup()
        t.goto(-1*maxc,y)
        t.pendown()
        if (y % 100 == 0):
            t.pensize(4)
        else:
            t.pensize(1)
        if (y == 0):
            t.pencolor('red')
        else:
            t.pencolor('black')
        t.goto(maxc,y)
    labelaxes(t, maxc)
    s.tracer(tracer)
    s.delay(delay)
    t.speed(3)
    return(t)

def labelaxes(t, maxc):
    t.penup()
    t.goto(0, maxc+10)
    t.write('0')
    t.goto(-1*maxc-10, maxc+10)
    t.write('-400, 400')
    t.goto(maxc+10, maxc+10)
    t.write('400, 400')
    t.goto(maxc+10, -1*maxc-10)
    t.write('400, -400')
    t.goto(-1*maxc-10, -1*maxc-10)
    t.write('-400, -400')
    t.goto(-1*maxc-10, 0)
    t.write('0')

def line(x1, y1, x2, y2):
    """Draw a line on the screen between the two given points"""
    t = turtle.Turtle()
    s = t.getscreen()
    t.hideturtle()
    delay = s.delay()
    tracer = s.tracer()
    s.delay(0)
    s.tracer(0)
    t.speed(0)
    t.color('blue')
    t.pensize(5)
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
    s.delay(delay)
    s.tracer(tracer)

def tri(x1, y1, x2, y2, x3, y3):
    """Draw a triangle on the screen between the given points"""
    t = turtle.Turtle()
    s = t.getscreen()
    t.hideturtle()
    delay = s.delay()
    tracer = s.tracer()
    #s.delay(0)
    #s.tracer(0)
    #t.speed(0)
    t.color('darkgreen')
    t.pensize(5)
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
    t.goto(x3,y3)
    t.goto(x1,y1)
    s.delay(delay)
    s.tracer(tracer)

def rect(x1, y1, x2, y2):
    """Draw a rectange on the screen between the two given points"""
    t = turtle.Turtle()
    s = t.getscreen()
    t.hideturtle()
    delay = s.delay()
    tracer = s.tracer()
    #s.delay(0)
    #s.tracer(0)
    #t.speed(0)
    t.color('purple')
    t.pensize(5)
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y1)
    t.goto(x2,y2)
    t.goto(x1,y2)
    t.goto(x1,y1)
    s.delay(delay)
    s.tracer(tracer)
