# Tic-tac-toe, a simplistic implementation
# Depends on python turtle
# Matt Jones 2013

import turtle
    
def drawboard():
    t = turtle.Turtle()
    t.pensize(5)
    t.color('red')
    line(t, -300, 100, 300,  100)
    line(t, -300,-100, 300, -100)
    line(t, -100, 300,-100, -300)
    line(t,  100, 300, 100, -300)
    return(t);

def cs():
    t = turtle.Turtle()
    s = t.getscreen()
    s.clearscreen()
    
def line(t, x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    
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

def processClick(x, y):
    global xTurn
    cell = whichCell(x, y)
    if (cell > 0):
        t = turtle.Turtle()
        t.hideturtle()
        col = (cell-1) % 3 + 1
        row = (cell - ((cell-1) % 3) - 1)/3 + 1
        gotocell(t, col, row)
        if (xTurn):
            moves[row-1][col-1] = 1
            marktic(t, 'X')
            xTurn = False
        else:
            moves[row-1][col-1] = 4
            marktic(t, 'O')
            xTurn = True
    checkWin(moves)
    
def checkWin(moves):
    # Now test if we've hit three in a row 
    # TODO: Check diagonal sums too    
    ctotals = map(sum,zip(*moves))
    rtotals = [ sum(x) for x in moves ]
    #for totals in [ctotals, rtotals]:
    for x in ctotals:
        if (x == 3):
            print("X Wins")
        elif (x == 12):
            print("O Wins")
    for x in rtotals:
        if (x == 3):
            print("X Wins")
        elif (x == 12):
            print("O Wins")
    
def whichCell(x, y):
    col = -10;
    row = -10;
    if (-300 < x < -100):
        col = 1
    elif (-100 < x < 100):
        col = 2
    elif (100 < x < 300):
        col = 3
    
    if (-300 < y < -100):
        row = 6
    elif (-100 < y < 100):
        row = 3
    elif (100 < y < 300):
        row = 0
    
    cell = row + col
    return(cell)
    
def quit():
    turtle.bye()
    
def main():
    global xTurn
    xTurn = True
    global moves
    moves = [[0]*3 for x in xrange(3)]
    
    win = turtle.Screen()
    t = drawboard()
    win.onclick(processClick)
    win.onkey(quit, "q")
    win.listen()

    turtle.mainloop()
    
if __name__ == '__main__':
    msg = main()
    
