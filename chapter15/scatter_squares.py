import matplotlib.pyplot as plt

#our data to plot
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

#style the plot
plt.style.use('Solarize_Light2')

#fig is the whole picture frame, ax is the canvas we draw our plot on. this setup gives us full control over what we are plotting be it a single plot or multiple
fig, ax =plt.subplots()

#this says draw our scatter point at the ffg co-ordinates, s is the size of the dots
ax.scatter(x_values, y_values, s=100)

#set chart title and label axes.
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#set size of tick labels
ax.tick_params(labelsize=14)

plt.show()