#!/env/python3

from tkinter import *
from math import atan2, degrees

canvas_width = 500
canvas_height = 500

# find angle of pt1 from pt0 from east(+x axis)
def angle(pt0, pt1):
	return degrees(atan2((pt1[1]-pt0[1]),(pt1[0]-pt0[0])))

def pr(pt):
	print(pt.x, pt.y)
	print(w.winfo_width)

print(angle([0,0],[2,2]))

master = Tk()
master.title( "Test" )

w = Canvas(master,
			width=canvas_width,
			height=canvas_height)
w.pack(expand = YES, fill = BOTH)

# Bind mouse click
w.bind( "<Button-1>", pr )
# print(dir(w))

message = Label( master, text = "Click to draw polygon" )
message.pack( side = BOTTOM )

mainloop()

input("press any key to continue")
