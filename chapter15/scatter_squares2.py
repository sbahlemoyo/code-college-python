import matplotlib.pyplot as plt

#our data to plot
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

#style the plot
plt.style.use('Solarize_Light2')

#fig is the whole picture frame, ax is the canvas we draw our plot on. this setup gives us full control over what we are plotting be it a single plot or multiple
fig, ax =plt.subplots()

#this says draw our scatter point at the ffg co-ordinates, s is the size of the dots
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.scatter(x_values, y_values, color='red', s=10)
# ax.scatter(x_values, y_values,color=(0, 0.8, 0) s=10) #uses rgb for color scheme

#set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#set the range for each axis
ax.axis([0, 1100, 0, 1_100_000])

#ovrride ticklabel default format that resorts to using exponential notation when the axis have too high ranges
ax.ticklabel_format(style='plain')

#set size of tick labels
ax.tick_params(labelsize=14)

#if you want to save plot image to file in system instead of showing it directly in matplotlib viewer
plt.savefig('squares_plot.png', bbox_inches='tight')

# plt.show()