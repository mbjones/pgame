# Drawing functions for tic-tac-toe
# Matt Jones 2013

import turtle

def drawgrid():
	t = turtle.Turtle()
	t.clear()
	s = t.getscreen()
	delay = s.delay()
	tracer = s.tracer()
	s.delay(0)
	s.tracer(0)
	t.speed(0)
	for x in range(-400,410,10):
		t.penup()
		t.goto(x,400)
		t.pendown()
		if (x % 100 == 0):
			t.pensize(3)
		else:
			t.pensize(1)
		if (x == 0):
			t.pencolor('red')
		else:
			t.pencolor('black')
		t.goto(x,-400)
	for y in range(400,-410,-10):
		t.penup()
		t.goto(-400,y)
		t.pendown()
		if (y % 100 == 0):
			t.pensize(4)
		else:
			t.pensize(1)
		if (y == 0):
			t.pencolor('red')
		else:
			t.pencolor('black')
		t.goto(400,y)
	labelaxes(t)
	s.tracer(tracer)
	s.delay(delay)
	t.speed(3)
	return(t)

def labelaxes(t):
	t.penup()
	t.goto(0, 410)
	t.write('0')
	t.goto(-410, 410)
	t.write('-400, 400')
	t.goto(410, 410)
	t.write('400, 400')
	t.goto(410, -410)
	t.write('400, -400')
	t.goto(-410, -410)
	t.write('-400, -400')
	t.goto(-410, 0)
	t.write('0')

