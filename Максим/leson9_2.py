import turtle


winedow = turtle.Screen()
winedow.bgcolor('yellow')

ball = turtle.Turtle(shape='circle')
ball.y = 0

ball.up()
while True:
    ball.y = ball.y - 1
    ball.goto(0, ball.ycor()+ball.y)

    if ball.ycor() <= -300:
        ball.y = -ball.y
