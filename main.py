from turtle import Turtle , Screen



tim = Turtle()
screen=Screen()
#
# def move_forward():
#     tim.forward(30)
# def move_up():
#     if (tim)
#     tim.left(90)
def move_up():
    tim.setheading(90)
def move_down() :
    tim.setheading(-90)
def turn_right() :
    tim.setheading(0)
def turn_left():
    tim.setheading(180)
def move_forward() :
    tim.forward(20)
def clear_drawing():
    tim.clear()
    tim.penup()
    tim.setx(0)
    tim.sety(0)

screen.listen()
screen.onkey(key="Up" , fun=move_up)
screen.onkey(key="Down" , fun=move_down)
screen.onkey(key="Right" , fun=turn_right)
screen.onkey(key="Left" ,  fun=turn_left)
screen.onkey(key="space" , fun=move_forward)
screen.onkey(key="c" , fun=clear_drawing)
screen.exitonclick()