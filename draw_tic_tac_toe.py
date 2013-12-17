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
        if moves[row-1][col-1] == 0:
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
    ctotals = map(sum,zip(*moves))
    rtotals = [ sum(x) for x in moves ]
    diags = [moves[0][0] + moves[1][1] + moves[2][2],
        moves[0][2] + moves[1][1] + moves[2][0]]
    for totals in [ctotals, rtotals, diags]:
        for x in totals:
            if (x == 3):
                announceWin("X")
            elif (x == 12):
                announceWin("O") 
                
def announceWin(who):
    t = turtle.Turtle()
    t.color('red')
    t.up()
    t.goto(-150, 290)
    t.down()
    t.write(who+" Wins!", font=('Arial', 96, 'normal'))
      
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
    
def q():
    turtle.bye()

def newGame():
    main()
        
def main():
    global xTurn
    xTurn = True
    global moves
    moves = [[0]*3 for x in xrange(3)]
    cs()
    t = drawboard()

    win = turtle.Screen()
    win.onclick(processClick)
    win.onkey(q, "q")
    win.onkey(newGame, "n")
    win.listen()

    turtle.mainloop()
    
if __name__ == '__main__':
    msg = main()
    
