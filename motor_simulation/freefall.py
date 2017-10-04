import rtplot
from time import time
import matplotlib.pyplot as plt
import numpy as np

G = 9.81 #gravitational constatnt

v = lambda u, m, C, g, t: u+(m*g-u*C)*t

simTime = 200
timestep = 0.5

time = np.arange(0,simTime,timestep)
vel1 = [0]
vel2 = [-5]
for i, t in enumerate(time[1:]):
    vel1.append(v(vel1[i], 0.5, 0.1, G, timestep))
    vel2.append(v(vel2[i], 1, 0.05, G, timestep))

plt.plot(time, vel1)
plt.plot(time, vel2, 'r-')
plt.show()
