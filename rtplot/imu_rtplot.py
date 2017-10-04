# This is written to use with MPU9250 in order to plot x,y,z readings of an accelerometer, gyoscope, magnetometer and the temperature reading
# in four subplots
import matplotlib.pyplot as plt
from time import time

def setupRTplot(initTimeRange, initYrange):
    """initTimeRange: max time axis value
    initYrange: in the form of [(y1min, y1max), (..), ..],.
    in the order of [(Accelerometer), (Gyroscope), (Magnetometer), (Temperature)]"""
    global pts, x, Y, time0

    time0 = time()
    x = []
    Y = [[] for i in range(10)]
    pts = [[] for i in range(10)]

    fig, ax = plt.subplots(nrows=4, ncols=1)

    for i in range(3):
        pts[i], = ax[0].plot(x, Y[i])

    for i in range(3,6):
        pts[i], = ax[1].plot(x, Y[i])

    for i in range(6,9):
        pts[i], = ax[2].plot(x, Y[i])

    pts[9], = ax[3].plot(x, Y[9])

    for i in range(4):
        ax[i].set_xlim(0, initTimeRange)
        ax[i].set_ylim(initYrange[i][0], initYrange[i][1])

def drawRTplot(valueSet):
    """input: list [(accel x,y,z), (gyro x,y,z), (mag x, y, z), temp]"""
    global pts, x, Y
    x.append(time() - time0)

    for i in range(3):
        Y[i].append(valueSet[0][i])

    for i in range(3,6):
        Y[i].append(valueSet[1][i-3])

    for i in range(6,9):
        Y[i].append(valueSet[2][i-6])

    Y[9].append(valueSet[3])

    for i in range(10):
        pts[i].set_data(x, Y[i])

    plt.pause(0.001)

def holdOn():
    plt.show(block=True)

if __name__ =='__main__':
    import math
    from time import sleep

    setupRTplot(60, [(-1,1), (-1,1), (-1,1), (0,10)])
    R = 500

    accel = [[math.sin(x/20) for x in range(R)],
                [math.cos(x/20) for x in range(R)],
                [math.sin((x+25)/20) for x in range(R)]]
    accel = list(zip(*accel))

    gyro = [[math.sin(x/20) for x in range(R)],
                [math.cos(x/20) for x in range(R)],
                [math.sin((x+50)/20) for x in range(R)]]
    gyro = list(zip(*gyro))

    mag = [[math.sin(x/20) for x in range(R)],
                [math.cos(x/20) for x in range(R)],
                [math.sin((x+75)/20) for x in range(R)]]
    mag = list(zip(*mag))

    temp = [math.sin(x/200)+8 for x in range(R)]

    for i in range(R):
        drawRTplot([accel[i], gyro[i], mag[i], temp[i]])
        sleep(0.2)
    # drawRTplot([accel[0], gyro[0], mag[0], temp[0]])
    holdOn()
