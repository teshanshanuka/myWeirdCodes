import rtplot
import math

rtplot.setupRTplot(1, 2, [(0,50),(-10,60)], [(-1.5,1.5),(-1,1)])

list_1 = [(x,math.sin(x/20)) for x in range(50)]
list_2 = [(x,math.cos(x/20)) for x in range(50)]

for i in range(len(list_1)):
    rtplot.drawRTplot([list_1[i], list_2[i]])

rtplot.holdOn()
