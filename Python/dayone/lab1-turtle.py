from turtle import *



edge_length = 760
n_sides = 16

i = 0
while i < n_sides:
    forward(edge_length/n_sides)
    left(360/n_sides)
    i = i + 1

left(99)
forward(217)
right(144)
forward(217)
right(144)
forward(217)
right(144)
forward(217)
right(144)
forward(217)
done()