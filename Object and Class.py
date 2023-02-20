import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen

tinny = Turtle()
print(tinny)
tinny.shape("turtle")#It will change the shape of turtle
tinny.color("coral")
tinny.forward(100)

my_screen = Screen()
print(my_screen.canvheight)#height of canves that the screen creates and screen is object and that canvas height is an attribute.
# and here in line 13 i.e{print(my_screen.canvheight)}  we can call methods that are associated with the object
my_screen.exitonclick()#my_screen = fxn, fxn is tied to objects so its actually called method
#method name is exitonclick and this will allow our program to continue running untill we click on the screen and then it exit our code

#we can create a new Object from a blueprint, we can tap into its attributes by using the object name dot then the name of the attribute
 
