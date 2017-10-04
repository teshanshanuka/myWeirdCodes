import turtle, time, threading
from random import random, randint

MAX_ANGLE = 90
MAX_DIST = 30
ECHO_INTERVAL = 1

t = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor('red')
t.speed(1)

def randAngle():
    return random()*MAX_ANGLE

def randDist():
    return random()*MAX_DIST

def randBinary():
    return randint(0,1)

def runTurtle():
    try:
        while True:
            t_x = t.pos().__getitem__(0)
            t_y = t.pos().__getitem__(1)
            x_max = sc.window_width()/2 - MAX_DIST
            y_max = sc.window_height()/2 - MAX_DIST
            if(abs(t_x) >= x_max or abs(t_y) >= y_max):
                t.right(180)
                t.forward(MAX_DIST)
            elif(randBinary()):
                t.left(randAngle())
                t.forward(randDist())
            else:
                t.right(randAngle())
                t.forward(randDist())
    except KeyboardInterrupt:
        print('Turtle Stopped!')

def echoPos():
    while True:
        print(t.pos())
        time.sleep(ECHO_INTERVAL)

if __name__=='__main__':
    ethread = threading.Thread(target=echoPos)
    ethread.daemon = True
    ethread.start()
    runTurtle()
