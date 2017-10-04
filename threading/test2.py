import threading, time

def myTh(threadNo):
	for j in range(5):
		print(threadNo, ':', j)
		time.sleep(1)
	return

for i in range(4):
	t = threading.Thread(target=myTh, args=(i,))
	t.start()

# import threading

# def worker(num):
#     """thread worker function""" 
#     for j in range(5):
# 	    print('Worker: %s : %d\n' % (num,j))
#     return

# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
time.sleep(10)
input('Press enter to continue...')