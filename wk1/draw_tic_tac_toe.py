# Drawing functions for tic-tac-toe
# Matt Jones 2013

import turtle

def drawboard():
    t = turtle.Turtle()
    t.pensize(5)
    t.color('red')
    t.clear()
    t.penup()
    t.goto(100,300)
    t.pendown()
    t.goto(100,-300)
    t.penup()
    t.goto(-100,-300)
    t.pendown()
    t.goto(-100,300)
    t.penup()
    t.goto(-300,100)
    t.pendown()
    t.goto(300,100)
    t.penup()
    t.goto(300,-100)
    t.pendown()
    t.goto(-300,-100)
    return(t);

def gotocell(t, cellx, celly):
    t.penup()
    originx = -235
    originy = 140
    newx = originx + ((cellx-1)*200)
    newy = originy - ((celly-1)*200)
    t.goto(newx,newy)
    t.pendown()

def marktic(t, letter):
    t.write(letter, font=('Arial', 96, 'normal'))

def main():
    t = drawboard()
    gotocell(t,1,1)
    marktic(t, 'X')
    gotocell(t,2,2)
    marktic(t, 'O')
    gotocell(t,3,3)
    marktic(t, 'X')

    moves = [[0]*3 for x in xrange(3)]
    turtle.mainloop()
    
if __name__ == '__main__':
    msg = main()
    
