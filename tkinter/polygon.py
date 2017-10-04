from tkinter import *
from math import sqrt

canvas_width = 500
canvas_height = 500

points_clicked = 0
init_point = prev_point = None
poly = []
turt = []
STATE = 0

def check_dist(point1, point2):
	return sqrt((point1.x-point2.x)**2+(point1.y-point2.y)**2)

def isPointInPath(x, y, poly):
	"""https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule"""
	num = len(poly)
	i = 0
	j = num - 1
	c = False
	for i in range(num):
		if  ((poly[i][1] > y) != (poly[j][1] > y)) and \
				(x < (poly[j][0] - poly[i][0]) * (y - poly[i][1]) / (poly[j][1] - poly[i][1]) + poly[i][0]):
			c = not c
		j = i
	return c

def isGradientBetween(p0,newPoint,lp1,lp2):
	"""Check whether gradient of line[p0,newPoint] is in between gradient of\
	lines [p0,lp1] and [p0,lp2]"""
	grad = lambda line:(line[1][1]-line[0][1])/(line[1][0]-line[0][0])
	l1grad = grad([p0,lp1])
	l2grad = grad([p0,lp2])
	lgrad = grad([p0, newPoint])
	print(l1grad,l2grad,lgrad)
	if not min(l1grad,l2grad) < lgrad < max(l1grad,l2grad):
		crossLine = True

def lineCrossPath(poly, newpoint):
	num = len(poly)
	if num < 3:
		return False
	crossLine = False
	newpoint = [newpoint.x, newpoint.y]
	p0 = [poly[num-1][0], poly[num-1][1]]
	for i in range(num-2):
		if isGradientBetween(p0, newpoint, poly[i], poly[i+1]) and isGradientBetween(poly[i], poly[i+1], p0, newpoint):
			crossLine = True
			break
	return crossLine


class turtle():
	def __init__(self, position, velocity):
		self.position = position
		self.velocity = velocity

def draw_polygon(new_point, FINISH = False):
	global points_clicked, init_point, prev_point, poly, STATE

	if points_clicked == 0:
		init_point = prev_point = new_point
		poly.append((new_point.x, new_point.y))
	elif FINISH == True or (points_clicked > 3 and check_dist(new_point, init_point) <= 10):
		w.create_line(prev_point.x, prev_point.y, init_point.x, init_point.y)
		#hence now finished drawing polygon
		message.pack_forget()
		but.pack(side = BOTTOM)
		STATE = 1
	else:
		if not lineCrossPath(poly, new_point):
			w.create_line(prev_point.x, prev_point.y, new_point.x, new_point.y)
			prev_point = new_point
			poly.append((new_point.x, new_point.y))
	points_clicked +=1

def finish_polygon(event):
	if STATE == 0:
		draw_polygon(event)
		draw_polygon(event, True)

def place_turtle(turtle_point):
	global turt
	if(isPointInPath(turtle_point.x, turtle_point.y,poly)):
		turt.append(turtle([turtle_point.x, turtle_point.y], [0,0]))
		w.create_oval(turtle_point.x-2, turtle_point.y-2,turtle_point.x+2, turtle_point.y+2)

def enufturtles():
	global STATE
	STATE = 2

def paint( new_point ):
	if STATE == 0:
		draw_polygon(new_point)

	elif STATE == 1:
		place_turtle(new_point)

master = Tk()
master.title( "WOW!" )

w = Canvas(master,
			width=canvas_width,
			height=canvas_height)
w.pack(expand = NO, fill = BOTH)

# Bind mouse click
w.bind( "<Button-1>", paint )
w.bind( "<Double-Button-1>", finish_polygon)

message = Label( master, text = "Click to draw polygon" )
message.pack( side = BOTTOM )
but = Button(master, text = "Finish", command = enufturtles)

mainloop()
