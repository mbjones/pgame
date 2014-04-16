# Quick reference sheet

## Saving your work.

We save our work in Google Drive.

### To get your file

- Log in to Google drive (http://drive.google.com)
    - Username: jccspython
    - Password: check with instructor
- Open the 'python-class/2014-trimester-3' folder
- Drag the 'matt-start.py' file (or one with your name) to your computer

### To edit your file
- Open it on your local computer using 'TextEdit' application
- Make changes
- Save file

### To save your file to Google Drive
- Open your local working folder
- Drag your file to the Google Drive '2014-trimester-3' folder

## Launch python
- We are using ipython as our language, launch it by:
    - Open the 'Terminal' application
    - Type `ipython` and press return
    - This should bring you to the ipython command prompt

## Python Turtle commands
```python
import turtle
jane = turtle.Turtle()
jane.left(90)
jane.forward(100)
jane.right(90)
jane.color('red')
jane.forward(100)
jane.penup()
jane.goto(-200, 200)
jane.pendown()
jane.forward(100)
```

## Loading and running code
- To run code in ipython from your text editor (TextEdit)
- Copy and paste the code by:
    - Copy the code to be run from TextEdit
    - At the ipython prompt, type `%paste`, which will paste the code in and run it
    - If you do not get the command prompt back, hit `return` to run the code
- Or, you can load code from a file
    - Be sure to start ipython from the directory in which you have the code (can be your home directory)
    - Load the code into python using:
        - `%load filename.py` where filename.py is the name of the file containing python commands to load
        - you may have to hit return to execute the last line of the file

## Functions
- Draw a square; notice that you have to issue the same commands 4 times?
- Functions are used to create a block of code you want to use more than once
- Here is a function for adding two numbers together:

```python
def add(x, y):
    sum = x + y
    return sum
```
- Once you define a function, you call it like any other python function.  E.g., `mysum = add(5, 6)`
- Can you make a function that returns the product of the numbers?
    - Hint: you need to indent using the same characters for it to work (for example, four spaces, or one tab)
- How about the quotient?

- Activities
    - Write a function that draws a line between two points using the turtle.goto(x, y) command
    - Write a function that draws a square at point (x,y) with a given side length of `size`

## Loops
- Often you want to run the same code multiple times.  You can use a `for` loop to accomplish this:

```python
import turtle
for x in range(75):
    turtle.forward(x)
    turtle.left(x)
```
- Activities
    - Write a loop that draws a square with a turtle
    - Write a square function from above using a loop (hint: there will be two steps in the loop)
    - Can you write other functions to draw various shapes?

```python
def square(x):
    t = turtle.Turtle()
    for i in range(4):
        t.forward(x)
        t.left(90)
```

