import turtle as t
import random

tim = t.Turtle()
t.colormode(255)#We changed the color mode we can now create a random color
def random_color():
    r = random.randint(0, 255)#red
    g = random.randint(0, 255)#green
    b = random.randint(0, 255)#blue
    #or
    #r = random.randint(0, 54)#red
    #g = random.randint(0, 25)#green
    #b = random.randint(0, 255)#blue
    random_color = (r, g, b)#here is our tuple created and this is basically a new random color
    return random_color# this fxn will return a random color as output


directions = [0, 90, 180, 270] #here the directions used i;e 0 = East , 90 = north, 180 = west and 270 = south
tim.pensize(5)# It will increase the width of line
tim.speed("fastest")#It helps to increase the speed of tim or turtle
for _ in range(200):#200 is the range used for loop to run
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
