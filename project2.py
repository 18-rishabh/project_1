from turtle import * # importing whole turtle module
from random import randrange # importing random
from freegames import square, vector #importing freegames
amul=Turtle()

target = vector(0, 0) #this is
snake = [vector(10, 0)]
pointer = vector(0, -10)

wn=Screen() # this is for background color
wn.bgcolor('blue') # background in blue color

def func_1(x, y): #parameters are 2 since its a 2-D game

    pointer.x = x # represents x axis
    pointer.y = y # represents y axis

def func_2(part): #boundary values. End values are essential for defining square.

    return -200 < part.x < 190 and -200 < part.y < 190 # when snake crosses boundary values it is a foul.

def move(): # movement is given to snake, it only moves in forward direction

    part= snake[-1].copy()
    part.move(pointer)
    if not func_2(part) or part in snake:
        square(part.x, part.y, 9, 'red')
        update()
        return
    snake.append(part)
    if part== target: # for counting
        print('Snake:', len(snake))
        target.x = randrange(-15, 15) * 10
        target.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    clear()
    for i in snake: # snake element-combination of squares.
        square(i.x, i.y, 9, 'black')
        square(target.x, target.y, 9, 'violet')
    update() # to update all the steps.
    ontimer(move, 100)

hideturtle()# to hide the turtle(arrow)
tracer(False) # brings back elements to initial state
listen()# countinously updates game
onkey(lambda: func_1(10, 0), 'Right') # controls are given
onkey(lambda: func_1(-10, 0), 'Left')
onkey(lambda: func_1(0, 10), 'Up')
onkey(lambda: func_1(0, -10), 'Down')
move() # calling function
done() # for holding screen
