import turtle

turtle.begin_fill()

turtle.color('black')

turtle.right(90)
turtle.forward(100)

turtle.right(90)
turtle.forward(100)

turtle.right(90)
turtle.forward(100)

turtle.right(90)
turtle.forward(100)

for i in range(4):
    turtle.right(90)
    turtle.forward(100)

turtle.clear()

for i in range(25):
    turtle.right(20)
    turtle.forward(15)

    
turtle.clear()

for i in range(80):
    turtle.right(15)
    turtle.forward(10+i)
    
turtle.clear()

turtle.circle(25)

colors = ['green','orange','yellow']
num = 100
n_color = 0

for i in range(400):
    turtle.right(90)
    turtle.forward(num - i)
    if n_color != len(colors) - 1:
        n_color += 1
    else:
        n_color = 0

        turtle.clear()

for i in range(400):
    turtle.color(colors[n_color])
    turtle.forward(num)
    if n_color != len(colors) - 1:
        n_color += 1
    else:
        n_color = 0
    num -= i