import turtle as t

tom = t.Turtle()
scr = t.Screen()


def move_forward():
    tom.forward(50)
def move_backward():
    tom.backward(50)
def turn_left():
    new_heading = tom.heading() + 20
    tom.setheading(new_heading)
def turn_right():
    new_heading = tom.heading() - 20
    tom.setheading(new_heading)


scr.listen()
scr.onkey(move_forward, "w")
scr.onkey(move_backward, "s")
scr.onkey(turn_left, "a")
scr.onkey(turn_right, "d")


scr.exitonclick()
