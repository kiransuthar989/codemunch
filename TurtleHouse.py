
import turtle
import math
 
wn = turtle.Screen()
wn.bgcolor("yellow")
bob = turtle.Turtle()
bob.shape("turtle")

# alex = turtle.Turtle()
# alex.shape("turtle")
# alex.speed(1)

# distance = 20
# direction = 45
# alex.penup()
# for i in ["blue", "green", "red", "purple"]:
    # alex.color(i)
    # alex.pensize(1)
    # alex.stamp()
    # alex.forward(distance)
    # alex.left(direction)
    # alex.forward(distance)
    # alex.right(direction)
    # distance += 10

angle = 90
distant = 50
 
bob.right(angle)
for i in range(3):
   bob.forward(distant)
   bob.left(angle)
 
bob.forward(distant)
bob.right(135)
 
dist = math.sqrt(distant ** 2 / 2)
bob.forward(dist)
bob.right(90)
bob.forward(dist)

wn.exitonclick()
