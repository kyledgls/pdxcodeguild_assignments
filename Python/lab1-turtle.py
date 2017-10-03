from turtle import *

# draws legs
right(45)
forward(125)
backward(125)
right(90)
forward(125)
backward(125)
#draws body
right(135)
forward(150)
# draw arms
right(90)
forward(100)
left(180)
forward(200)
right(180)
forward(100)
#draw neck
left(90)
forward(25)
#draw head
left(90)

edge_length = 220
n_sides = 30

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1


done()
