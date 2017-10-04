import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

x1 = []
y1 = []
x2 = []
y2 = []

xx = 10

list_1 = [(x,math.sin(x/20)) for x in range(xx)]
list_2 = [(x,math.cos(x/20)) for x in range(xx)]

points_1, = ax[0].plot(x1, y1, color = 'red')
points_2, = ax[1].plot(x2, y2)
ax[0].set_xlim(0, len(list_1))
ax[0].set_ylim(-1, 1)
ax[1].set_xlim(0, len(list_2))
ax[1].set_ylim(-1, 1)

for t in range(len(list_1)):
    x1_coord, y1_coord = list_1[t]
    x2_coord, y2_coord = list_2[t]
    x1.append(x1_coord)
    y1.append(y1_coord)
    x2.append(x2_coord)
    y2.append(y2_coord)
    points_1.set_data(x1, y1)
    points_2.set_data(x2, y2)
    plt.pause(0.001)

ax[0].set_xlim(0, len(list_1)+10)
# points_1.set_data(x1+[len(list_1)], y1+[1])
plt.pause(0.001)

plt.show(block=True)
