import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125] #Cubes of x_values

plt.style.use('Solarize_Light2')

fig, ax = plt.subplots() #set the canvas and plane for the plot to be drawn

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.inferno , s=100)

ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

ax.ticklabel_format(style='plain')

ax.tick_params(labelsize=14)

plt.savefig('cubes3_plot.png', bbox_inches='tight')