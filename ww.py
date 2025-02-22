import turtle

t = turtle.Turtle()

t.speed(100)
screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')

t_ground = turtle.Turtle()
t_ground.penup()
t_ground.speed(0)
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.fillcolor('white')
t_ground.pencolor('white')
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)

t.hideturtle()


t.pencolor("green")


t.goto(0,150)
t.write("The circle next to the snowman is a snowball", font=("Arial", 20, "bold"), align="center")

t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,50)
t.pendown()
t.goto(-40,10)
t.goto(40,10)
t.goto(0,50)
t.end_fill()
t.penup()


t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,25)
t.pendown()
t.goto(-60,-25)
t.goto(60,-25)
t.goto(0,25)
t.end_fill()
t.penup()


t.fillcolor("green")
t.begin_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.goto(-80,-50)
t.goto(80,-50)
t.goto(0,0)
t.end_fill()
t.penup()


t.fillcolor("green")
t.begin_fill()
t.penup()

t.pencolor("black")




t.penup()
t.goto(0, -150)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()

# Middle circle
t.penup()
t.goto(0, -90)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

# Head circle
t.penup()
t.goto(0, -50)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-5, -40)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(2)
t.end_fill()
t.penup()
t.goto(5, -40)
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()

# Nose
t.penup()
t.goto(0, -45)
t.pendown()
t.fillcolor("orange")
t.begin_fill()
t.goto(10, -50)
t.goto(0, -50)
t.end_fill()

# Buttons
t.penup()
t.goto(0, -100)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(2)
t.end_fill()
t.penup()
t.goto(0, -115)
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()
t.penup()
t.goto(0, -130)
t.pendown()
t.begin_fill()
t.circle(2)
t.end_fill()


t.hideturtle()
t.penup()
t.goto(-50,-150)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.pensize(5)
t.begin_fill()
t.pencolor('red')
t.penup()
t.goto(100, 10)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.fillcolor('red')
t.end_fill()

t.pencolor('green')
t.penup()
t.goto(150, -100)
t.pendown()
t.forward(100)

t.shape("turtle")
t.speed(5)
t.pensize(3)

t.penup()
t.goto(-100, -100)
t.pendown()
t.pencolor("black")
t.begin_fill()

t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.fillcolor('Powder Blue')
t.end_fill()


t.penup()
t.goto(-300, -100)
t.pendown()
t.pencolor("navy")
t.begin_fill()

t.setheading(0)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.goto(-200, 50)
t.pendown()
t.pencolor('navy')
t.begin_fill()

t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

t.hideturtle()
t.penup()
t.goto(200,300)
t.pencolor('yellow')
t.pendown()

t.forward(100)
t.right(144)
t.forward(100)
t.right(144)
t.forward(100)
t.right(144)
t.forward(100)
t.right(144)
t.forward(100)
t.right(144)


t.speed(5)
t.pensize(2)
t.pencolor('white')
t.fillcolor('white')

t.penup()
t.goto(-50, 300)
t.pendown()

t.begin_fill()
t.circle(40)
t.penup()
t.goto(0, 290)
t.pendown()
t.circle(50)
t.penup()
t.goto(60, 320)
t.pendown()
t.circle(40)
t.penup()
t.goto(20, 270)
t.pendown()
t.circle(60)
t.end_fill()

t.goto(-200,200)
t.forward(100)
t.backward(100)
t.right(60)

t.forward(100)
t.backward(100)
t.right(60)

t.forward(100)
t.backward(100)
t.right(60)

t.forward(100)
t.backward(100)
t.right(60)

t.forward(100)
t.backward(100)
t.right(60)

t.forward(100)
t.backward(100)

t.done()