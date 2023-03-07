import turtle as t
import random

tim = t.Turtle()
t.colormode(255)#We changed the color mode we can now create a random color
def random_color():
    r = random.randint(0, 255)#red
    g = random.randint(0, 255)#green
    b = random.randint(0, 255)#blue
    color = (r, g, b)#here is our tuple created and this is basically a new random color
    return color# this fxn will return a random color as output



tim.speed("fastest")#It helps to increase the speed of tim or turtle
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):#Its stopping only once it's gone through the hundred rotations
        tim.color(random_color())
        tim.circle(100)#100 is the radius of the circle
        tim.setheading(tim.heading() + size_of_gap)
draw_spirograph(5) #Here we are going to call this method draw_spirograph


screen = t.Screen()
screen.exitonclick()
