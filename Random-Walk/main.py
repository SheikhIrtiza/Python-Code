import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SeaGreen"]
directions = [0, 90, 180, 270] #here the directions used i;e 0 = East , 90 = north, 180 = west and 270 = south
tim.pensize(5)# It will increase the width of line
tim.speed("fastest")#It helps to increase the speed of tim or turtle
for _ in range(200):#200 is the range used for loop to run
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


