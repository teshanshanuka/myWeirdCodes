import numpy.random as npr
import datetime as dt

def getNextTimestamp(time):
    return time+dt.timedelta(0, int(npr.choice([16,17])))

t = getNextTimestamp(dt.datetime(100,1,1,0,0,0))
templist = [36.95,36.98,37.02,37.05,37.08,37.12,37.15,37.19]

for i in range(30):
    filename = str(i)+'.TXT'
    with open(filename, 'w') as f:

        tempPos = npr.choice(range(len(templist)))
        line = str(t.time())+','+str(templist[tempPos])+',\n'
        f.write(line)

        while True:
            t = getNextTimestamp(t)
            if t.day > i+1:
                break
            if tempPos == 0 or tempPos == 1:
                tempPos = 2
            elif tempPos == len(templist) or tempPos == len(templist)-1:
                tempPos = len(templist) - 2
            tempPos = (tempPos + npr.choice([1,2,-1,-2,0,0,0]))%len(templist)

            line = str(t.time())+','+str(templist[tempPos])+',\n'
            f.write(line)

    f.close()
