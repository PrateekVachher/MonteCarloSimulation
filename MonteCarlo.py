import turtle

def mark_point(x,y,col):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(5, col)
turtle.showturtle()
turtle.penup()
turtle.goto(-250,-250)
turtle.pendown()
sidelength = 500
turtle.forward(sidelength)
turtle.left(90)
turtle.forward(sidelength)
turtle.left(90)
turtle.forward(sidelength)
turtle.left(90)
turtle.forward(sidelength)
turtle.left(90)
turtle.forward(sidelength/2)
turtle.circle(250)
turtle.left(90)
turtle.forward(530)
turtle.backward(530+30)
turtle.forward(280)
turtle.left(90)
turtle.forward(530/2)
turtle.backward(530+30)
turtle.speed(1000)


def pytha_dist(x,y):
    import math
    # d**2 = x*2 + Y ** 2
    a = x**2
    b = y**2
    c = math.sqrt(a+b)
    return c

times = 1000
g = 0
r = 0
for m in range(times):
    import random
    x = random.randint(-250,250)
    y = random.randint(-250,250)


    if pytha_dist(x,y) <= 250:
        col = 'green'
        g += 1

    else:
        col = 'red'
        r += 1

    mark_point(x,y,col)
    print (x,y,pytha_dist(x,y),col)

print (g)
print (times)
print ('Pi: ', float(g)/(times)*4)
input()