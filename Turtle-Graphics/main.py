from turtle import Turtle#from turtle module we are goint to import Turtle class
from turtle import Screen

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")#we can use cirle, square etc shapes also
#timmy_the_turtle.color("blue")#we can use here any color
#timmy_the_turtle.forward(100)
#timmy_the_turtle.backward(200)
#timmy_the_turtle.left(120)
#timmy_the_turtle.right(90)


#now we can draw a simple score by the help of these lines
#timmy_the_turtle.forward(100)
#timmy_the_turtle.left(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.left(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.left(90)
#timmy_the_turtle.forward(100)
#timmy_the_turtle.left(90)
#Or instead of these lines of code we can use
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)








#After running this code we have to create another object which we'll call our screen
#screen = Screen()# we also have to import it from turtle
#screen.exitonclick()
