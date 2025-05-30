import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make a random walk and plot the points

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth=1)

plt.show()