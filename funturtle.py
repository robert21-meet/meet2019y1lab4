
import turtle
turtle.shape("turtle")
def up():
    turtle.onkeypress("w")
    turtle.pos()
    turtle.goto(turtle.xcor(),turtle.ycor()+10)
def down():
    turtle.onkeypress("s")
    turtle.pos()
    turtle.goto(turtle.xcor(),turtle.ycor()-10)
def left():
    turtle.onkeypress("a")
    turtle.pos()
    turtle.goto(turtle.xcor()-10,turtle.ycor())
def right():
    turtle.onkeypress("d")
    turtle.pos()
    turtle.goto(turtle.xcor()+10,turtle.ycor())

turtle.onkeypress(up,"w")
turtle.onkeypress(down,"s")
turtle.onkeypress(left,"a")
turtle.onkeypress(right,"d")
turtle.listen()

turtle.mainloop()
