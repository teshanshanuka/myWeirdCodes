import matplotlib.pyplot as plt
import math

def setupRTplot(plotRows, plotCols, initXrange, initYrange):
    """initXrange: in the form of [(x1min, x1max), (..), ..], and the same goes for initYrange.
    this can only draw plots in 1D. Either plotRows or plotCols should be 1 and both cannot be 1 at once"""
    global points, x, y
    x = [[] for i in range(plotRows*plotCols)]
    y = [[] for i in range(plotRows*plotCols)]
    points = []

    fig, ax = plt.subplots(nrows=plotRows, ncols=plotCols)
    for i in range(plotRows*plotCols):
        pts, = ax[i].plot(x[i], y[i])
        points.append(pts)
        ax[i].set_xlim(initXrange[i][0], initXrange[i][1])
        ax[i].set_ylim(initYrange[i][0], initYrange[i][1])

def drawRTplot(valueSet):
    """input: array of new coordinate tuples in the form of [(x1,y1), (x2,y2)...]"""
    global x, y, points
    for i in range(len(valueSet)):
        x_coord, y_coord = valueSet[i]
        x[i].append(x_coord)
        y[i].append(y_coord)
        points[i].set_data(x[i], y[i])
    plt.pause(0.001)

def holdOn():
    plt.show(block=True)
