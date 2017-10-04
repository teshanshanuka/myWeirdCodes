import numpy as np
import matplotlib.pyplot as plt

omega = lambda omega0, F, r, I, t: omega0 + (F*r*t)/I

simTime = 60
timestep = 0.005

time = np.arange(0,simTime,timestep)
force = np.array([0.5]*(len(time)//3)+[0]*(len(time)-2*(len(time)//3))+[-0.6]*(len(time)//3))

avel = [0]

for i, t in enumerate(time[1:]):
    avel.append(omega(avel[i], force[i], 0.2, 0.5, timestep))

# plt.plot(time, avel)
# plt.show()

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
ax.set_title("Wheel Sim", va='bottom')

for omega in avel:
    try:
        theta += omega*timestep
        ball.set_data(theta, 1)
        plt.pause(timestep)
    except KeyboardInterrupt:
        break

plt.show()
