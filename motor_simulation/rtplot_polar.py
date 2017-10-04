import matplotlib.pyplot as plt
import numpy as np

a360 = np.arange(0, 2*np.pi, 0.01)
r = np.array([1]*len(a360))
ax = plt.subplot(111, projection='polar')


ax.plot(a360, r)

theta = 0
ball, = ax.plot(theta, 1, 'ro', markersize=20)

ax.set_rmax(1.5)
ax.set_rticks([])  # less radial ticks
# ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)
ax.set_title("A line plot on a polar axis", va='bottom')

while theta < 2*np.pi:
    try:
        ball.set_data(theta, 1)
        theta += 0.1
        plt.pause(0.001)
    except KeyboardInterrupt:
        break

plt.show()
