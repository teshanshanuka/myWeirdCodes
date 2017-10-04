import serial, time
import matplotlib.pyplot as plt

PORT = '/dev/ttyACM0'
baudrate = 9600

def setupRTplot(initXrange, initYrange):
    """initXrange: in the form of [(x1min, x1max), (..), ..], and the same goes for initYrange."""
    global pts, x, y
    x = []
    y = []

    fig, ax = plt.subplots()
    pts, = ax.plot(x, y)
    ax.set_xlim(initXrange[0], initXrange[1])
    ax.set_ylim(initYrange[0], initYrange[1])

def drawRTplot(coord):
    """input:tuple of new coordinates (x,y)"""
    global x, y, pts
    x_coord, y_coord = coord
    x.append(x_coord)
    y.append(y_coord)
    pts.set_data(x, y)
    plt.pause(0.001)

startTime = time.time()
setupRTplot((0, 60), (-1,1))

with serial.Serial(PORT, baudrate, timeout=1) as ser:
    line = ser.readline().decode('utf-8').replace("\r\n", '')
    while True:
        try:
            line = ser.readline().decode('utf-8').replace("\r\n", '')
            t = time.time() - startTime
            try:
                num = float(line)*10
                print(num)
                drawRTplot((t, num))
            except ValueError:
                print('Error converting to float')
                print(line)
        except KeyboardInterrupt:
            print()
            plt.show(block=True)
            break
