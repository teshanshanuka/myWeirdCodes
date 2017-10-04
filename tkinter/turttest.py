import turtle

turt = turtle.Turtle()

sc = turtle.Screen()
sc.bgcolor('green')

turt.color('red', 'yellow')
turt.begin_fill()
initpos = turtle.Vec2D(-100,0)
turt.penup()
turt.setpos(initpos)
turt.pendown()
while True:
    turt.forward(200)
    turt.right(120)#(170)
    if abs(turt.pos()-initpos) < 1:
        break
turt.end_fill()

sc.exitonclick()