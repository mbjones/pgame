# Checkers, a simplistic implementation
# Depends on python turtle
# Matt Jones 2013

import turtle
    
def line(t, x1, y1, x2, y2):
    '''Draw a line from x1,y1 to x2,y2.'''
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)

def square(t, x1, y1, size, color):
    '''Draw a square filled with the provided color.'''
    t.penup()
    t.goto(x1, y1)
    t.color(color)
    t.fillcolor(color)
    t.pendown()
    t.fill(True)
    for x in range(4):
        t.forward(size)
        t.left(90)
    t.fill(False)

def flipcolor(color):
    '''Swap the color from black to red, or vice versa.'''
    if (color=="black"):
        color='red'
    else:
        color='black'
    return(color)

def drawboard():
    '''Draw the Checkers grid with a size of 80 units.'''
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    s = t.getscreen()
    delay = s.delay()
    tracer = s.tracer()
    #s.delay(0)
    #s.tracer(0)
    t.pensize(1)
    color='black'
    size = 80
    x = -400
    y = -300
    for i in range(0, size*8, size):
        for j in range(0, size*8, size):
            x += size
            square(t, x, y, size, color)
            color = flipcolor(color)
        x = -400
        y += size
        color = flipcolor(color)

def drawchecker(t, cellx, celly, color):
    t.color(color)
    t.penup()
    t.goto(cellx, celly)
    t.fill(True)
    t.circle(30)
    t.fill(False)
    
def startposition():
    t = turtle.Turtle()
    t.getscreen().reset()
    drawboard()
    t.hideturtle()
    t.speed(0)
    y = -290
    for cellx in range(1, 9, 2):
        x = -280 + 80*(cellx-1)
        drawchecker(t, x, y, 'grey')
    y = -210
    for cellx in range(2, 9, 2):
        x = -280 + 80*(cellx-1)
        drawchecker(t, x, y, 'grey')
    y = -130
    for cellx in range(1, 9, 2):
        x = -280 + 80*(cellx-1)
        drawchecker(t, x, y, 'grey')
    y = -130+240
    for cellx in range(2, 9, 2):
        x = -280 + 80*(cellx-1)
        drawchecker(t, x, y, 'red')
    y = -130+320
    for cellx in range(1, 9, 2):
        x = -280 + 80*(cellx-1)
        drawchecker(t, x, y, 'red')
    y = -130+400
    for cellx in range(2, 9, 2):
        x = -280 + 80*(cellx-1)
        drawchecker(t, x, y, 'red')

    #drawchecker(t, -280, -130, 'green')
    #drawchecker(t, -200, -210, 'green')
    
def cs():
    '''Clear the screen of all drawing.'''
    t = turtle.Turtle()
    s = t.getscreen()
    s.clearscreen()
    
def markletter(t, cellx, celly, letter):
    '''Position turtle in a given cell in location proper for writing an X or O. 
    The cells are indexed from 1 to 3 in both dimensions.'''
    t.penup()
    originx = -235
    originy = 140
    newx = originx + ((cellx-1)*200)
    newy = originy - ((celly-1)*200)
    t.goto(newx,newy)
    t.pendown()
    t.write(letter, font=('Arial', 96, 'normal'))
    
def processClick(x, y):
    '''Upon mouse click, determine which cell it is in, store the move, and draw it on the screen.'''
    global xTurn
    col = 0
    row = 0
    if (-300 < x < -100):
        col = 1
    elif (-100 < x < 100):
        col = 2
    elif (100 < x < 300):
        col = 3
    
    if (-300 < y < -100):
        row = 3
    elif (-100 < y < 100):
        row = 2
    elif (100 < y < 300):
        row = 1
        
    if ((col > 0) & (row > 0)):
        t = turtle.Turtle()
        t.hideturtle()
        if moves[row-1][col-1] == 0:
            if (xTurn):
                moves[row-1][col-1] = 1
                markletter(t, col, row, 'X')
                xTurn = False
            else:
                moves[row-1][col-1] = 4
                markletter(t, col, row, 'O')
                xTurn = True
            checkWin(moves)

def checkWin(moves):
    '''Check if we have any row, column, or diagonal with three in a row.'''
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
    '''Announce that X or O has won the game.'''
    t = turtle.Turtle()
    t.color('red')
    t.up()
    t.goto(-150, 290)
    t.down()
    t.write(who+" Wins!", font=('Arial', 96, 'normal'))
    
def q():
    '''Quit the program.'''
    turtle.bye()

def newGame():
    '''Reinitialize the program and start a new game.'''
    main()
        
def main():
    '''Reinitialize the program and start a new game.'''
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
    
#if __name__ == '__main__':
#    msg = main()
    
