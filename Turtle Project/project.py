import turtle
def my_paint():
	window = turtle.Screen()
	window.bgcolor("#ffffff")
	obj = turtle.Turtle()
	obj.color("#000000")
	obj.pensize(2)
	obj.speed(1000)
	obj.forward(2)
	obj.left(120)
	obj.forward(5)
	obj.left(120)
	obj.forward(7)
	obj.left(120)
	obj.forward(10)
	i = 5
	while i < 1000:
		obj.left(120 + 1)
		obj.forward(10 + i)
		i = i + 3
	window.exitonclick()
my_paint()