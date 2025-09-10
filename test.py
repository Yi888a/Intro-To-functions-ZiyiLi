import turtle
from turtle import *
t = Turtle()
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
for i in range(60):
    square(200)
    t.right(5)