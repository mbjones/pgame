# coding: utf-8
def drawboard():
    import turtle
    grid = turtle.Turtle()
    #s = grid.getscreen()
    #s.clearscreen()
    grid.color('red')
    line(grid, -300, 100, 300,  100)
    line(grid, -300,-100, 300, -100)
    line(grid, -100, 300,-100, -300)
    line(grid,  100, 300, 100, -300)
    
def cs():
    t = turtle.Turtle()
    s = t.getscreen()
    s.clearscreen()
    
def line(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    
