import threading
import time

def myFunc(no):
    print('myFunc', no)
    for i in range(10):
        print(no, ':', i)
        time.sleep(0.5)

# threads = []
for i in range(5):
    myThread = threading.Thread(target=myFunc, args=(i,))
    # threads.append(myThread)
    myThread.start()
    if i is not 0:
        myThread.join()
