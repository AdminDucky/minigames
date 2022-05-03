# Simple Pong in Python 3
# Made by a tutorial for beginners
# This is simply to allow me learning python

import turtle # Simple preinstalled game engine

score_pa = 0 # Player A score 
score_pb = 0 # Player B score
playera_name = input("What is your name? ")
playerb_name = input("What is the second player's name? ")

def write():
    pen.clear()
    pen.write(f"{playera_name}: {score_pa} || {playerb_name}: {score_pb}", align="center", font=("Courier", 24, "normal"))

deltax = 0.25
deltay = 0.25
wn = turtle.Screen() # Creates window
wn.title("Pong by AdminDuckyie, by a tutorial")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # stops window from updating, speeds up game


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # Turtles by default draw lines as they move, we don't want that
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = deltax # seperates ball movement to x and y, d means delta or "change"
ball.dy = deltay

# Score display (Pen)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
# pen.hideturtle
pen.goto(0, 260)
write()


# Function (movement)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding
wn.listen() # Listens for keyboard input
wn.onkeypress(paddle_a_up, "w") # if user presses w (lowercase only), calls function
wn.onkeypress(paddle_a_down, "s") 
wn.onkeypress(paddle_b_up, "Up") # Upper arrow key
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update() # updates window, only possible bc of line 11
    ball.setx(ball.xcor() + ball.dx) # moves ball on x 
    ball.sety(ball.ycor() + ball.dy) # moves ball on y

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = deltax
        score_pa += 1
        write()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = deltax
        score_pb += 1
        write()

    # Paddle & Ball collisions 
    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.1

    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.1

    
