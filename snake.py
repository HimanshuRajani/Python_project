import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

#setup screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0) #turns off the svreen updates

#snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("circle")
snake_head.color("while")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = "stop"

#snake food

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.penup()
food.goto(0,100)

segments = []

#pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)

pen.write("score::0 high_score::0", align="center", font=("courier", 24, "normal"))

#functions

def go_up():
    if snake_head.direction != "down":
        snake_head.direction="up"

def go_down():
    if snake_head.direction!="up":
        snake_head.direction="down"

def go_right():
    if snake_head.direction!="left":
        snake_head.direction="right"

def go_left():
    if snake_head.direction!="right":
        snake_head.direction="left"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.set(y+20)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.set(y-20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.set(x+20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.set(x-20)

#keyboard button setup


wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#main game loop
while True:
    wn.update()

    #check collision with border
    if snake_head.xcor()>290 or snake_head.xcor()<=290 or snake_head.ycor()>290 or snake_head.ycor()<=290:
        time.sleep(1)
        snake_head.goto(0,0)
        snake_head.direction = "stop"

    #hide segments

    for segment in segments:
        segment.got(1000,1000)

    #clear the segment list

    segment.clear()

    #reset the score
    score = 0

    #reset the delay

    delay = 0.1

    pen.clear()
    pen.write("Score : high score:{}".format{score, high_score}, align="center", font=("courier", 24, "normal"))

