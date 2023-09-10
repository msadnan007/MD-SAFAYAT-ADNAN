#Name:MD.JUBAYER HOSSAIN
#Student ID: 202312117

import turtle
def setup():
	turtle.title("Assignment 2")
	turtle.setup(1000,1000,0,0)
	turtle.hideturtle()

def draw_hexa(size):
	turtle.forward(size)
	turtle.right(60)
	turtle.forward(size)
	turtle.right(60)
	turtle.forward(size)
	turtle.right(60)
	turtle.forward(size)
	turtle.right(60)
	turtle.forward(size)
	turtle.right(60)
	turtle.forward(size)
	

setup()

for _ in range(0,12):

	#color

	turtle.pencolor("blue")
	turtle.fillcolor("red")
	turtle.begin_fill()
	draw_hexa(250)
	turtle.right(30)
	turtle.end_fill()



turtle.exitonclick()
turtle.done()
