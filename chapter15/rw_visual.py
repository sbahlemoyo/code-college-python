import matplotlib.pyplot as plt
from random_walk import RandomWalk

#make a random walk and plot the points

while True:
    rw = RandomWalk()
    rw.fill_walk()
    
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=1)
    
    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running.lower() == 'n':
        break   