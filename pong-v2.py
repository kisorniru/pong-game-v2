# Simple Pong game in Python 3 for beginners
# By @kisorniru
# Part 1: Getting Started

import turtle
import os

wn = turtle.Screen()
wn.title("Pong v2 by @kisorniru")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score = 0

# Paddle Info
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=10)
paddle.penup()
paddle.goto(0, -250)

# Ball Info
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = -.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.write("Player : 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_right():
    x = paddle.xcor()
    x += 20
    paddle.setx(x)


def paddle_left():
    x = paddle.xcor()
    x -= 20
    paddle.setx(x)


# Keyboard listen
wn.listen()
wn.onkeypress(paddle_right, "Right")
wn.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    wn.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle boundary checking
    if paddle.xcor() > 290:
        x = -290
        paddle.setx(x)

    if paddle.xcor() < -290:
        x = 290
        paddle.setx(x)

    # Ball boundary checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay sound/finish.wav&")

    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    # Paddle and Ball Collisions
    if (-240 > ball.ycor() > -250) and (paddle.xcor() + 100 > ball.xcor() > paddle.xcor() - 100):
        ball.sety(-240)
        ball.dy *= -1
        os.system("aplay sound/bounce.wav&")
        score += 1
        pen.clear()
        pen.write("Player : {}".format(score), align="center", font=("Courier", 24, "normal"))