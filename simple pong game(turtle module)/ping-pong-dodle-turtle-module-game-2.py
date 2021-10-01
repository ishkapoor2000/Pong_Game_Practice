import turtle
import winsound
#import os
wn = turtle.Screen()
wn.title("PONG BY ISH")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#Score
score_a = 0
score_b = 0
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2
#Pen_1
pen_1 = turtle.Turtle()
pen_1.speed(0)
pen_1.shape("square") 
pen_1.color("white")
pen_1.penup()
pen_1.hideturtle()
pen_1.goto(0, 260)
pen_1.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))
#Pen_2
pen_2 = turtle.Turtle()
pen_2.speed(0)
pen_2.shape("square")
pen_2.color("white")
pen_2.penup()
pen_2.hideturtle()
pen_2.goto(-400, -300)
pen_2.write("ISH GAMING CLUB", align="left", font=("Courier", 16, "normal"))
#Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 60#20
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 60#20
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += 60#20
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 60#20
    paddle_b.sety(y)
#Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
#Main game loop
while True:
    wn.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border checking
    #Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("afplay bounce.wav&")
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("afplay bounce.wav&")
    #Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen_1.clear()
        pen_1.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    elif ball.xcor() < -350:
        score_b += 1
        pen_1.clear()
        pen_1.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        #Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("afplay bounce.wav&")
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("afplay bounce.wav&")